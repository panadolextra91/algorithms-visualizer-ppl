// API Client Configuration
import { SERVER_BASE_URL } from '@/config/api';

const API_BASE_URL = __DEV__ 
  ? SERVER_BASE_URL
  : 'https://your-production-api.com';

export interface ApiResponse {
  status: 'success' | 'error';
  type?: string;
  message?: string;
  algorithm?: string;
  step?: number;
  data?: {
    array?: number[];
    highlighted_indices?: number[];
    sorted_indices?: number[];
  };
  explanation?: string;
  options?: { id: string; label: string }[];
  grid_size?: { rows: number; cols: number };
}

export interface CommandRequest {
  sessionId: string;
  command: string;
}

class ApiClient {
  private baseURL: string;

  constructor(baseURL: string = API_BASE_URL) {
    this.baseURL = baseURL;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseURL}${endpoint}`;
    
    const defaultHeaders = {
      'Content-Type': 'application/json',
    };

    try {
      const response = await fetch(url, {
        ...options,
        headers: {
          ...defaultHeaders,
          ...options.headers,
        },
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
      }

      const data = await response.json();
      return data as T;
    } catch (error: any) {
      console.error('API request failed:', error);
      
      // Provide user-friendly error messages
      if (error.message?.includes('Network request failed') || error.message?.includes('Failed to fetch')) {
        throw new Error('Cannot connect to server. Make sure the server is running on port 8069.');
      }
      
      throw error;
    }
  }

  async getGreeting(): Promise<ApiResponse> {
    return this.request<ApiResponse>('/greeting', {
      method: 'GET',
    });
  }

  async sendCommand(sessionId: string, command: string): Promise<ApiResponse> {
    return this.request<ApiResponse>('/command', {
      method: 'POST',
      body: JSON.stringify({
        sessionId,
        command,
      }),
    });
  }

  async healthCheck(): Promise<{ status: string; message: string }> {
    return this.request<{ status: string; message: string }>('/', {
      method: 'GET',
    });
  }
}

export default new ApiClient();
