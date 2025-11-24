# Client Configuration Guide

## API Server URL Configuration

The API server URL is configured in `config/api.ts`. Edit this file to switch between platforms:

### **For iOS Simulator:**
```typescript
// iOS Simulator (use localhost)
export const SERVER_BASE_URL = 'http://localhost:8069';
```

### **For Android Emulator:**
```typescript
// Android Emulator (use 10.0.2.2)
export const SERVER_BASE_URL = 'http://10.0.2.2:8069';
```

### **For Physical Device:**
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

## Quick Setup

1. Open `config/api.ts`
2. Comment/uncomment the appropriate URL
3. Save the file
4. Restart Expo (the app will reload automatically)

## Example Configuration

```typescript
// config/api.ts

// iOS Simulator (use localhost)
export const SERVER_BASE_URL = 'http://localhost:8069';

// Android Emulator (use 10.0.2.2)
// export const SERVER_BASE_URL = 'http://10.0.2.2:8069';

// Physical Device (use your computer's IP address)
// export const SERVER_BASE_URL = 'http://192.168.1.100:8069';
```

Just comment/uncomment the line you need!
