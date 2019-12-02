# Generated from gramatica.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\7\6/\n\6\f\6\16\6\62\13\6\3\6")
        buf.write("\6\6\65\n\6\r\6\16\6\66\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2=\2\16\3\2\2\2\4\33\3\2")
        buf.write("\2\2\6 \3\2\2\2\b%\3\2\2\2\n*\3\2\2\2\f;\3\2\2\2\16\22")
        buf.write("\7\b\2\2\17\21\7\r\2\2\20\17\3\2\2\2\21\24\3\2\2\2\22")
        buf.write("\20\3\2\2\2\22\23\3\2\2\2\23\25\3\2\2\2\24\22\3\2\2\2")
        buf.write("\25\26\5\4\3\2\26\27\5\6\4\2\27\30\5\b\5\2\30\31\5\n\6")
        buf.write("\2\31\32\7\t\2\2\32\3\3\2\2\2\33\34\7\6\2\2\34\35\7\3")
        buf.write("\2\2\35\36\7\5\2\2\36\37\7\r\2\2\37\5\3\2\2\2 !\7\4\2")
        buf.write("\2!\"\7\3\2\2\"#\7\16\2\2#$\7\r\2\2$\7\3\2\2\2%&\7\7\2")
        buf.write("\2&\'\7\3\2\2\'(\7\16\2\2()\7\r\2\2)\t\3\2\2\2*+\7\n\2")
        buf.write("\2+,\7\3\2\2,\60\7\b\2\2-/\7\r\2\2.-\3\2\2\2/\62\3\2\2")
        buf.write("\2\60.\3\2\2\2\60\61\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2")
        buf.write("\2\63\65\5\f\7\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2")
        buf.write("\2\2\66\67\3\2\2\2\678\3\2\2\289\7\t\2\29:\7\r\2\2:\13")
        buf.write("\3\2\2\2;<\7\f\2\2<=\7\3\2\2=>\7\16\2\2>?\7\r\2\2?\r\3")
        buf.write("\2\2\2\5\22\60\66")
        return buf.getvalue()


class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "'funcionarios'", "<INVALID>", 
                     "'tipo'", "'corredores'", "'{'", "'}'", "'livros'", 
                     "'retorna'" ]

    symbolicNames = [ "<INVALID>", "ZETA", "FUNCIONARIOS", "ESPACO", "TIPO", 
                      "CORREDORES", "ABRE_CHAVE", "FECHA_CHAVE", "LIVROS", 
                      "RETORNA", "TYPE", "QUEBRA_LINHA", "NUMERO", "SPACE" ]

    RULE_programa = 0
    RULE_tipo = 1
    RULE_funcionarios = 2
    RULE_corredores = 3
    RULE_livros = 4
    RULE_livro = 5

    ruleNames =  [ "programa", "tipo", "funcionarios", "corredores", "livros", 
                   "livro" ]

    EOF = Token.EOF
    ZETA=1
    FUNCIONARIOS=2
    ESPACO=3
    TIPO=4
    CORREDORES=5
    ABRE_CHAVE=6
    FECHA_CHAVE=7
    LIVROS=8
    RETORNA=9
    TYPE=10
    QUEBRA_LINHA=11
    NUMERO=12
    SPACE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_CHAVE(self):
            return self.getToken(gramaticaParser.ABRE_CHAVE, 0)

        def tipo(self):
            return self.getTypedRuleContext(gramaticaParser.TipoContext,0)


        def funcionarios(self):
            return self.getTypedRuleContext(gramaticaParser.FuncionariosContext,0)


        def corredores(self):
            return self.getTypedRuleContext(gramaticaParser.CorredoresContext,0)


        def livros(self):
            return self.getTypedRuleContext(gramaticaParser.LivrosContext,0)


        def FECHA_CHAVE(self):
            return self.getToken(gramaticaParser.FECHA_CHAVE, 0)

        def QUEBRA_LINHA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.QUEBRA_LINHA)
            else:
                return self.getToken(gramaticaParser.QUEBRA_LINHA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = gramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(gramaticaParser.ABRE_CHAVE)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramaticaParser.QUEBRA_LINHA:
                self.state = 13
                self.match(gramaticaParser.QUEBRA_LINHA)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.tipo()
            self.state = 20
            self.funcionarios()
            self.state = 21
            self.corredores()
            self.state = 22
            self.livros()
            self.state = 23
            self.match(gramaticaParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(gramaticaParser.TIPO, 0)

        def ZETA(self):
            return self.getToken(gramaticaParser.ZETA, 0)

        def ESPACO(self):
            return self.getToken(gramaticaParser.ESPACO, 0)

        def QUEBRA_LINHA(self):
            return self.getToken(gramaticaParser.QUEBRA_LINHA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = gramaticaParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tipo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(gramaticaParser.TIPO)
            self.state = 26
            self.match(gramaticaParser.ZETA)
            self.state = 27
            self.match(gramaticaParser.ESPACO)
            self.state = 28
            self.match(gramaticaParser.QUEBRA_LINHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncionariosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCIONARIOS(self):
            return self.getToken(gramaticaParser.FUNCIONARIOS, 0)

        def ZETA(self):
            return self.getToken(gramaticaParser.ZETA, 0)

        def NUMERO(self):
            return self.getToken(gramaticaParser.NUMERO, 0)

        def QUEBRA_LINHA(self):
            return self.getToken(gramaticaParser.QUEBRA_LINHA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_funcionarios

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionarios" ):
                listener.enterFuncionarios(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionarios" ):
                listener.exitFuncionarios(self)




    def funcionarios(self):

        localctx = gramaticaParser.FuncionariosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcionarios)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(gramaticaParser.FUNCIONARIOS)
            self.state = 31
            self.match(gramaticaParser.ZETA)
            self.state = 32
            self.match(gramaticaParser.NUMERO)
            self.state = 33
            self.match(gramaticaParser.QUEBRA_LINHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CorredoresContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORREDORES(self):
            return self.getToken(gramaticaParser.CORREDORES, 0)

        def ZETA(self):
            return self.getToken(gramaticaParser.ZETA, 0)

        def NUMERO(self):
            return self.getToken(gramaticaParser.NUMERO, 0)

        def QUEBRA_LINHA(self):
            return self.getToken(gramaticaParser.QUEBRA_LINHA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_corredores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCorredores" ):
                listener.enterCorredores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCorredores" ):
                listener.exitCorredores(self)




    def corredores(self):

        localctx = gramaticaParser.CorredoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_corredores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(gramaticaParser.CORREDORES)
            self.state = 36
            self.match(gramaticaParser.ZETA)
            self.state = 37
            self.match(gramaticaParser.NUMERO)
            self.state = 38
            self.match(gramaticaParser.QUEBRA_LINHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LivrosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIVROS(self):
            return self.getToken(gramaticaParser.LIVROS, 0)

        def ZETA(self):
            return self.getToken(gramaticaParser.ZETA, 0)

        def ABRE_CHAVE(self):
            return self.getToken(gramaticaParser.ABRE_CHAVE, 0)

        def FECHA_CHAVE(self):
            return self.getToken(gramaticaParser.FECHA_CHAVE, 0)

        def QUEBRA_LINHA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.QUEBRA_LINHA)
            else:
                return self.getToken(gramaticaParser.QUEBRA_LINHA, i)

        def livro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.LivroContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.LivroContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_livros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLivros" ):
                listener.enterLivros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLivros" ):
                listener.exitLivros(self)




    def livros(self):

        localctx = gramaticaParser.LivrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_livros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(gramaticaParser.LIVROS)
            self.state = 41
            self.match(gramaticaParser.ZETA)
            self.state = 42
            self.match(gramaticaParser.ABRE_CHAVE)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramaticaParser.QUEBRA_LINHA:
                self.state = 43
                self.match(gramaticaParser.QUEBRA_LINHA)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.livro()
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==gramaticaParser.TYPE):
                    break

            self.state = 54
            self.match(gramaticaParser.FECHA_CHAVE)
            self.state = 55
            self.match(gramaticaParser.QUEBRA_LINHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LivroContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(gramaticaParser.TYPE, 0)

        def ZETA(self):
            return self.getToken(gramaticaParser.ZETA, 0)

        def NUMERO(self):
            return self.getToken(gramaticaParser.NUMERO, 0)

        def QUEBRA_LINHA(self):
            return self.getToken(gramaticaParser.QUEBRA_LINHA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_livro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLivro" ):
                listener.enterLivro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLivro" ):
                listener.exitLivro(self)




    def livro(self):

        localctx = gramaticaParser.LivroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_livro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(gramaticaParser.TYPE)
            self.state = 58
            self.match(gramaticaParser.ZETA)
            self.state = 59
            self.match(gramaticaParser.NUMERO)
            self.state = 60
            self.match(gramaticaParser.QUEBRA_LINHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





