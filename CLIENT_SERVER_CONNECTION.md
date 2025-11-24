# Client-Server Connection Testing Guide

## ✅ Connection Status: CONNECTED

The client is fully connected to the server. Here's what's been implemented:

### **Connection Components:**

1. **API Client** (`services/api/client.ts`)
   - Configured to connect to `http://localhost:8069`
   - Handles GET `/greeting` and POST `/command` endpoints
   - Error handling for network issues

2. **Session Management** (`services/session/SessionManager.ts`)
   - Generates anonymous session IDs
   - Maintains session state

3. **Chat Screen Integration** (`app/chat.tsx`)
   - Automatically loads greeting on mount
   - Sends user commands to server
   - Displays server responses
   - Shows visualization steps with bar charts
   - Error handling with user-friendly messages

## 🧪 Testing Steps

### **1. Start the Server**
```bash
cd /Users/huynhngocanhthu/algorithms-visualizer/server
conda activate base
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8069
```

### **2. Start the Mobile App**
```bash
cd /Users/huynhngocanhthu/algorithms-visualizer/algorithms-visualizer-client
npx expo start
```

### **3. Test the Connection**

**In the Mobile App:**

1. **App opens** → Splash screen (2 seconds) → Chat screen
2. **Greeting should appear automatically:**
   ```
   "Hello, what are we going to do today, developer?
   1. Sorting algorithms.
   2. Pathfinding algorithms.
   3. Data structures"
   ```

3. **Test Sorting Flow:**
   - Type: `"sorting"` or `"1"`
   - Expected: Menu with 6 sorting algorithms
   - Type: `"1"` or `"bubble"`
   - Expected: Prompt for array input
   - Type: `"5,2,8,1,9"`
   - Expected: Bar chart visualization appears!

4. **Test Next Steps:**
   - Type: `"next"`
   - Expected: Next step with updated bar colors

5. **Test Other Algorithms:**
   - Try: `"2"` (Merge Sort), `"3"` (Selection Sort), etc.
   - All should work now!

## 🔧 Troubleshooting

### **If you see "Cannot connect to server":**

**For iOS Simulator:**
- `localhost` should work
- Make sure server is running on port 8069

**For Android Emulator:**
- Change API_BASE_URL to `http://10.0.2.2:8069`

**For Physical Device:**
- Find your computer's IP address:
  ```bash
  # macOS
  ifconfig | grep "inet " | grep -v 127.0.0.1
  ```
- Update `services/api/client.ts`:
  ```typescript
  const API_BASE_URL = __DEV__ 
    ? 'http://YOUR_IP_ADDRESS:8069'  // e.g., http://192.168.1.100:8069
    : 'https://your-production-api.com';
  ```
- Make sure phone and computer are on same WiFi network

### **Common Issues:**

1. **Server not running:**
   - Error: "Cannot connect to server"
   - Solution: Start server on port 8069

2. **Wrong port:**
   - Error: Connection refused
   - Solution: Verify server is on port 8069

3. **Network issues:**
   - Error: Network request failed
   - Solution: Check WiFi connection, use IP address for physical devices

## ✅ Expected Behavior

**When everything works:**
- ✅ Greeting loads automatically
- ✅ Commands send to server
- ✅ Server responses appear in chat
- ✅ Visualization steps show bar charts
- ✅ "next" command advances algorithm
- ✅ All 6 sorting algorithms work

## 🎯 Quick Test Commands

```
"sorting" → Shows sorting menu
"1" → Selects Bubble Sort
"5,2,8,1,9" → Starts visualization
"next" → Next step
"2" → Selects Merge Sort
"3,7,1,4,2" → Starts Merge Sort visualization
```

The connection is ready! Just make sure both server and client are running. 🚀
