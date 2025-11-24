# Generated from grammar/AlgoDSL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AlgoDSLParser import AlgoDSLParser
else:
    from AlgoDSLParser import AlgoDSLParser

# This class defines a complete listener for a parse tree produced by AlgoDSLParser.
class AlgoDSLListener(ParseTreeListener):

    # Enter a parse tree produced by AlgoDSLParser#command.
    def enterCommand(self, ctx:AlgoDSLParser.CommandContext):
        pass

    # Exit a parse tree produced by AlgoDSLParser#command.
    def exitCommand(self, ctx:AlgoDSLParser.CommandContext):
        pass


    # Enter a parse tree produced by AlgoDSLParser#MenuSort.
    def enterMenuSort(self, ctx:AlgoDSLParser.MenuSortContext):
        pass

    # Exit a parse tree produced by AlgoDSLParser#MenuSort.
    def exitMenuSort(self, ctx:AlgoDSLParser.MenuSortContext):
        pass


    # Enter a parse tree produced by AlgoDSLParser#MenuPath.
    def enterMenuPath(self, ctx:AlgoDSLParser.MenuPathContext):
        pass

    # Exit a parse tree produced by AlgoDSLParser#MenuPath.
    def exitMenuPath(self, ctx:AlgoDSLParser.MenuPathContext):
        pass


    # Enter a parse tree produced by AlgoDSLParser#MenuStruct.
    def enterMenuStruct(self, ctx:AlgoDSLParser.MenuStructContext):
        pass

    # Exit a parse tree produced by AlgoDSLParser#MenuStruct.
    def exitMenuStruct(self, ctx:AlgoDSLParser.MenuStructContext):
        pass


    # Enter a parse tree produced by AlgoDSLParser#visualize.
    def enterVisualize(self, ctx:AlgoDSLParser.VisualizeContext):
        pass

    # Exit a parse tree produced by AlgoDSLParser#visualize.
    def exitVisualize(self, ctx:AlgoDSLParser.VisualizeContext):
        pass


    # Enter a parse tree produced by AlgoDSLParser#array.
    def enterArray(self, ctx:AlgoDSLParser.ArrayContext):
        pass

    # Exit a parse tree produced by AlgoDSLParser#array.
    def exitArray(self, ctx:AlgoDSLParser.ArrayContext):
        pass


    # Enter a parse tree produced by AlgoDSLParser#elements.
    def enterElements(self, ctx:AlgoDSLParser.ElementsContext):
        pass

    # Exit a parse tree produced by AlgoDSLParser#elements.
    def exitElements(self, ctx:AlgoDSLParser.ElementsContext):
        pass



del AlgoDSLParser