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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\5\2\37\n\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4)\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\67\n\5\3\6\3\6\3\6\7\6<\n\6\f\6\16\6?\13\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\5\13")
        buf.write("N\n\13\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2")
        buf.write("\2\2`\2\36\3\2\2\2\4 \3\2\2\2\6(\3\2\2\2\b\66\3\2\2\2")
        buf.write("\n8\3\2\2\2\f@\3\2\2\2\16B\3\2\2\2\20D\3\2\2\2\22F\3\2")
        buf.write("\2\2\24K\3\2\2\2\26\37\5\4\3\2\27\37\5\6\4\2\30\37\5\b")
        buf.write("\5\2\31\37\5\n\6\2\32\37\5\f\7\2\33\37\5\16\b\2\34\37")
        buf.write("\5\20\t\2\35\37\5\22\n\2\36\26\3\2\2\2\36\27\3\2\2\2\36")
        buf.write("\30\3\2\2\2\36\31\3\2\2\2\36\32\3\2\2\2\36\33\3\2\2\2")
        buf.write("\36\34\3\2\2\2\36\35\3\2\2\2\37\3\3\2\2\2 !\7\3\2\2!\5")
        buf.write("\3\2\2\2\")\7\4\2\2#)\7\5\2\2$)\7\6\2\2%)\7\7\2\2&)\7")
        buf.write("\b\2\2\')\7\t\2\2(\"\3\2\2\2(#\3\2\2\2($\3\2\2\2(%\3\2")
        buf.write("\2\2(&\3\2\2\2(\'\3\2\2\2)\7\3\2\2\2*\67\7\7\2\2+\67\7")
        buf.write("\b\2\2,\67\7\t\2\2-\67\7\n\2\2.\67\7\13\2\2/\67\7\f\2")
        buf.write("\2\60\67\7\r\2\2\61\67\7\16\2\2\62\67\7\17\2\2\63\67\7")
        buf.write("\20\2\2\64\67\7\21\2\2\65\67\7\22\2\2\66*\3\2\2\2\66+")
        buf.write("\3\2\2\2\66,\3\2\2\2\66-\3\2\2\2\66.\3\2\2\2\66/\3\2\2")
        buf.write("\2\66\60\3\2\2\2\66\61\3\2\2\2\66\62\3\2\2\2\66\63\3\2")
        buf.write("\2\2\66\64\3\2\2\2\66\65\3\2\2\2\67\t\3\2\2\28=\7\33\2")
        buf.write("\29:\7\32\2\2:<\7\33\2\2;9\3\2\2\2<?\3\2\2\2=;\3\2\2\2")
        buf.write("=>\3\2\2\2>\13\3\2\2\2?=\3\2\2\2@A\7\23\2\2A\r\3\2\2\2")
        buf.write("BC\7\24\2\2C\17\3\2\2\2DE\7\25\2\2E\21\3\2\2\2FG\7\26")
        buf.write("\2\2GH\7\r\2\2HI\7\27\2\2IJ\5\24\13\2J\23\3\2\2\2KM\7")
        buf.write("\30\2\2LN\5\n\6\2ML\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\31")
        buf.write("\2\2P\25\3\2\2\2\7\36(\66=M")
        return buf.getvalue()


class AlgoDSLParser ( Parser ):

    grammarFileName = "AlgoDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'menu'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'next'", "'explain'", "'reset'", "'visualize'", 
                     "'on'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "MENU", "SORTING_KEYWORDS", "PATHFINDING_KEYWORDS", 
                      "DATA_STRUCTURE_KEYWORDS", "NUMBER_ONE", "NUMBER_TWO", 
                      "NUMBER_THREE", "NUMBER_FOUR", "NUMBER_FIVE", "NUMBER_SIX", 
                      "BUBBLE_KEYWORDS", "MERGE_KEYWORDS", "SELECTION_KEYWORDS", 
                      "INSERTION_KEYWORDS", "QUICK_KEYWORDS", "HEAP_KEYWORDS", 
                      "NEXT", "EXPLAIN", "RESET", "VISUALIZE", "ON", "LBRACKET", 
                      "RBRACKET", "COMMA", "NUMBER", "WS" ]

    RULE_command = 0
    RULE_menuCommand = 1
    RULE_menuSelection = 2
    RULE_sortingAlgorithmSelection = 3
    RULE_arrayInput = 4
    RULE_nextCommand = 5
    RULE_explainCommand = 6
    RULE_resetCommand = 7
    RULE_visualizeCommand = 8
    RULE_arrayLiteral = 9

    ruleNames =  [ "command", "menuCommand", "menuSelection", "sortingAlgorithmSelection", 
                   "arrayInput", "nextCommand", "explainCommand", "resetCommand", 
                   "visualizeCommand", "arrayLiteral" ]

    EOF = Token.EOF
    MENU=1
    SORTING_KEYWORDS=2
    PATHFINDING_KEYWORDS=3
    DATA_STRUCTURE_KEYWORDS=4
    NUMBER_ONE=5
    NUMBER_TWO=6
    NUMBER_THREE=7
    NUMBER_FOUR=8
    NUMBER_FIVE=9
    NUMBER_SIX=10
    BUBBLE_KEYWORDS=11
    MERGE_KEYWORDS=12
    SELECTION_KEYWORDS=13
    INSERTION_KEYWORDS=14
    QUICK_KEYWORDS=15
    HEAP_KEYWORDS=16
    NEXT=17
    EXPLAIN=18
    RESET=19
    VISUALIZE=20
    ON=21
    LBRACKET=22
    RBRACKET=23
    COMMA=24
    NUMBER=25
    WS=26

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

        def menuCommand(self):
            return self.getTypedRuleContext(AlgoDSLParser.MenuCommandContext,0)


        def menuSelection(self):
            return self.getTypedRuleContext(AlgoDSLParser.MenuSelectionContext,0)


        def sortingAlgorithmSelection(self):
            return self.getTypedRuleContext(AlgoDSLParser.SortingAlgorithmSelectionContext,0)


        def arrayInput(self):
            return self.getTypedRuleContext(AlgoDSLParser.ArrayInputContext,0)


        def nextCommand(self):
            return self.getTypedRuleContext(AlgoDSLParser.NextCommandContext,0)


        def explainCommand(self):
            return self.getTypedRuleContext(AlgoDSLParser.ExplainCommandContext,0)


        def resetCommand(self):
            return self.getTypedRuleContext(AlgoDSLParser.ResetCommandContext,0)


        def visualizeCommand(self):
            return self.getTypedRuleContext(AlgoDSLParser.VisualizeCommandContext,0)


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
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.menuCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.menuSelection()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.sortingAlgorithmSelection()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.arrayInput()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 24
                self.nextCommand()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 25
                self.explainCommand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 26
                self.resetCommand()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 27
                self.visualizeCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MenuCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENU(self):
            return self.getToken(AlgoDSLParser.MENU, 0)

        def getRuleIndex(self):
            return AlgoDSLParser.RULE_menuCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuCommand" ):
                listener.enterMenuCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuCommand" ):
                listener.exitMenuCommand(self)




    def menuCommand(self):

        localctx = AlgoDSLParser.MenuCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_menuCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(AlgoDSLParser.MENU)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MenuSelectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AlgoDSLParser.RULE_menuSelection

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MenuSortingNumberContext(MenuSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.MenuSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_ONE(self):
            return self.getToken(AlgoDSLParser.NUMBER_ONE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuSortingNumber" ):
                listener.enterMenuSortingNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuSortingNumber" ):
                listener.exitMenuSortingNumber(self)


    class MenuDataStructuresContext(MenuSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.MenuSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DATA_STRUCTURE_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.DATA_STRUCTURE_KEYWORDS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuDataStructures" ):
                listener.enterMenuDataStructures(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuDataStructures" ):
                listener.exitMenuDataStructures(self)


    class MenuSortingContext(MenuSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.MenuSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SORTING_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.SORTING_KEYWORDS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuSorting" ):
                listener.enterMenuSorting(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuSorting" ):
                listener.exitMenuSorting(self)


    class MenuDataStructuresNumberContext(MenuSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.MenuSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_THREE(self):
            return self.getToken(AlgoDSLParser.NUMBER_THREE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuDataStructuresNumber" ):
                listener.enterMenuDataStructuresNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuDataStructuresNumber" ):
                listener.exitMenuDataStructuresNumber(self)


    class MenuPathfindingNumberContext(MenuSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.MenuSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_TWO(self):
            return self.getToken(AlgoDSLParser.NUMBER_TWO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuPathfindingNumber" ):
                listener.enterMenuPathfindingNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuPathfindingNumber" ):
                listener.exitMenuPathfindingNumber(self)


    class MenuPathfindingContext(MenuSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.MenuSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PATHFINDING_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.PATHFINDING_KEYWORDS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenuPathfinding" ):
                listener.enterMenuPathfinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenuPathfinding" ):
                listener.exitMenuPathfinding(self)



    def menuSelection(self):

        localctx = AlgoDSLParser.MenuSelectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_menuSelection)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AlgoDSLParser.SORTING_KEYWORDS]:
                localctx = AlgoDSLParser.MenuSortingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(AlgoDSLParser.SORTING_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.PATHFINDING_KEYWORDS]:
                localctx = AlgoDSLParser.MenuPathfindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(AlgoDSLParser.PATHFINDING_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.DATA_STRUCTURE_KEYWORDS]:
                localctx = AlgoDSLParser.MenuDataStructuresContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(AlgoDSLParser.DATA_STRUCTURE_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.NUMBER_ONE]:
                localctx = AlgoDSLParser.MenuSortingNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(AlgoDSLParser.NUMBER_ONE)
                pass
            elif token in [AlgoDSLParser.NUMBER_TWO]:
                localctx = AlgoDSLParser.MenuPathfindingNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.match(AlgoDSLParser.NUMBER_TWO)
                pass
            elif token in [AlgoDSLParser.NUMBER_THREE]:
                localctx = AlgoDSLParser.MenuDataStructuresNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 37
                self.match(AlgoDSLParser.NUMBER_THREE)
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


    class SortingAlgorithmSelectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AlgoDSLParser.RULE_sortingAlgorithmSelection

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SelectSelectionSortContext(SortingAlgorithmSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.SortingAlgorithmSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_THREE(self):
            return self.getToken(AlgoDSLParser.NUMBER_THREE, 0)
        def SELECTION_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.SELECTION_KEYWORDS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectSelectionSort" ):
                listener.enterSelectSelectionSort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectSelectionSort" ):
                listener.exitSelectSelectionSort(self)


    class SelectInsertionSortContext(SortingAlgorithmSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.SortingAlgorithmSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_FOUR(self):
            return self.getToken(AlgoDSLParser.NUMBER_FOUR, 0)
        def INSERTION_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.INSERTION_KEYWORDS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectInsertionSort" ):
                listener.enterSelectInsertionSort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectInsertionSort" ):
                listener.exitSelectInsertionSort(self)


    class SelectBubbleSortContext(SortingAlgorithmSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.SortingAlgorithmSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_ONE(self):
            return self.getToken(AlgoDSLParser.NUMBER_ONE, 0)
        def BUBBLE_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.BUBBLE_KEYWORDS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectBubbleSort" ):
                listener.enterSelectBubbleSort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectBubbleSort" ):
                listener.exitSelectBubbleSort(self)


    class SelectHeapSortContext(SortingAlgorithmSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.SortingAlgorithmSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_SIX(self):
            return self.getToken(AlgoDSLParser.NUMBER_SIX, 0)
        def HEAP_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.HEAP_KEYWORDS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectHeapSort" ):
                listener.enterSelectHeapSort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectHeapSort" ):
                listener.exitSelectHeapSort(self)


    class SelectQuickSortContext(SortingAlgorithmSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.SortingAlgorithmSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_FIVE(self):
            return self.getToken(AlgoDSLParser.NUMBER_FIVE, 0)
        def QUICK_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.QUICK_KEYWORDS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectQuickSort" ):
                listener.enterSelectQuickSort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectQuickSort" ):
                listener.exitSelectQuickSort(self)


    class SelectMergeSortContext(SortingAlgorithmSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.SortingAlgorithmSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_TWO(self):
            return self.getToken(AlgoDSLParser.NUMBER_TWO, 0)
        def MERGE_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.MERGE_KEYWORDS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectMergeSort" ):
                listener.enterSelectMergeSort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectMergeSort" ):
                listener.exitSelectMergeSort(self)



    def sortingAlgorithmSelection(self):

        localctx = AlgoDSLParser.SortingAlgorithmSelectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sortingAlgorithmSelection)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AlgoDSLParser.NUMBER_ONE]:
                localctx = AlgoDSLParser.SelectBubbleSortContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(AlgoDSLParser.NUMBER_ONE)
                pass
            elif token in [AlgoDSLParser.NUMBER_TWO]:
                localctx = AlgoDSLParser.SelectMergeSortContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(AlgoDSLParser.NUMBER_TWO)
                pass
            elif token in [AlgoDSLParser.NUMBER_THREE]:
                localctx = AlgoDSLParser.SelectSelectionSortContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(AlgoDSLParser.NUMBER_THREE)
                pass
            elif token in [AlgoDSLParser.NUMBER_FOUR]:
                localctx = AlgoDSLParser.SelectInsertionSortContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.match(AlgoDSLParser.NUMBER_FOUR)
                pass
            elif token in [AlgoDSLParser.NUMBER_FIVE]:
                localctx = AlgoDSLParser.SelectQuickSortContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.match(AlgoDSLParser.NUMBER_FIVE)
                pass
            elif token in [AlgoDSLParser.NUMBER_SIX]:
                localctx = AlgoDSLParser.SelectHeapSortContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.match(AlgoDSLParser.NUMBER_SIX)
                pass
            elif token in [AlgoDSLParser.BUBBLE_KEYWORDS]:
                localctx = AlgoDSLParser.SelectBubbleSortContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.match(AlgoDSLParser.BUBBLE_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.MERGE_KEYWORDS]:
                localctx = AlgoDSLParser.SelectMergeSortContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 47
                self.match(AlgoDSLParser.MERGE_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.SELECTION_KEYWORDS]:
                localctx = AlgoDSLParser.SelectSelectionSortContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 48
                self.match(AlgoDSLParser.SELECTION_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.INSERTION_KEYWORDS]:
                localctx = AlgoDSLParser.SelectInsertionSortContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 49
                self.match(AlgoDSLParser.INSERTION_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.QUICK_KEYWORDS]:
                localctx = AlgoDSLParser.SelectQuickSortContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 50
                self.match(AlgoDSLParser.QUICK_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.HEAP_KEYWORDS]:
                localctx = AlgoDSLParser.SelectHeapSortContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 51
                self.match(AlgoDSLParser.HEAP_KEYWORDS)
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


    class ArrayInputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(AlgoDSLParser.NUMBER)
            else:
                return self.getToken(AlgoDSLParser.NUMBER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AlgoDSLParser.COMMA)
            else:
                return self.getToken(AlgoDSLParser.COMMA, i)

        def getRuleIndex(self):
            return AlgoDSLParser.RULE_arrayInput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayInput" ):
                listener.enterArrayInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayInput" ):
                listener.exitArrayInput(self)




    def arrayInput(self):

        localctx = AlgoDSLParser.ArrayInputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayInput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(AlgoDSLParser.NUMBER)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AlgoDSLParser.COMMA:
                self.state = 55
                self.match(AlgoDSLParser.COMMA)
                self.state = 56
                self.match(AlgoDSLParser.NUMBER)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NextCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEXT(self):
            return self.getToken(AlgoDSLParser.NEXT, 0)

        def getRuleIndex(self):
            return AlgoDSLParser.RULE_nextCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNextCommand" ):
                listener.enterNextCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNextCommand" ):
                listener.exitNextCommand(self)




    def nextCommand(self):

        localctx = AlgoDSLParser.NextCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_nextCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(AlgoDSLParser.NEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplainCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPLAIN(self):
            return self.getToken(AlgoDSLParser.EXPLAIN, 0)

        def getRuleIndex(self):
            return AlgoDSLParser.RULE_explainCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplainCommand" ):
                listener.enterExplainCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplainCommand" ):
                listener.exitExplainCommand(self)




    def explainCommand(self):

        localctx = AlgoDSLParser.ExplainCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_explainCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(AlgoDSLParser.EXPLAIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResetCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RESET(self):
            return self.getToken(AlgoDSLParser.RESET, 0)

        def getRuleIndex(self):
            return AlgoDSLParser.RULE_resetCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResetCommand" ):
                listener.enterResetCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResetCommand" ):
                listener.exitResetCommand(self)




    def resetCommand(self):

        localctx = AlgoDSLParser.ResetCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_resetCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(AlgoDSLParser.RESET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VISUALIZE(self):
            return self.getToken(AlgoDSLParser.VISUALIZE, 0)

        def BUBBLE_KEYWORDS(self):
            return self.getToken(AlgoDSLParser.BUBBLE_KEYWORDS, 0)

        def ON(self):
            return self.getToken(AlgoDSLParser.ON, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(AlgoDSLParser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return AlgoDSLParser.RULE_visualizeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualizeCommand" ):
                listener.enterVisualizeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualizeCommand" ):
                listener.exitVisualizeCommand(self)




    def visualizeCommand(self):

        localctx = AlgoDSLParser.VisualizeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_visualizeCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(AlgoDSLParser.VISUALIZE)
            self.state = 69
            self.match(AlgoDSLParser.BUBBLE_KEYWORDS)
            self.state = 70
            self.match(AlgoDSLParser.ON)
            self.state = 71
            self.arrayLiteral()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(AlgoDSLParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(AlgoDSLParser.RBRACKET, 0)

        def arrayInput(self):
            return self.getTypedRuleContext(AlgoDSLParser.ArrayInputContext,0)


        def getRuleIndex(self):
            return AlgoDSLParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)




    def arrayLiteral(self):

        localctx = AlgoDSLParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(AlgoDSLParser.LBRACKET)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AlgoDSLParser.NUMBER:
                self.state = 74
                self.arrayInput()


            self.state = 77
            self.match(AlgoDSLParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





