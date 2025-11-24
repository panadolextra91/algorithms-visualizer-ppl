# API Testing Guide

## Server Endpoints

### 1. Health Check
```bash
curl http://localhost:8069/
```

**Expected Response:**
```json
{
  "status": "ok",
  "message": "Algorithms Visualizer Server is running"
}
```

### 2. Get Greeting Message
```bash
curl http://localhost:8069/greeting
```

**Expected Response:**
```json
{
  "status": "success",
  "type": "greeting",
  "message": "Hello, what are we going to do today, developer?\n1. Sorting algorithms.\n2. Pathfinding algorithms.\n3. Data structures"
}
```

### 3. Send Commands

#### Test Menu Selection (Sorting)
```bash
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"test123","command":"sorting"}'
```

**Expected Response:**
```json
{
  "status": "success",
  "type": "menu",
  "message": "Currently we have these algorithms for sorting, please select an algorithm that you want to explore:\n\n1. Bubble Sort\n2. Merge Sort\n3. Selection Sort\n4. Insertion Sort\n5. Quick Sort\n6. Heap Sort\n\nYou can type a number (1-6) or part of the algorithm name (e.g., 'bubble', 'quick')."
}
```

#### Test Algorithm Selection (Bubble Sort)
```bash
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"test123","command":"1"}'
```

**Expected Response:**
```json
{
  "status": "success",
  "type": "prompt",
  "message": "Great! You selected Bubble Sort. Now please enter an array of numbers to sort. Separate each number with a comma (e.g., 5,2,8,1,9):"
}
```

#### Test Array Input
```bash
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"test123","command":"5,2,8,1,9"}'
```

**Expected Response:**
```json
{
  "status": "success",
  "type": "visualization_step",
  "algorithm": "Bubble Sort",
  "step": 1,
  "data": {
    "array": [2, 5, 8, 1, 9],
    "highlighted_indices": [0, 1],
    "sorted_indices": []
  },
  "explanation": "Comparing elements at index 0 (5) and index 1 (2). Since the left is greater, they are swapped."
}
```

#### Test Next Step
```bash
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"test123","command":"next"}'
```

#### Test Pathfinding Menu
```bash
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"test456","command":"pathfinding"}'
```

#### Test Data Structures Menu
```bash
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"test789","command":"data structures"}'
```

## Complete Flow Test

### Test Full Sorting Flow:
```bash
# 1. Start with greeting (or use menu selection)
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"flow123","command":"sorting"}'

# 2. Select algorithm
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"flow123","command":"bubble"}'

# 3. Enter array
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"flow123","command":"5,2,8,1,9"}'

# 4. Get next steps
curl -X POST http://localhost:8069/command \
  -H "Content-Type: application/json" \
  -d '{"sessionId":"flow123","command":"next"}'
```

## Testing from Mobile App

1. **Start the server** (already running on port 8069)
2. **Open the mobile app** - it should automatically:
   - Load the greeting message when chat screen opens
   - Be ready to accept commands

3. **Test in the app:**
   - Type "sorting" → Should show sorting menu
   - Type "1" or "bubble" → Should prompt for array
   - Type "5,2,8,1,9" → Should start visualization
   - Type "next" → Should show next step

## Common Test Commands

```bash
# Menu selections
"sorting" / "sort" / "1"
"pathfinding" / "path" / "2"  
"data structures" / "data" / "3"

# Algorithm selection (when in sorting menu)
"1" / "bubble" / "bubble sort"
"2" / "merge" / "merge sort"
"5" / "quick" / "quick sort"

# Array input (after algorithm selection)
"5,2,8,1,9"
"3,7,1,4,2"

# Control commands
"next" - Advance algorithm step
"explain" - Get algorithm explanation
"reset" - Clear session
```

## Troubleshooting

- **Server not responding**: Check if server is running on port 8069
- **Connection errors**: Make sure mobile device and server are on same network
- **For iOS Simulator**: Use `http://localhost:8069`
- **For Physical Device**: Use your computer's IP address (e.g., `http://192.168.1.100:8069`)



