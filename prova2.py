import sys
import re
from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from gramaticaListener import gramaticaListener
class gramaticaPrintListener(gramaticaListener):
    space      = ''
    corredors   = 0
    workers     = 0
    totalBooks  = 0
    bookErrors  = []
    # Enter a parse tree produced by gramaticaParser#programa.
    def enterPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#programa.
    def exitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#tipo.
    def enterTipo(self, ctx:gramaticaParser.TipoContext):
        self.space = ctx.ESPACO().getText()

    # Exit a parse tree produced by gramaticaParser#tipo.
    def exitTipo(self, ctx:gramaticaParser.TipoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcionarios.
    def enterFuncionarios(self, ctx:gramaticaParser.FuncionariosContext):
        self.workers = int(ctx.NUMERO().getText())

    # Exit a parse tree produced by gramaticaParser#funcionarios.
    def exitFuncionarios(self, ctx:gramaticaParser.FuncionariosContext):
        pass


    # Enter a parse tree produced by gramaticaParser#corredores.
    def enterCorredores(self, ctx:gramaticaParser.CorredoresContext):
        self.corredors = int(ctx.NUMERO().getText())
        if self.space == 'biblioteca':
            temp = self.corredors / 2
            if not (temp).is_integer():
                temp = int(temp)
                temp += 1
            #we add one because we are goint to lose 1 worker to be atendant
            temp +=1
            if not temp <= self.workers:
                raise Exception('workers need to be >= {} . The value of workers was: {}'.format(temp, self.workers))
        else:
            temp = self.corredors / 4
            if not (temp).is_integer():
                temp = int(temp)
                temp += 1
            if not temp <= self.workers:
                raise Exception('workers need to be >= {} . The value of workers was: {}'.format(temp, self.workers))
    # Exit a parse tree produced by gramaticaParser#corredores.
    def exitCorredores(self, ctx:gramaticaParser.CorredoresContext):
        pass


    # Enter a parse tree produced by gramaticaParser#livros.
    def enterLivros(self, ctx:gramaticaParser.LivrosContext):
        pass

    # Exit a parse tree produced by gramaticaParser#livros.
    def exitLivros(self, ctx:gramaticaParser.LivrosContext):
        if self.space == 'biblioteca':
            temp = self.totalBooks / 12
            if not (temp).is_integer():
                temp = int(temp)
                temp += 1
            if self.corredors < temp:
                raise Exception('corredors need to be >= {} . The value of corredors was: {}'.format(temp, self.corredors))

        else:
            temp = self.totalBooks / 20
            if not (temp).is_integer():
                temp = int(temp)
                temp += 1
            if self.corredors < temp:
                raise Exception('corredors need to be >= {} . The value of corredors was: {}'.format(temp, self.corredors))

    # Enter a parse tree produced by gramaticaParser#livro.
    def enterLivro(self, ctx:gramaticaParser.LivroContext):
        self.totalBooks += int(ctx.NUMERO().getText())
        if  self.space == 'acervo' and int(ctx.NUMERO().getText()) % 2 == 1:
            self.bookErrors.append('The book class: {} hasn`t a pair number of copies'.format(ctx.TYPE().getText()))

    # Exit a parse tree produced by gramaticaParser#livro.
    def exitLivro(self, ctx:gramaticaParser.LivroContext):
        temp = '\n'
        if len(self.bookErrors) > 1:
            for error in self.bookErrors:
                temp += error + '\n'
            raise Exception(temp)
class gramaticaCodeListener(gramaticaListener):
    template = ''
    books = []
    bookTemplate = "'##TYPE##' :{'current':##VAL##, 'total':##VAL##}"
    # Enter a parse tree produced by gramaticaParser#programa.
    def enterPrograma(self, ctx:gramaticaParser.ProgramaContext):
        self.template = open('./template.txt','r').read()

    # Exit a parse tree produced by gramaticaParser#programa.
    def exitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        self.template = re.sub(r'##BOOKS##', ','.join(self.books), self.template)
        open('./result.py','w').write(self.template)


    # Enter a parse tree produced by gramaticaParser#tipo.
    def enterTipo(self, ctx:gramaticaParser.TipoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#tipo.
    def exitTipo(self, ctx:gramaticaParser.TipoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcionarios.
    def enterFuncionarios(self, ctx:gramaticaParser.FuncionariosContext):
        pass
    # Exit a parse tree produced by gramaticaParser#funcionarios.
    def exitFuncionarios(self, ctx:gramaticaParser.FuncionariosContext):
        pass


    # Enter a parse tree produced by gramaticaParser#corredores.
    def enterCorredores(self, ctx:gramaticaParser.CorredoresContext):
        pass
    # Exit a parse tree produced by gramaticaParser#corredores.
    def exitCorredores(self, ctx:gramaticaParser.CorredoresContext):
        pass


    # Enter a parse tree produced by gramaticaParser#livros.
    def enterLivros(self, ctx:gramaticaParser.LivrosContext):
        pass

    # Exit a parse tree produced by gramaticaParser#livros.
    def exitLivros(self, ctx:gramaticaParser.LivrosContext):
        pass
    # Enter a parse tree produced by gramaticaParser#livro.
    def enterLivro(self, ctx:gramaticaParser.LivroContext):
        temp = re.sub(r'##VAL##', ctx.NUMERO().getText(), self.bookTemplate)
        self.books.append(re.sub(r'##TYPE##', ctx.TYPE().getText(), temp))
    # Exit a parse tree produced by gramaticaParser#livro.
    def exitLivro(self, ctx:gramaticaParser.LivroContext):
        pass

def main(argv):
  input = FileStream(argv[1])
  lexer = gramaticaLexer(input)
  stream = CommonTokenStream(lexer)
  parser = gramaticaParser(stream)
  tree = parser.programa()
  # print(tree.toStringTree(recog=parser))
  printer = gramaticaPrintListener()
  printer = gramaticaCodeListener()
  walker = ParseTreeWalker()
  walker.walk(printer, tree)
if __name__ == '__main__':
  main(sys.argv)
