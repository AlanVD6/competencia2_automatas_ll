# Generated from suma.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,16,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,5,1,11,8,1,10,1,
        12,1,14,9,1,1,1,0,0,2,0,2,0,0,14,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,
        1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,12,5,1,0,0,8,9,5,2,0,0,9,11,5,1,0,
        0,10,8,1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,3,1,
        0,0,0,14,12,1,0,0,0,1,12
    ]

class sumaParser ( Parser ):

    grammarFileName = "suma.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'" ]

    symbolicNames = [ "<INVALID>", "NUM", "MAS", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    NUM=1
    MAS=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(sumaParser.ExprContext,0)


        def EOF(self):
            return self.getToken(sumaParser.EOF, 0)

        def getRuleIndex(self):
            return sumaParser.RULE_root




    def root(self):

        localctx = sumaParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(sumaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(sumaParser.NUM)
            else:
                return self.getToken(sumaParser.NUM, i)

        def MAS(self, i:int=None):
            if i is None:
                return self.getTokens(sumaParser.MAS)
            else:
                return self.getToken(sumaParser.MAS, i)

        def getRuleIndex(self):
            return sumaParser.RULE_expr




    def expr(self):

        localctx = sumaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(sumaParser.NUM)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 8
                self.match(sumaParser.MAS)
                self.state = 9
                self.match(sumaParser.NUM)
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





