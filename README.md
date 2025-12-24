# Algorithms Visualizer Server

A Python FastAPI server that interprets a custom Domain-Specific Language (DSL) for algorithm visualization. The server parses user commands, manages algorithm state, generates visualization steps, and provides explanations for sorting algorithms, pathfinding algorithms, and data structures.

## Problem Statement

Learning algorithms and data structures can be challenging due to their abstract nature. Traditional learning methods rely on static diagrams or code, making it difficult to understand how algorithms work step-by-step. This server addresses this problem by:

1. **Providing an interactive, step-by-step visualization system** that breaks down complex algorithms into digestible steps
2. **Offering a natural language-like DSL** that allows users to interact with algorithms without writing code
3. **Maintaining algorithm state across multiple steps** to enable forward and backward navigation
4. **Supporting multiple algorithm categories** (sorting, pathfinding, data structures) through a unified interface
5. **Generating structured visualization data** that can be rendered by client applications

## Framework Description

### Technology Stack

- **FastAPI**: Modern Python web framework for building REST APIs
- **ANTLR4**: Parser generator for creating the DSL grammar and parser
- **Python 3.8+**: Core programming language
- **Pydantic**: Data validation using Python type annotations

### Architecture

The server follows a **session-based, stateful architecture**:

```
┌─────────────┐
│   Client    │
│  (React     │
│   Native)   │
└──────┬──────┘
       │ HTTP POST /command
       │ {sessionId, command}
       ▼
┌─────────────────────────────────┐
│      FastAPI Server             │
│  ┌───────────────────────────┐  │
│  │  AlgorithmSessionManager  │  │
│  │  - Manages sessions       │  │
│  │  - Routes commands        │  │
│  └───────────┬──────────────┘  │
│              │                   │
│  ┌───────────▼──────────────┐  │
│  │   DSL Interpreter         │  │
│  │  - Pattern matching       │  │
│  │  - State management       │  │
│  │  - Algorithm execution    │  │
│  └───────────┬──────────────┘  │
│              │                   │
│  ┌───────────▼──────────────┐  │
│  │  Algorithm Builders       │  │
│  │  - Generate steps         │  │
│  │  - Track state            │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
       │
       │ JSON Response
       │ {type, data, explanation}
       ▼
┌─────────────┐
│   Client    │
└─────────────┘
```

### Key Components

1. **AlgorithmSessionManager**: Manages user sessions and routes commands to the interpreter
2. **DSL Interpreter**: Parses user commands using pattern matching and keyword recognition
3. **Algorithm Builders**: Generate step-by-step visualization data for each algorithm
4. **AlgorithmRunner**: Maintains current step index and provides step navigation
5. **Session State**: Tracks current algorithm, stage (menu/awaiting input/visualizing), and pending selections

## Request Table

### Request Format (User Input)

All requests are sent via HTTP POST to `/command`:

```json
{
  "sessionId": "string",
  "command": "string"
}
```

**Parameters:**
- `sessionId`: Unique identifier for the user session (e.g., "user12345")
- `command`: Natural language command or DSL instruction

### Expected Return (Output)

The server returns JSON responses with the following structure:

#### 1. Menu Response
```json
{
  "status": "success",
  "type": "menu",
  "message": "Hi, what are you going to explore today?\n\n1. Sorting algorithms\n2. Pathfinding algorithms\n3. Data structures",
  "options": [
    {"id": "1", "label": "Sorting Algorithms"},
    {"id": "2", "label": "Pathfinding Algorithms"},
    {"id": "3", "label": "Data Structures"}
  ]
}
```

#### 2. Algorithm Menu Response
```json
{
  "status": "success",
  "type": "sorting_menu",
  "message": "Sorting Algorithms:\n1. Bubble Sort\n2. Merge Sort\n...",
  "options": [
    {"id": "1", "label": "Bubble Sort"},
    {"id": "2", "label": "Merge Sort"},
    ...
  ]
}
```

#### 3. Awaiting Input Response
```json
{
  "status": "success",
  "type": "await_array",
  "algorithm": "Bubble Sort",
  "message": "Enter the array for Bubble Sort as comma-separated integers. Example: 5, 2, 9, 1."
}
```

#### 4. Visualization Step Response
```json
{
  "status": "success",
  "type": "visualization_step",
  "algorithm": "Bubble Sort",
  "step": 1,
  "isFinal": false,
  "data": {
    "array": [2, 5, 8, 1, 9],
    "highlighted_indices": [0, 1],
    "sorted_indices": []
  },
  "explanation": "Comparing elements at index 0 (5) and index 1 (2). Since 5 > 2, they are swapped."
}
```

#### 5. Data Structure Step Response
```json
{
  "status": "success",
  "type": "data_structure_step",
  "data_structure": "Stack (LIFO)",
  "step": 2,
  "isFinal": false,
  "data": {
    "type": "stack",
    "values": [1, 2, 3, 99],
    "top_index": 3,
    "operation": "push",
    "pushed_value": 99
  },
  "explanation": "Pushed 99 onto the stack. Stack now: [1, 2, 3, 99]"
}
```

#### 6. Pathfinding Grid Response
```json
{
  "status": "success",
  "type": "await_grid",
  "algorithm": "Dijkstra's Algorithm",
  "grid_size": {"rows": 10, "cols": 10},
  "message": "Configure the grid for Dijkstra's Algorithm..."
}
```

#### 7. Pathfinding Visualization Step
```json
{
  "status": "success",
  "type": "visualization_step",
  "algorithm": "Dijkstra's Algorithm",
  "step": 5,
  "isFinal": false,
  "data": {
    "grid": {
      "start": [0, 0],
      "end": [9, 9],
      "barriers": [[2, 3], [2, 4]],
      "grid_size": {"rows": 10, "cols": 10},
      "visited": [[0, 0], [0, 1], [1, 0]],
      "path": [],
      "frontier": [[1, 1], [0, 2]]
    }
  },
  "explanation": "Exploring neighbors of (0, 0)."
}
```

#### 8. Explanation Response
```json
{
  "status": "success",
  "type": "explanation",
  "algorithm": "Bubble Sort",
  "explanation": "THEORY:\nBubble Sort works by repeatedly stepping through the list...\n\nHOW IT WORKS:\n1. Start from the first element...\n\nSTATISTICS:\n• Time Complexity: Best O(n), Average O(n²), Worst O(n²)\n..."
}
```

#### 9. Error Response
```json
{
  "status": "error",
  "message": "Unknown command or invalid syntax. Type 'menu' to restart."
}
```

### Operations Included (Backend Logic)

#### Command Types and Operations

| Command | Operation | Backend Logic |
|---------|-----------|---------------|
| `menu` | Reset session and show main menu | Clears algorithm state, resets stage to "menu", returns main menu payload |
| `1`, `2`, `3` | Select category from main menu | Sets stage to corresponding menu (sorting_menu, pathfinding_menu, data_structure_menu) |
| `sorting`, `pathfinding`, `data structures` | Select category by keyword | Same as number selection, uses keyword matching |
| `bubble sort`, `1` (in sorting menu) | Select algorithm | Sets pending_algorithm, changes stage to "await_array" or "await_grid" |
| `[5, 2, 8]` or `5, 2, 8` | Provide input array | Parses array, calls algorithm builder, creates AlgorithmRunner, returns first step |
| `next` | Advance to next step | Increments AlgorithmRunner index, returns next step or repeats last if at end |
| `explain [algorithm]` | Get algorithm explanation | Searches explanation dictionary, returns formatted explanation |
| `reset` | Reset current session | Clears all session state, returns to idle |

#### Algorithm Builders

Each algorithm has a builder function that:

1. **Takes input data** (array for sorting, grid config for pathfinding, array for data structures)
2. **Generates step-by-step visualization data**:
   - For sorting: array state, highlighted indices, sorted indices, explanation
   - For pathfinding: grid state, visited nodes, path, frontier, explanation
   - For data structures: structure state, operation type, explanation
3. **Returns list of step dictionaries** that can be navigated forward/backward

#### State Management

- **Session State**: Each session maintains:
  - `algorithm`: Currently active algorithm name
  - `state`: AlgorithmRunner instance with steps and current index
  - `stage`: Current interaction stage ("menu", "sorting_menu", "await_array", "await_grid", "visualizing")
  - `pending_algorithm`: Algorithm selected but awaiting input

- **AlgorithmRunner**: Maintains:
  - `algorithm`: Algorithm name
  - `steps`: List of all visualization steps
  - `index`: Current step index (0-based)

## System Workflow

See [workflow-diagram.md](./workflow-diagram.md) for a detailed flowchart.

### High-Level Workflow

```
1. Client sends command → FastAPI receives POST /command
2. AlgorithmSessionManager gets/creates session
3. DSL Interpreter processes command:
   a. Pattern matching (regex/keywords)
   b. Stage-based routing
   c. Command execution
4. Response generation:
   - Menu responses
   - Input prompts
   - Visualization steps
   - Explanations
5. JSON response sent to client
```

### Command Processing Flow

```
User Input
    │
    ▼
[Command Received]
    │
    ▼
[Session Lookup/Creation]
    │
    ▼
[Command Parsing]
    │
    ├─→ menu → [Reset Session] → [Return Main Menu]
    │
    ├─→ category selection → [Set Stage] → [Return Category Menu]
    │
    ├─→ algorithm selection → [Set Pending] → [Return Input Prompt]
    │
    ├─→ array input → [Parse Array] → [Build Steps] → [Return First Step]
    │
    ├─→ next → [Increment Index] → [Return Next Step]
    │
    ├─→ explain → [Lookup Explanation] → [Return Explanation]
    │
    └─→ reset → [Clear Session] → [Return Success]
```

## Principles of Programming Languages in Application

### 1. Lexical Analysis (Tokenization)

The DSL uses **ANTLR4** for lexical analysis, which breaks input strings into tokens.

#### Token Definitions (from `AlgoDSL.g4`)

**Keywords:**
- `MENU`: 'menu'
- `NEXT`: 'next'
- `EXPLAIN`: 'explain'
- `RESET`: 'reset'
- `VISUALIZE`: 'visualize'
- `ON`: 'on'

**Category Keywords:**
- `SORTING_KEYWORDS`: 'sorting algorithms' | 'sorting algorithm' | 'sort algorithms' | 'sort algorithm' | 'sorting' | 'sort'
- `PATHFINDING_KEYWORDS`: 'pathfinding algorithms' | 'pathfinding algorithm' | 'path algorithms' | 'path algorithm' | 'pathfinding' | 'path'
- `DATA_STRUCTURE_KEYWORDS`: 'data structures' | 'data structure' | 'structures' | 'structure' | 'data'

**Algorithm Keywords:**
- `BUBBLE_KEYWORDS`: 'bubble sort' | 'bubblesort' | 'bubble'
- `MERGE_KEYWORDS`: 'merge sort' | 'mergesort' | 'merge'
- `SELECTION_KEYWORDS`: 'selection sort' | 'selectionsort' | 'selection'
- `INSERTION_KEYWORDS`: 'insertion sort' | 'insertionsort' | 'insertion'
- `QUICK_KEYWORDS`: 'quick sort' | 'quicksort' | 'quick'
- `HEAP_KEYWORDS`: 'heap sort' | 'heapsort' | 'heap'

**Data Structure Keywords:**
- `STACK_DS`: 'stack data structure' | 'stack structure' | 'stack' | 'lifo' | 'lifo stack'
- `QUEUE_DS`: 'queue data structure' | 'queue structure' | 'queue' | 'fifo' | 'fifo queue'
- `LINKEDLIST_DS`: 'linked list (singly)' | 'linked list' | 'singly linked list' | 'linked'

**Literals:**
- `NUMBER`: '-'? [0-9]+ (integers, optionally negative)
- `NUMBER_ONE` through `NUMBER_SIX`: '1' through '6'
- `LBRACKET`: '['
- `RBRACKET`: ']'
- `COMMA`: ','

**Whitespace:**
- `WS`: [ \t\r\n]+ -> skip (whitespace is ignored)

#### Tokenization Process

1. **Input String**: `"visualize bubble sort on [5, 2, 8]"`
2. **Lexer Output**: 
   ```
   VISUALIZE 'visualize'
   BUBBLE_KEYWORDS 'bubble sort'
   ON 'on'
   LBRACKET '['
   NUMBER '5'
   COMMA ','
   NUMBER '2'
   COMMA ','
   NUMBER '8'
   RBRACKET ']'
   EOF
   ```

3. **Token Stream**: Sequence of tokens passed to parser

### 2. Syntax Analysis (Context-Free Grammar)

The grammar is defined using **ANTLR4's EBNF notation** in `AlgoDSL.g4`.

#### Grammar Rules

**Top-Level Command Rule:**
```
command
    : menuCommand
    | menuSelection
    | sortingAlgorithmSelection
    | dataStructureSelection
    | arrayInput
    | nextCommand
    | explainCommand
    | resetCommand
    | visualizeCommand
    ;
```

**Menu Selection Rule:**
```
menuSelection
    : SORTING_KEYWORDS    #MenuSorting
    | PATHFINDING_KEYWORDS #MenuPathfinding
    | DATA_STRUCTURE_KEYWORDS #MenuDataStructures
    | NUMBER_ONE          #MenuSortingNumber
    | NUMBER_TWO          #MenuPathfindingNumber
    | NUMBER_THREE        #MenuDataStructuresNumber
    ;
```

**Algorithm Selection Rule:**
```
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
```

**Array Input Rule:**
```
arrayInput
    : NUMBER (COMMA NUMBER)*
    ;
```

**Array Literal Rule:**
```
arrayLiteral
    : LBRACKET arrayInput? RBRACKET
    ;
```

#### Parse Tree Generation

ANTLR4 generates a **parse tree** (concrete syntax tree) from the token stream:

**Example Parse Tree for `"bubble sort"`:**
```
command
└── sortingAlgorithmSelection
    └── SelectBubbleSort
        └── BUBBLE_KEYWORDS: 'bubble sort'
```

**Example Parse Tree for `"[5, 2, 8]"`:**
```
command
└── arrayInput
    ├── NUMBER: '5'
    ├── COMMA: ','
    ├── NUMBER: '2'
    ├── COMMA: ','
    └── NUMBER: '8'
```

### 3. Semantic Analysis & AST Generation

While ANTLR4 generates a parse tree, the current implementation uses **pattern matching** for semantic analysis rather than a full AST walk. However, the grammar structure supports AST generation.

#### Current Semantic Analysis Approach

The interpreter performs semantic analysis through:

1. **Keyword Matching**: Maps user input to canonical algorithm names
   ```python
   SORTING_SELECTION_KEYWORDS = {
       "bubble sort": "Bubble Sort",
       "bubble": "Bubble Sort",
       "1": "Bubble Sort",
       ...
   }
   ```

2. **Stage-Based Routing**: Determines command meaning based on current session stage
   - `stage == "menu"`: Numbers/keywords select categories
   - `stage == "sorting_menu"`: Numbers/keywords select algorithms
   - `stage == "await_array"`: Input is parsed as array
   - `stage == "visualizing"`: "next" advances steps

3. **Type Validation**: 
   - Array parsing validates integer format
   - Grid configuration validates JSON structure
   - Algorithm names validated against available builders

#### Potential AST-Based Semantic Analysis

With ANTLR4's listener pattern, semantic analysis could be implemented as:

```python
class AlgoDSLSemanticAnalyzer(AlgoDSLListener):
    def __init__(self):
        self.command_type = None
        self.algorithm = None
        self.array_values = []
    
    def enterSelectBubbleSort(self, ctx):
        self.algorithm = "Bubble Sort"
        self.command_type = "algorithm_selection"
    
    def enterArrayInput(self, ctx):
        # Extract numbers from parse tree
        for child in ctx.children:
            if isinstance(child, TerminalNode) and child.symbol.type == AlgoDSLLexer.NUMBER:
                self.array_values.append(int(child.getText()))
```

### 4. Abstraction of Business Logic

The system abstracts business logic through several layers:

#### Layer 1: Command Abstraction

User commands are abstracted into **canonical operations**:
- Menu navigation → `_menu_payload()`, `_sorting_menu_payload()`
- Algorithm selection → `_match_sorting_selection()`, `_match_pathfinding_selection()`
- Input parsing → `_parse_array()`, `_is_array_literal()`
- Step generation → Algorithm builder functions

#### Layer 2: Algorithm Abstraction

Each algorithm is abstracted as a **builder function**:

```python
def generate_bubble_sort_steps(array: List[int]) -> List[Dict[str, Any]]:
    """Abstract bubble sort algorithm into visualization steps."""
    steps = []
    # ... algorithm logic ...
    return steps
```

**Abstraction Benefits:**
- Uniform interface: All builders take input and return step list
- Encapsulation: Algorithm details hidden from interpreter
- Extensibility: New algorithms added by creating new builder functions

#### Layer 3: State Abstraction

Algorithm state is abstracted through **AlgorithmRunner**:

```python
@dataclass
class AlgorithmRunner:
    algorithm: str
    steps: List[Dict[str, Any]]
    index: int = 0
    
    def step(self) -> Dict[str, Any]:
        """Abstract step navigation."""
        result = self.steps[self.index]
        if self.index < len(self.steps) - 1:
            self.index += 1
        return result
```

**Abstraction Benefits:**
- Navigation logic separated from algorithm logic
- Consistent step access interface
- Easy to add features (backward navigation, jumping to step)

#### Layer 4: Response Abstraction

All responses follow a **unified structure**:

```python
{
    "status": "success" | "error",
    "type": "menu" | "visualization_step" | "explanation" | ...,
    "data": {...},  # Type-specific data
    "explanation": "...",
    ...
}
```

**Abstraction Benefits:**
- Client can handle all response types uniformly
- Easy to add new response types
- Consistent error handling

## Running the Server

### Prerequisites

- Python 3.8+
- Java (for ANTLR4 parser generation, optional)

### Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running

```bash
# Development mode with auto-reload
uvicorn server.main:app --reload --port 8069

# Production mode
uvicorn server.main:app --host 0.0.0.0 --port 8069
```

### Generating ANTLR Parser (Optional)

The ANTLR parser is pre-generated, but to regenerate after grammar changes:

```bash
cd server
java -jar antlr4-4.9.2-complete.jar -Dlanguage=Python3 -o parser/grammar grammar/AlgoDSL.g4
```

Or use the Makefile:

```bash
make -C server generate
```

## Example Usage

### Example 1: Sorting Algorithm Flow

```bash
# 1. Get main menu
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user1","command":"menu"}'

# 2. Select sorting category
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user1","command":"1"}'

# 3. Select bubble sort
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user1","command":"bubble sort"}'

# 4. Provide array
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user1","command":"[5, 2, 8, 1, 9]"}'

# 5. Advance steps
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user1","command":"next"}'
```

### Example 2: Data Structure Flow

```bash
# 1. Select data structures
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user2","command":"3"}'

# 2. Select stack
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user2","command":"stack"}'

# 3. Provide initial values
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user2","command":"[1, 2, 3, 4]"}'
```

## Supported Algorithms

### Sorting Algorithms
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

### Pathfinding Algorithms
- Dijkstra's Algorithm
- A* (A-Star)
- Breadth-First Search (BFS)
- Depth-First Search (DFS)

### Data Structures
- Stack (LIFO)
- Queue (FIFO)
- Linked List (Singly)

## API Endpoints

- `POST /command`: Process user commands
- `GET /greeting`: Get initial menu
- `GET /`: Health check

## Architecture Notes

- **Session-based**: Each user session maintains independent state
- **Stateful**: Algorithm state persists across multiple requests
- **Extensible**: New algorithms can be added by creating builder functions
- **Grammar-driven**: DSL structure defined in ANTLR4 grammar file
- **Pattern matching**: Current implementation uses regex/keyword matching (ANTLR parser available but not actively used)

## How to Run the Application

### Prerequisites

**Server:**
- Python 3.8+
- Java (for ANTLR4 parser generation, optional)
- Conda/Miniconda (recommended)

**Client:**
- Node.js 20+
- npm or yarn
- Android Studio (for Android emulator)
- Xcode (for iOS simulator, macOS only)

### Step 1: Start the Server

1. **Navigate to server directory:**
   ```bash
   cd server
   ```

2. **Activate conda environment:**
   ```bash
   conda activate base
   ```

3. **Install dependencies (if not already installed):**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server:**
   ```bash
   python run_server.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn server.main:app --reload --host 0.0.0.0 --port 8069
   ```

5. **Verify server is running:**
   ```bash
   curl http://localhost:8069/
   ```
   
   You should see: `{"status":"ok","message":"Algorithms Visualizer Server is running"}`

The server will be running on `http://localhost:8069` (or the port specified in `.env`).

### Step 2: Configure Client API URL

Before running the client, configure the API URL based on your target platform:

1. **Open the API configuration file:**
   ```bash
   cd algorithms-visualizer-client
   # Edit config/api.ts
   ```

2. **Set the appropriate URL:**

   **For Android Emulator:**
   ```typescript
   export const SERVER_BASE_URL = 'http://10.0.2.2:8069';
   ```

   **For iOS Simulator:**
   ```typescript
   export const SERVER_BASE_URL = 'http://localhost:8069';
   ```

   **For Physical Device:**
   ```typescript
   // Use your computer's IP address
   export const SERVER_BASE_URL = 'http://192.168.1.100:8069';
   ```
   
   To find your computer's IP address:
   ```bash
   # macOS/Linux
   ifconfig | grep "inet " | grep -v 127.0.0.1
   # Or on macOS:
   ipconfig getifaddr en0
   
   # Windows
   ipconfig
   ```

### Step 3: Start the Client

#### Option A: Run on Android Emulator

1. **Start Android Emulator:**
   - Open Android Studio
   - Go to **Tools → Device Manager**
   - Click the Play button next to your emulator
   
   Or from command line:
   ```bash
   emulator -avd <your_avd_name>
   ```

2. **Install dependencies:**
   ```bash
   cd algorithms-visualizer-client
   npm install
   ```

3. **Start Expo:**
   ```bash
   npx expo start
   ```

4. **Build and run on Android:**
   ```bash
   # First time: Generate native Android project
   npx expo prebuild --platform android
   
   # Build and install on emulator
   npm run android
   ```
   
   Or press `a` in the Expo CLI to open on Android emulator.

#### Option B: Run on iOS Simulator (macOS only)

1. **Install dependencies:**
   ```bash
   cd algorithms-visualizer-client
   npm install
   ```

2. **Start Expo:**
   ```bash
   npx expo start
   ```

3. **Run on iOS:**
   ```bash
   npm run ios
   ```
   
   Or press `i` in the Expo CLI to open on iOS simulator.

#### Option C: Run on Physical Device

1. **Ensure your device and computer are on the same Wi-Fi network**

2. **Configure API URL** with your computer's IP address (see Step 2)

3. **Start Expo:**
   ```bash
   cd algorithms-visualizer-client
   npx expo start
   ```

4. **Scan QR code:**
   - Install **Expo Go** app on your device
   - Scan the QR code displayed in the terminal
   - Note: Some features may be limited in Expo Go

### Step 4: Verify Everything Works

1. **Server is running** - Check terminal shows: `Uvicorn running on http://0.0.0.0:8069`

2. **Client connects** - In the app, you should see the main menu

3. **Test a command:**
   - Type `menu` in the chat
   - Select `1` for sorting algorithms
   - Select `1` for Bubble Sort
   - Enter `[5, 2, 8, 1, 9]`
   - Click "Next" to see visualization steps

### Troubleshooting

#### Server Issues

**Port already in use:**
```bash
# Find process using port 8069
lsof -i :8069
# Kill the process
kill -9 <PID>
```

**Import errors:**
```bash
# Ensure you're in the server directory
cd server
# Verify Python path
which python
# Reinstall dependencies
pip install -r requirements.txt
```

#### Client Issues

**Cannot connect to server:**
- Verify server is running: `curl http://localhost:8069/`
- Check API URL in `config/api.ts` matches your platform
- For Android emulator, ensure URL is `http://10.0.2.2:8069`
- For physical device, ensure device and computer are on same network

**Build errors:**
```bash
# Clear cache and rebuild
cd algorithms-visualizer-client
npx expo start --clear
# Or clean native projects
npx expo prebuild --clean
```

**Android emulator not detected:**
```bash
# Check if emulator is running
adb devices
# Restart adb if needed
adb kill-server
adb start-server
```

### Quick Start Summary

```bash
# Terminal 1: Start Server
cd server
conda activate base
python run_server.py

# Terminal 2: Start Client
cd algorithms-visualizer-client
# Configure config/api.ts for your platform
npm install
npx expo start
# Press 'a' for Android or 'i' for iOS
```

## Demo