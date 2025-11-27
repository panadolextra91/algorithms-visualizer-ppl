# Algorithms Visualizer

An interactive algorithms visualization chatbot application with a Python FastAPI server and React Native mobile client. Users can explore sorting algorithms, pathfinding algorithms, and data structures through step-by-step visualizations.

## Project Structure

```
algorithms-visualizer/
├── server/                    # Python FastAPI backend
│   ├── grammar/              # ANTLR grammar definitions
│   ├── parser/               # Generated ANTLR parser
│   ├── dsl_interpreter.py    # Command interpreter
│   ├── main.py               # FastAPI application
│   └── requirements.txt      # Python dependencies
└── algorithms-visualizer-client/  # React Native/Expo frontend
    ├── app/                  # Expo Router screens
    ├── components/            # React components
    ├── services/             # API client and services
    └── stores/               # State management (Zustand)
```

## Features

- **6 Sorting Algorithms**: Bubble Sort, Merge Sort, Selection Sort, Insertion Sort, Quick Sort, Heap Sort
- **Interactive Visualization**: Step-by-step bar chart visualization with color-coded states
- **Command-Based Interface**: Natural language commands parsed with ANTLR grammar
- **Cross-Platform**: iOS and Android support via React Native/Expo
- **State Management**: Cached algorithm steps with forward/backward navigation

## Server Setup

### Prerequisites

- Python 3.13
- Java (for ANTLR parser generation)
- Conda/Miniconda (recommended)

### Configuration

Server configuration is stored in `server/.env` file:

```bash
PORT=8069
HOST=0.0.0.0
```

Edit `.env` to change the port or host.

### Installation

```bash
cd server
conda activate base
pip install -r requirements.txt
```

### Generate ANTLR Parser

```bash
# Ensure Java is installed
make -C server generate
```

This generates Python parser/lexer code into `server/parser` using `server/grammar/AlgoDSL.g4`.

### Running the Server

**Option 1: Using the run script (recommended)**
```bash
cd server
conda activate base
python run_server.py  # Use 'python' not 'python3' when conda is activated
```

**Option 2: Using uvicorn directly**
```bash
cd server
conda activate base
uvicorn main:app --reload --host 0.0.0.0 --port 8069
```

The server will start on `http://localhost:8069` (or the port specified in `.env`).

### Testing the Server

```bash
# Health check
curl http://localhost:8069/

# Get greeting
curl http://localhost:8069/greeting

# Send command
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user12345","command":"menu"}'
```

## Client Setup

### Prerequisites

- Node.js 20+
- npm or yarn
- Expo CLI (optional, for development)

### Installation

```bash
cd algorithms-visualizer-client
npm install
```

### Configuration

The API server URL is configured in `algorithms-visualizer-client/config/api.ts`. Edit this file to switch between platforms:

**For iOS Simulator:**
```typescript
// iOS Simulator (use localhost)
export const SERVER_BASE_URL = 'http://localhost:8069';
```

**For Android Emulator:**
```typescript
// Android Emulator (use 10.0.2.2)
export const SERVER_BASE_URL = 'http://10.0.2.2:8069';
```

**For Physical Device:**
```typescript
// Physical Device (use your computer's IP address)
export const SERVER_BASE_URL = 'http://192.168.1.100:8069';
```

**To find your computer's IP address:**
```bash
# macOS
ifconfig | grep "inet " | grep -v 127.0.0.1
# Or use:
ipconfig getifaddr en0
```

**Quick Setup:**
1. Open `algorithms-visualizer-client/config/api.ts`
2. Comment/uncomment the appropriate URL
3. Save the file
4. Restart Expo (the app will reload automatically)

### Running the Client

```bash
cd algorithms-visualizer-client
npx expo start
```

In the output, you'll find options to open the app in:
- Development build
- Android emulator
- iOS simulator
- Expo Go (limited functionality)

### Prebuild iOS (Optional)

To generate the iOS native project:

```bash
cd algorithms-visualizer-client
npx expo prebuild --platform ios
cd ios
pod install
```

## Usage

### Available Commands

The server understands the following commands (defined in `server/grammar/AlgoDSL.g4`):

- `menu` - Return to main selection menu
- `sorting` or `1` - Show sorting algorithms menu
- `pathfinding` or `2` - Show pathfinding algorithms menu
- `data structures` or `3` - Show data structures menu
- `1-6` or algorithm name - Select a sorting algorithm
- `5,2,8,1,9` - Input array for sorting (comma-separated numbers)
- `next` - Advance to next step
- `explain` - Get algorithm explanation and principle
- `reset` - Reset current session

### Example Workflow

1. **Start the server:**
   ```bash
   cd server
   conda activate base
   python run_server.py
   ```

2. **Start the client:**
   ```bash
   cd algorithms-visualizer-client
   npx expo start
   ```

3. **In the app:**
   - Type `sorting` or `1` to see sorting algorithms
   - Type `1` or `bubble` to select Bubble Sort
   - Type `5,2,8,1,9` to input an array
   - Use the **Next** and **Previous** buttons to navigate steps
   - Type `explain` to see algorithm principles and current progress

### Visualization Features

- **Bar Chart Display**: Array values shown as bars with automatic sizing
- **Color Coding**:
  - Gray: Unsorted elements
  - Yellow: Currently comparing
  - Green: Already sorted
  - Red: Elements being swapped
- **Step Navigation**: Navigate forward/backward through cached steps
- **Real-time Updates**: Card updates in place (no new cards created)

## Development

### Project Structure

- **Server**: Python FastAPI with ANTLR-based DSL parser
- **Client**: React Native with Expo Router, Zustand for state management
- **Grammar**: ANTLR grammar file defines all commands and tokens

### Adding New Algorithms

1. Create a state class in `server/dsl_interpreter.py` (similar to `BubbleSortState`)
2. Add the algorithm to `SORTING_ALGORITHMS` list
3. Update `_handle_array_input()` to instantiate the new state
4. Update `_get_algorithm_principle()` with algorithm explanation

### CI/CD

GitHub Actions workflows are configured for:
- Server: Python syntax checking, import validation, command parsing tests
- Client: ESLint, TypeScript type checking

Workflows run automatically on push/PR to `main` and `develop` branches.

## Technology Stack

**Server:**
- Python 3.13
- FastAPI
- ANTLR 4.9.2
- Uvicorn

**Client:**
- React Native 0.81.5
- Expo ~54.0
- TypeScript
- Zustand (state management)
- Expo Router (navigation)

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

