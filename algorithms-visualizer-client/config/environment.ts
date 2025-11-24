// Environment Configuration
export const ENV = {
  DEVELOPMENT: __DEV__,
  PRODUCTION: !__DEV__,
} as const;

// API Configuration
export const API_CONFIG = {
  BASE_URL: __DEV__ 
    ? 'http://localhost:8069' 
    : 'https://your-production-api.com',
  TIMEOUT: 10000,
  RETRY_ATTEMPTS: 3,
} as const;

// Navigation Configuration
export const NAVIGATION_CONFIG = {
  ANIMATION_DURATION: 300,
  HEADER_HEIGHT: 60,
  TAB_BAR_HEIGHT: 80,
} as const;




