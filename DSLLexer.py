# Generated from gramatica.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\6\13W\n\13\r\13\16\13X\3\f\6\f\\\n\f")
        buf.write("\r\f\16\f]\3\r\6\ra\n\r\r\r\16\rb\3\r\3\r\2\2\16\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3")
        buf.write("\2\5\4\2\f\f\17\17\3\2\62;\4\2\13\13\"\"\2h\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\36\3")
        buf.write("\2\2\2\7+\3\2\2\2\t\60\3\2\2\2\13;\3\2\2\2\r=\3\2\2\2")
        buf.write("\17?\3\2\2\2\21F\3\2\2\2\23N\3\2\2\2\25V\3\2\2\2\27[\3")
        buf.write("\2\2\2\31`\3\2\2\2\33\34\7/\2\2\34\35\7@\2\2\35\4\3\2")
        buf.write("\2\2\36\37\7h\2\2\37 \7w\2\2 !\7p\2\2!\"\7e\2\2\"#\7k")
        buf.write("\2\2#$\7q\2\2$%\7p\2\2%&\7c\2\2&\'\7t\2\2\'(\7k\2\2()")
        buf.write("\7q\2\2)*\7u\2\2*\6\3\2\2\2+,\7v\2\2,-\7k\2\2-.\7r\2\2")
        buf.write("./\7q\2\2/\b\3\2\2\2\60\61\7e\2\2\61\62\7q\2\2\62\63\7")
        buf.write("t\2\2\63\64\7t\2\2\64\65\7g\2\2\65\66\7f\2\2\66\67\7q")
        buf.write("\2\2\678\7t\2\289\7g\2\29:\7u\2\2:\n\3\2\2\2;<\7}\2\2")
        buf.write("<\f\3\2\2\2=>\7\177\2\2>\16\3\2\2\2?@\7n\2\2@A\7k\2\2")
        buf.write("AB\7x\2\2BC\7t\2\2CD\7q\2\2DE\7u\2\2E\20\3\2\2\2FG\7t")
        buf.write("\2\2GH\7g\2\2HI\7v\2\2IJ\7q\2\2JK\7t\2\2KL\7p\2\2LM\7")
        buf.write("c\2\2M\22\3\2\2\2NO\7]\2\2OP\7c\2\2PQ\7/\2\2QR\7|\2\2")
        buf.write("RS\7_\2\2ST\7-\2\2T\24\3\2\2\2UW\t\2\2\2VU\3\2\2\2WX\3")
        buf.write("\2\2\2XV\3\2\2\2XY\3\2\2\2Y\26\3\2\2\2Z\\\t\3\2\2[Z\3")
        buf.write("\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^\30\3\2\2\2_a\t")
        buf.write("\4\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2cd\3\2\2")
        buf.write("\2de\b\r\2\2e\32\3\2\2\2\6\2X]b\3\2\3\2")
        return buf.getvalue()


class DSLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ZETA = 1
    FUNCIONARIOS = 2
    TIPO = 3
    CORREDORES = 4
    ABRE_CHAVE = 5
    FECHA_CHAVE = 6
    LIVROS = 7
    RETORNA = 8
    TYPE = 9
    QUEBRA_LINHA = 10
    NUMERO = 11
    SPACE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'->'", "'funcionarios'", "'tipo'", "'corredores'", "'{'", "'}'", 
            "'livros'", "'retorna'", "'[a-z]+'" ]

    symbolicNames = [ "<INVALID>",
            "ZETA", "FUNCIONARIOS", "TIPO", "CORREDORES", "ABRE_CHAVE", 
            "FECHA_CHAVE", "LIVROS", "RETORNA", "TYPE", "QUEBRA_LINHA", 
            "NUMERO", "SPACE" ]

    ruleNames = [ "ZETA", "FUNCIONARIOS", "TIPO", "CORREDORES", "ABRE_CHAVE", 
                  "FECHA_CHAVE", "LIVROS", "RETORNA", "TYPE", "QUEBRA_LINHA", 
                  "NUMERO", "SPACE" ]

    grammarFileName = "gramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


