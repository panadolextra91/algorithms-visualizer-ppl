// App Constants
export const APP_NAME = 'Algorithms Visualizer';
export const APP_VERSION = '1.0.0';

// API Configuration
export const API_BASE_URL = __DEV__ 
  ? 'http://localhost:8069' 
  : 'https://your-production-api.com';

// Algorithm Types
export const ALGORITHM_TYPES = {
  SORTING: 'sorting',
  PATHFINDING: 'pathfinding', 
  DATA_STRUCTURES: 'data_structures',
} as const;

// Sorting Algorithms
export const SORTING_ALGORITHMS = [
  'Bubble Sort',
  'Merge Sort',
  'Selection Sort',
  'Insertion Sort',
  'Quick Sort',
  'Heap Sort',
] as const;

// Pathfinding Algorithms
export const PATHFINDING_ALGORITHMS = [
  'BFS',
  'DFS',
  'Dijkstra',
  'A*',
] as const;

// Data Structures
export const DATA_STRUCTURES = [
  'Queue (FIFO)',
  'Array',
  'Stack (LIFO)',
  'Linked List (Singly)',
  'Linked List (Doubly)',
  'Binary Search Tree (BST)',
  'Trie (Prefix Tree)',
  'Hash Table',
] as const;

// Storage Keys
export const STORAGE_KEYS = {
  SESSION_ID: 'sessionId',
  CHAT_HISTORY: 'chatHistory',
  USER_PREFERENCES: 'userPreferences',
} as const;




