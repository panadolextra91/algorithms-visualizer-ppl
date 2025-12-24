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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\5\2\"\n\2\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5:\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6B\n\6")
        buf.write("\3\7\3\7\3\7\7\7G\n\7\f\7\16\7J\13\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\fY\n\f\3\f\3")
        buf.write("\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\2\2p\2!\3\2")
        buf.write("\2\2\4#\3\2\2\2\6+\3\2\2\2\b9\3\2\2\2\nA\3\2\2\2\fC\3")
        buf.write("\2\2\2\16K\3\2\2\2\20M\3\2\2\2\22O\3\2\2\2\24Q\3\2\2\2")
        buf.write("\26V\3\2\2\2\30\"\5\4\3\2\31\"\5\6\4\2\32\"\5\b\5\2\33")
        buf.write("\"\5\n\6\2\34\"\5\f\7\2\35\"\5\16\b\2\36\"\5\20\t\2\37")
        buf.write("\"\5\22\n\2 \"\5\24\13\2!\30\3\2\2\2!\31\3\2\2\2!\32\3")
        buf.write("\2\2\2!\33\3\2\2\2!\34\3\2\2\2!\35\3\2\2\2!\36\3\2\2\2")
        buf.write("!\37\3\2\2\2! \3\2\2\2\"\3\3\2\2\2#$\7\3\2\2$\5\3\2\2")
        buf.write("\2%,\7\4\2\2&,\7\5\2\2\',\7\6\2\2(,\7\7\2\2),\7\b\2\2")
        buf.write("*,\7\t\2\2+%\3\2\2\2+&\3\2\2\2+\'\3\2\2\2+(\3\2\2\2+)")
        buf.write("\3\2\2\2+*\3\2\2\2,\7\3\2\2\2-:\7\7\2\2.:\7\b\2\2/:\7")
        buf.write("\t\2\2\60:\7\n\2\2\61:\7\13\2\2\62:\7\f\2\2\63:\7\r\2")
        buf.write("\2\64:\7\16\2\2\65:\7\17\2\2\66:\7\20\2\2\67:\7\21\2\2")
        buf.write("8:\7\22\2\29-\3\2\2\29.\3\2\2\29/\3\2\2\29\60\3\2\2\2")
        buf.write("9\61\3\2\2\29\62\3\2\2\29\63\3\2\2\29\64\3\2\2\29\65\3")
        buf.write("\2\2\29\66\3\2\2\29\67\3\2\2\298\3\2\2\2:\t\3\2\2\2;B")
        buf.write("\7\7\2\2<B\7\b\2\2=B\7\t\2\2>B\7\23\2\2?B\7\24\2\2@B\7")
        buf.write("\25\2\2A;\3\2\2\2A<\3\2\2\2A=\3\2\2\2A>\3\2\2\2A?\3\2")
        buf.write("\2\2A@\3\2\2\2B\13\3\2\2\2CH\7\36\2\2DE\7\35\2\2EG\7\36")
        buf.write("\2\2FD\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\r\3\2\2")
        buf.write("\2JH\3\2\2\2KL\7\26\2\2L\17\3\2\2\2MN\7\27\2\2N\21\3\2")
        buf.write("\2\2OP\7\30\2\2P\23\3\2\2\2QR\7\31\2\2RS\7\r\2\2ST\7\32")
        buf.write("\2\2TU\5\26\f\2U\25\3\2\2\2VX\7\33\2\2WY\5\f\7\2XW\3\2")
        buf.write("\2\2XY\3\2\2\2YZ\3\2\2\2Z[\7\34\2\2[\27\3\2\2\2\b!+9A")
        buf.write("HX")
        return buf.getvalue()


class AlgoDSLParser ( Parser ):

    grammarFileName = "AlgoDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'menu'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'next'", "'explain'", "'reset'", "'visualize'", "'on'", 
                     "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "MENU", "SORTING_KEYWORDS", "PATHFINDING_KEYWORDS", 
                      "DATA_STRUCTURE_KEYWORDS", "NUMBER_ONE", "NUMBER_TWO", 
                      "NUMBER_THREE", "NUMBER_FOUR", "NUMBER_FIVE", "NUMBER_SIX", 
                      "BUBBLE_KEYWORDS", "MERGE_KEYWORDS", "SELECTION_KEYWORDS", 
                      "INSERTION_KEYWORDS", "QUICK_KEYWORDS", "HEAP_KEYWORDS", 
                      "STACK_DS", "QUEUE_DS", "LINKEDLIST_DS", "NEXT", "EXPLAIN", 
                      "RESET", "VISUALIZE", "ON", "LBRACKET", "RBRACKET", 
                      "COMMA", "NUMBER", "WS" ]

    RULE_command = 0
    RULE_menuCommand = 1
    RULE_menuSelection = 2
    RULE_sortingAlgorithmSelection = 3
    RULE_dataStructureSelection = 4
    RULE_arrayInput = 5
    RULE_nextCommand = 6
    RULE_explainCommand = 7
    RULE_resetCommand = 8
    RULE_visualizeCommand = 9
    RULE_arrayLiteral = 10

    ruleNames =  [ "command", "menuCommand", "menuSelection", "sortingAlgorithmSelection", 
                   "dataStructureSelection", "arrayInput", "nextCommand", 
                   "explainCommand", "resetCommand", "visualizeCommand", 
                   "arrayLiteral" ]

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
    STACK_DS=17
    QUEUE_DS=18
    LINKEDLIST_DS=19
    NEXT=20
    EXPLAIN=21
    RESET=22
    VISUALIZE=23
    ON=24
    LBRACKET=25
    RBRACKET=26
    COMMA=27
    NUMBER=28
    WS=29

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


        def dataStructureSelection(self):
            return self.getTypedRuleContext(AlgoDSLParser.DataStructureSelectionContext,0)


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
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.menuCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.menuSelection()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.sortingAlgorithmSelection()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.dataStructureSelection()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.arrayInput()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 27
                self.nextCommand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 28
                self.explainCommand()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 29
                self.resetCommand()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 30
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
            self.state = 33
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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AlgoDSLParser.SORTING_KEYWORDS]:
                localctx = AlgoDSLParser.MenuSortingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(AlgoDSLParser.SORTING_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.PATHFINDING_KEYWORDS]:
                localctx = AlgoDSLParser.MenuPathfindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(AlgoDSLParser.PATHFINDING_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.DATA_STRUCTURE_KEYWORDS]:
                localctx = AlgoDSLParser.MenuDataStructuresContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(AlgoDSLParser.DATA_STRUCTURE_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.NUMBER_ONE]:
                localctx = AlgoDSLParser.MenuSortingNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(AlgoDSLParser.NUMBER_ONE)
                pass
            elif token in [AlgoDSLParser.NUMBER_TWO]:
                localctx = AlgoDSLParser.MenuPathfindingNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.match(AlgoDSLParser.NUMBER_TWO)
                pass
            elif token in [AlgoDSLParser.NUMBER_THREE]:
                localctx = AlgoDSLParser.MenuDataStructuresNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 40
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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AlgoDSLParser.NUMBER_ONE]:
                localctx = AlgoDSLParser.SelectBubbleSortContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(AlgoDSLParser.NUMBER_ONE)
                pass
            elif token in [AlgoDSLParser.NUMBER_TWO]:
                localctx = AlgoDSLParser.SelectMergeSortContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(AlgoDSLParser.NUMBER_TWO)
                pass
            elif token in [AlgoDSLParser.NUMBER_THREE]:
                localctx = AlgoDSLParser.SelectSelectionSortContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(AlgoDSLParser.NUMBER_THREE)
                pass
            elif token in [AlgoDSLParser.NUMBER_FOUR]:
                localctx = AlgoDSLParser.SelectInsertionSortContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(AlgoDSLParser.NUMBER_FOUR)
                pass
            elif token in [AlgoDSLParser.NUMBER_FIVE]:
                localctx = AlgoDSLParser.SelectQuickSortContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.match(AlgoDSLParser.NUMBER_FIVE)
                pass
            elif token in [AlgoDSLParser.NUMBER_SIX]:
                localctx = AlgoDSLParser.SelectHeapSortContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.match(AlgoDSLParser.NUMBER_SIX)
                pass
            elif token in [AlgoDSLParser.BUBBLE_KEYWORDS]:
                localctx = AlgoDSLParser.SelectBubbleSortContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.match(AlgoDSLParser.BUBBLE_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.MERGE_KEYWORDS]:
                localctx = AlgoDSLParser.SelectMergeSortContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 50
                self.match(AlgoDSLParser.MERGE_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.SELECTION_KEYWORDS]:
                localctx = AlgoDSLParser.SelectSelectionSortContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 51
                self.match(AlgoDSLParser.SELECTION_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.INSERTION_KEYWORDS]:
                localctx = AlgoDSLParser.SelectInsertionSortContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 52
                self.match(AlgoDSLParser.INSERTION_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.QUICK_KEYWORDS]:
                localctx = AlgoDSLParser.SelectQuickSortContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 53
                self.match(AlgoDSLParser.QUICK_KEYWORDS)
                pass
            elif token in [AlgoDSLParser.HEAP_KEYWORDS]:
                localctx = AlgoDSLParser.SelectHeapSortContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 54
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


    class DataStructureSelectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AlgoDSLParser.RULE_dataStructureSelection

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SelectStackContext(DataStructureSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.DataStructureSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_ONE(self):
            return self.getToken(AlgoDSLParser.NUMBER_ONE, 0)
        def STACK_DS(self):
            return self.getToken(AlgoDSLParser.STACK_DS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStack" ):
                listener.enterSelectStack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStack" ):
                listener.exitSelectStack(self)


    class SelectQueueContext(DataStructureSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.DataStructureSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_TWO(self):
            return self.getToken(AlgoDSLParser.NUMBER_TWO, 0)
        def QUEUE_DS(self):
            return self.getToken(AlgoDSLParser.QUEUE_DS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectQueue" ):
                listener.enterSelectQueue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectQueue" ):
                listener.exitSelectQueue(self)


    class SelectLinkedListContext(DataStructureSelectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoDSLParser.DataStructureSelectionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER_THREE(self):
            return self.getToken(AlgoDSLParser.NUMBER_THREE, 0)
        def LINKEDLIST_DS(self):
            return self.getToken(AlgoDSLParser.LINKEDLIST_DS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectLinkedList" ):
                listener.enterSelectLinkedList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectLinkedList" ):
                listener.exitSelectLinkedList(self)



    def dataStructureSelection(self):

        localctx = AlgoDSLParser.DataStructureSelectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dataStructureSelection)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AlgoDSLParser.NUMBER_ONE]:
                localctx = AlgoDSLParser.SelectStackContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(AlgoDSLParser.NUMBER_ONE)
                pass
            elif token in [AlgoDSLParser.NUMBER_TWO]:
                localctx = AlgoDSLParser.SelectQueueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(AlgoDSLParser.NUMBER_TWO)
                pass
            elif token in [AlgoDSLParser.NUMBER_THREE]:
                localctx = AlgoDSLParser.SelectLinkedListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(AlgoDSLParser.NUMBER_THREE)
                pass
            elif token in [AlgoDSLParser.STACK_DS]:
                localctx = AlgoDSLParser.SelectStackContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.match(AlgoDSLParser.STACK_DS)
                pass
            elif token in [AlgoDSLParser.QUEUE_DS]:
                localctx = AlgoDSLParser.SelectQueueContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.match(AlgoDSLParser.QUEUE_DS)
                pass
            elif token in [AlgoDSLParser.LINKEDLIST_DS]:
                localctx = AlgoDSLParser.SelectLinkedListContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 62
                self.match(AlgoDSLParser.LINKEDLIST_DS)
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
        self.enterRule(localctx, 10, self.RULE_arrayInput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(AlgoDSLParser.NUMBER)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AlgoDSLParser.COMMA:
                self.state = 66
                self.match(AlgoDSLParser.COMMA)
                self.state = 67
                self.match(AlgoDSLParser.NUMBER)
                self.state = 72
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
        self.enterRule(localctx, 12, self.RULE_nextCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
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
        self.enterRule(localctx, 14, self.RULE_explainCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
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
        self.enterRule(localctx, 16, self.RULE_resetCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
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
        self.enterRule(localctx, 18, self.RULE_visualizeCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(AlgoDSLParser.VISUALIZE)
            self.state = 80
            self.match(AlgoDSLParser.BUBBLE_KEYWORDS)
            self.state = 81
            self.match(AlgoDSLParser.ON)
            self.state = 82
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
        self.enterRule(localctx, 20, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(AlgoDSLParser.LBRACKET)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AlgoDSLParser.NUMBER:
                self.state = 85
                self.arrayInput()


            self.state = 88
            self.match(AlgoDSLParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





