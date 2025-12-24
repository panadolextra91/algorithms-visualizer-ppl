# System Workflow Diagram

## Main System Flow

```mermaid
flowchart TD
    A[Client Request] --> B[FastAPI POST /command]
    B --> C{Session Exists?}
    C -->|No| D[Create New Session]
    C -->|Yes| E[Get Existing Session]
    D --> F[AlgorithmSessionManager]
    E --> F
    F --> G[DSL Interpreter]
    G --> H{Command Type?}
    
    H -->|menu| I[Reset Session]
    I --> J[Return Main Menu]
    
    H -->|category selection| K{Current Stage?}
    K -->|menu| L[Set Stage to Category Menu]
    K -->|category_menu| M[Set Stage to Algorithm Menu]
    L --> N[Return Category Menu]
    M --> O[Return Algorithm Menu]
    
    H -->|algorithm selection| P{Stage?}
    P -->|sorting_menu| Q[Set Pending Algorithm]
    P -->|pathfinding_menu| R[Set Pending Algorithm]
    P -->|data_structure_menu| S[Set Pending Algorithm]
    Q --> T[Set Stage: await_array]
    R --> U[Set Stage: await_grid]
    S --> T
    T --> V[Return Input Prompt]
    U --> W[Return Grid Config Prompt]
    
    H -->|array input| X{Stage == await_array?}
    X -->|Yes| Y[Parse Array]
    X -->|No| Z[Error: Invalid Stage]
    Y --> AA{Algorithm Type?}
    AA -->|Sorting| AB[Call Sorting Builder]
    AA -->|Data Structure| AC[Call DS Builder]
    AB --> AD[Create AlgorithmRunner]
    AC --> AD
    AD --> AE[Return First Step]
    
    H -->|grid config| AF{Stage == await_grid?}
    AF -->|Yes| AG[Parse Grid Config]
    AF -->|No| Z
    AG --> AH[Call Pathfinding Builder]
    AH --> AD
    
    H -->|next| AI{Has Active Algorithm?}
    AI -->|Yes| AJ[Increment Step Index]
    AI -->|No| AK[Error: No Algorithm]
    AJ --> AL[Return Next Step]
    
    H -->|explain| AM[Lookup Explanation]
    AM --> AN[Return Explanation]
    
    H -->|reset| AO[Clear Session State]
    AO --> AP[Return Success]
    
    J --> AQ[JSON Response]
    N --> AQ
    O --> AQ
    V --> AQ
    W --> AQ
    AE --> AQ
    AL --> AQ
    AN --> AQ
    AP --> AQ
    Z --> AQ
    AK --> AQ
    AQ --> AR[Client]
```

## Command Processing Flow

```mermaid
flowchart LR
    A[User Input] --> B[Command String]
    B --> C[Pattern Matching]
    C --> D{Match Found?}
    D -->|Yes| E[Extract Parameters]
    D -->|No| F[Keyword Matching]
    F --> G{Keyword Found?}
    G -->|Yes| E
    G -->|No| H[Error: Unknown Command]
    E --> I[Route by Stage]
    I --> J[Execute Operation]
    J --> K[Generate Response]
    K --> L[Return JSON]
```

## Algorithm Visualization Flow

```mermaid
flowchart TD
    A[Input Received] --> B{Input Type?}
    B -->|Array| C[Parse Array Values]
    B -->|Grid Config| D[Parse Grid JSON]
    
    C --> E{Algorithm Type?}
    E -->|Sorting| F[Sorting Builder]
    E -->|Data Structure| G[Data Structure Builder]
    
    D --> H[Pathfinding Builder]
    
    F --> I[Generate Steps]
    G --> I
    H --> I
    
    I --> J[Create Step Objects]
    J --> K[Add Explanations]
    K --> L[Create AlgorithmRunner]
    L --> M[Store in Session]
    M --> N[Return First Step]
    
    N --> O[User Clicks Next]
    O --> P[Increment Index]
    P --> Q[Return Next Step]
    Q --> R{Is Final Step?}
    R -->|No| O
    R -->|Yes| S[Stop Navigation]
```

## Session State Machine

```mermaid
stateDiagram-v2
    [*] --> idle: Session Created
    idle --> menu: menu command
    menu --> sorting_menu: "1" or "sorting"
    menu --> pathfinding_menu: "2" or "pathfinding"
    menu --> data_structure_menu: "3" or "data structures"
    
    sorting_menu --> await_array: Algorithm Selected
    pathfinding_menu --> await_grid: Algorithm Selected
    data_structure_menu --> await_array: Data Structure Selected
    
    await_array --> visualizing: Array Provided
    await_grid --> visualizing: Grid Configured
    
    visualizing --> visualizing: next command
    visualizing --> menu: menu command
    visualizing --> [*]: reset command
    
    menu --> [*]: reset command
    sorting_menu --> menu: menu command
    pathfinding_menu --> menu: menu command
    data_structure_menu --> menu: menu command
    await_array --> menu: menu command
    await_grid --> menu: menu command
```

## Algorithm Builder Flow

```mermaid
flowchart TD
    A[Builder Function Called] --> B[Initialize Variables]
    B --> C[Execute Algorithm Logic]
    C --> D{Algorithm Type?}
    
    D -->|Sorting| E[Track Array State]
    E --> F[Track Highlighted Indices]
    F --> G[Track Sorted Indices]
    G --> H[Generate Step]
    H --> I{More Steps?}
    
    D -->|Pathfinding| J[Initialize Grid]
    J --> K[Track Visited Nodes]
    K --> L[Track Path]
    L --> M[Track Frontier]
    M --> H
    
    D -->|Data Structure| N[Initialize Structure]
    N --> O[Track Operations]
    O --> P[Track State Changes]
    P --> H
    
    I -->|Yes| C
    I -->|No| Q[Add Final Step]
    Q --> R[Return Step List]
```

## Response Generation Flow

```mermaid
flowchart TD
    A[Operation Complete] --> B{Response Type?}
    
    B -->|Menu| C[Build Menu Payload]
    C --> D[Add Options]
    D --> E[JSON Response]
    
    B -->|Visualization Step| F[Extract Step Data]
    F --> G[Format Array/Grid/DS Data]
    G --> H[Add Explanation]
    H --> I[Set isFinal Flag]
    I --> E
    
    B -->|Explanation| J[Lookup Explanation Text]
    J --> K[Format Explanation]
    K --> E
    
    B -->|Error| L[Create Error Message]
    L --> E
    
    E --> M[Send to Client]
```

## Lexical Analysis Flow

```mermaid
flowchart LR
    A[Input String] --> B[ANTLR Lexer]
    B --> C[Token Stream]
    C --> D{Token Type?}
    D -->|Keyword| E[Keyword Token]
    D -->|Number| F[Number Token]
    D -->|Punctuation| G[Punctuation Token]
    D -->|Whitespace| H[Skip]
    E --> I[Parser]
    F --> I
    G --> I
    H --> I
    I --> J[Parse Tree]
```

## Syntax Analysis Flow

```mermaid
flowchart TD
    A[Token Stream] --> B[ANTLR Parser]
    B --> C[Apply Grammar Rules]
    C --> D{Match Rule?}
    D -->|Yes| E[Create Parse Tree Node]
    D -->|No| F[Try Alternative Rule]
    F --> D
    E --> G{More Tokens?}
    G -->|Yes| C
    G -->|No| H[Complete Parse Tree]
    H --> I[Semantic Analysis]
```

## Semantic Analysis Flow

```mermaid
flowchart TD
    A[Parse Tree] --> B[Walk Tree]
    B --> C{Node Type?}
    C -->|Menu Selection| D[Map to Category]
    C -->|Algorithm Selection| E[Map to Algorithm Name]
    C -->|Array Input| F[Extract Numbers]
    C -->|Command| G[Identify Command Type]
    
    D --> H[Update Session Stage]
    E --> I[Set Pending Algorithm]
    F --> J[Validate Array]
    G --> K[Execute Command Logic]
    
    H --> L[Generate Response]
    I --> L
    J --> L
    K --> L
    L --> M[Return to Client]
```

