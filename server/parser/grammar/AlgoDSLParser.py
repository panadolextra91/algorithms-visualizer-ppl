# Generated from grammar/AlgoDSL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\5\2\22\n\2\3\3\3\3\3\3\5\3\27\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\5\5 \n\5\3\5\3\5\3\6\3\6\3\6\7\6\'\n")
        buf.write("\6\f\6\16\6*\13\6\3\6\2\2\7\2\4\6\b\n\2\5\4\2\f\f\17\17")
        buf.write("\4\2\r\r\20\20\4\2\16\16\21\21\2.\2\21\3\2\2\2\4\26\3")
        buf.write("\2\2\2\6\30\3\2\2\2\b\35\3\2\2\2\n#\3\2\2\2\f\22\5\4\3")
        buf.write("\2\r\22\5\6\4\2\16\22\7\t\2\2\17\22\7\n\2\2\20\22\7\13")
        buf.write("\2\2\21\f\3\2\2\2\21\r\3\2\2\2\21\16\3\2\2\2\21\17\3\2")
        buf.write("\2\2\21\20\3\2\2\2\22\3\3\2\2\2\23\27\t\2\2\2\24\27\t")
        buf.write("\3\2\2\25\27\t\4\2\2\26\23\3\2\2\2\26\24\3\2\2\2\26\25")
        buf.write("\3\2\2\2\27\5\3\2\2\2\30\31\7\6\2\2\31\32\7\7\2\2\32\33")
        buf.write("\7\b\2\2\33\34\5\b\5\2\34\7\3\2\2\2\35\37\7\3\2\2\36 ")
        buf.write("\5\n\6\2\37\36\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\7\4\2")
        buf.write("\2\"\t\3\2\2\2#(\7\22\2\2$%\7\5\2\2%\'\7\22\2\2&$\3\2")
        buf.write("\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\13\3\2\2\2*(\3\2")
        buf.write("\2\2\6\21\26\37(")
        return buf.getvalue()


class AlgoDSLParser ( Parser ):

    grammarFileName = "AlgoDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "','", "'visualize'", "<INVALID>", 
                     "'on'", "'next'", "'explain'", "'reset'", "'1'", "'2'", 
                     "'3'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VISUALIZE", "ALGO", "ON", "NEXT", "EXPLAIN", "RESET", 
                      "ONE", "TWO", "THREE", "SORT", "PATH", "STRUCT", "INT", 
                      "WS" ]

    RULE_command = 0
    RULE_menuSelect = 1
    RULE_visualize = 2
    RULE_array = 3
    RULE_elements = 4

    ruleNames =  [ "command", "menuSelect", "visualize", "array", "elements" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    VISUALIZE=4
    ALGO=5
    ON=6
    NEXT=7
    EXPLAIN=8
    RESET=9
    ONE=10
    TWO=11
    THREE=12
    SORT=13
    PATH=14
    STRUCT=15
    INT=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def menuSelect(self):
            return self.getTypedRuleContext(AlgoDSLParser.MenuSelectContext,0)


        def visualize(self):
            return self.getTypedRuleContext(AlgoDSLParser.VisualizeContext,0)


        def NEXT(self):
            return self.getToken(AlgoDSLParser.NEXT, 0)

        def EXPLAIN(self):
            return self.getToken(AlgoDSLParser.EXPLAIN, 0)

        def RESET(self):
            return self.getToken(AlgoDSLParser.RESET, 0)

        def getRuleIndex(self):
            return AlgoDSLParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = AlgoDSLParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AlgoDSLParser.ONE, AlgoDSLParser.TWO, AlgoDSLParser.THREE, AlgoDSLParser.SORT, AlgoDSLParser.PATH, AlgoDSLParser.STRUCT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.menuSelect()
                pass
            elif token in [AlgoDSLParser.VISUALIZE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.visualize()
                pass
            elif token in [AlgoDSLParser.NEXT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.match(AlgoDSLParser.NEXT)
                pass
            elif token in [AlgoDSLParser.EXPLAIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 13
                self.match(AlgoDSLParser.EXPLAIN)
                pass
            elif token in [AlgoDSLParser.RESET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 14
                self.match(AlgoDSLParser.RESET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MenuSelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AlgoDSLParser.RULE_menuSelect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MenuSortContext(MenuSelectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.MenuSelectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ONE(self):
            return self.getToken(AlgoDSLParser.ONE, 0)
        def SORT(self):
            return self.getToken(AlgoDSLParser.SORT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuSort" ):
                listener.enterMenuSort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuSort" ):
                listener.exitMenuSort(self)


    class MenuPathContext(MenuSelectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.MenuSelectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TWO(self):
            return self.getToken(AlgoDSLParser.TWO, 0)
        def PATH(self):
            return self.getToken(AlgoDSLParser.PATH, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuPath" ):
                listener.enterMenuPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuPath" ):
                listener.exitMenuPath(self)


    class MenuStructContext(MenuSelectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.MenuSelectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THREE(self):
            return self.getToken(AlgoDSLParser.THREE, 0)
        def STRUCT(self):
            return self.getToken(AlgoDSLParser.STRUCT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuStruct" ):
                listener.enterMenuStruct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuStruct" ):
                listener.exitMenuStruct(self)



    def menuSelect(self):

        localctx = AlgoDSLParser.MenuSelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_menuSelect)
        self._la = 0 # Token type
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AlgoDSLParser.ONE, AlgoDSLParser.SORT]:
                localctx = AlgoDSLParser.MenuSortContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                _la = self._input.LA(1)
                if not(_la==AlgoDSLParser.ONE or _la==AlgoDSLParser.SORT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [AlgoDSLParser.TWO, AlgoDSLParser.PATH]:
                localctx = AlgoDSLParser.MenuPathContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                _la = self._input.LA(1)
                if not(_la==AlgoDSLParser.TWO or _la==AlgoDSLParser.PATH):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [AlgoDSLParser.THREE, AlgoDSLParser.STRUCT]:
                localctx = AlgoDSLParser.MenuStructContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                _la = self._input.LA(1)
                if not(_la==AlgoDSLParser.THREE or _la==AlgoDSLParser.STRUCT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VISUALIZE(self):
            return self.getToken(AlgoDSLParser.VISUALIZE, 0)

        def ALGO(self):
            return self.getToken(AlgoDSLParser.ALGO, 0)

        def ON(self):
            return self.getToken(AlgoDSLParser.ON, 0)

        def array(self):
            return self.getTypedRuleContext(AlgoDSLParser.ArrayContext,0)


        def getRuleIndex(self):
            return AlgoDSLParser.RULE_visualize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualize" ):
                listener.enterVisualize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualize" ):
                listener.exitVisualize(self)




    def visualize(self):

        localctx = AlgoDSLParser.VisualizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_visualize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(AlgoDSLParser.VISUALIZE)
            self.state = 23
            self.match(AlgoDSLParser.ALGO)
            self.state = 24
            self.match(AlgoDSLParser.ON)
            self.state = 25
            self.array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(AlgoDSLParser.ElementsContext,0)


        def getRuleIndex(self):
            return AlgoDSLParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = AlgoDSLParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(AlgoDSLParser.T__0)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AlgoDSLParser.INT:
                self.state = 28
                self.elements()


            self.state = 31
            self.match(AlgoDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(AlgoDSLParser.INT)
            else:
                return self.getToken(AlgoDSLParser.INT, i)

        def getRuleIndex(self):
            return AlgoDSLParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)




    def elements(self):

        localctx = AlgoDSLParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(AlgoDSLParser.INT)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AlgoDSLParser.T__2:
                self.state = 34
                self.match(AlgoDSLParser.T__2)
                self.state = 35
                self.match(AlgoDSLParser.INT)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





