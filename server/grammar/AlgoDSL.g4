grammar AlgoDSL;

// Main command entry point
command
    : menuCommand
    | menuSelection
    | sortingAlgorithmSelection
    | arrayInput
    | nextCommand
    | explainCommand
    | resetCommand
    | visualizeCommand
    ;

// Menu command - returns to main menu
menuCommand
    : MENU
    ;

// Menu selections - top level categories
menuSelection
    : SORTING_KEYWORDS    #MenuSorting
    | PATHFINDING_KEYWORDS #MenuPathfinding
    | DATA_STRUCTURE_KEYWORDS #MenuDataStructures
    | NUMBER_ONE          #MenuSortingNumber
    | NUMBER_TWO          #MenuPathfindingNumber
    | NUMBER_THREE        #MenuDataStructuresNumber
    ;

// Sorting algorithm selection (numbers or names)
sortingAlgorithmSelection
    : NUMBER_ONE          #SelectBubbleSort
    | NUMBER_TWO          #SelectMergeSort
    | NUMBER_THREE        #SelectSelectionSort
    | NUMBER_FOUR         #SelectInsertionSort
    | NUMBER_FIVE         #SelectQuickSort
    | NUMBER_SIX          #SelectHeapSort
    | BUBBLE_KEYWORDS     #SelectBubbleSort
    | MERGE_KEYWORDS      #SelectMergeSort
    | SELECTION_KEYWORDS  #SelectSelectionSort
    | INSERTION_KEYWORDS  #SelectInsertionSort
    | QUICK_KEYWORDS      #SelectQuickSort
    | HEAP_KEYWORDS       #SelectHeapSort
    ;

// Array input - comma-separated numbers
arrayInput
    : NUMBER (COMMA NUMBER)*
    ;

// Next step command
nextCommand
    : NEXT
    ;

// Explain command
explainCommand
    : EXPLAIN
    ;

// Reset command
resetCommand
    : RESET
    ;

// Legacy visualize command (for backward compatibility)
visualizeCommand
    : VISUALIZE BUBBLE_KEYWORDS ON arrayLiteral
    ;

arrayLiteral
    : LBRACKET arrayInput? RBRACKET
    ;

// Tokens

// Menu command
MENU: 'menu';

// Menu selection keywords
SORTING_KEYWORDS: 'sorting algorithms' | 'sorting algorithm' | 'sort algorithms' | 'sort algorithm' | 'sorting' | 'sort';
PATHFINDING_KEYWORDS: 'pathfinding algorithms' | 'pathfinding algorithm' | 'path algorithms' | 'path algorithm' | 'pathfinding' | 'path';
DATA_STRUCTURE_KEYWORDS: 'data structures' | 'data structure' | 'structures' | 'structure' | 'data';

// Numbers for menu and algorithm selection
NUMBER_ONE: '1';
NUMBER_TWO: '2';
NUMBER_THREE: '3';
NUMBER_FOUR: '4';
NUMBER_FIVE: '5';
NUMBER_SIX: '6';

// Sorting algorithm keywords
BUBBLE_KEYWORDS: 'bubble sort' | 'bubblesort' | 'bubble';
MERGE_KEYWORDS: 'merge sort' | 'mergesort' | 'merge';
SELECTION_KEYWORDS: 'selection sort' | 'selectionsort' | 'selection';
INSERTION_KEYWORDS: 'insertion sort' | 'insertionsort' | 'insertion';
QUICK_KEYWORDS: 'quick sort' | 'quicksort' | 'quick';
HEAP_KEYWORDS: 'heap sort' | 'heapsort' | 'heap';

// Action commands
NEXT: 'next';
EXPLAIN: 'explain';
RESET: 'reset';

// Legacy visualize command tokens
VISUALIZE: 'visualize';
ON: 'on';

// Array literal tokens
LBRACKET: '[';
RBRACKET: ']';
COMMA: ',';

// Number token (must come after specific number tokens)
NUMBER: '-'? [0-9]+;

// Whitespace - skip
WS: [ \t\r\n]+ -> skip;