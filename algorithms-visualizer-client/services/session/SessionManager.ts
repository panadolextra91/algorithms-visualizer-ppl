// Session Manager Service
const SESSION_ID_KEY = 'sessionId';

class SessionManager {
  private sessionId: string | null = null;

  async getSessionId(): Promise<string> {
    if (!this.sessionId) {
      // For now, generate a new session ID each time
      // TODO: Add AsyncStorage persistence when available
      this.sessionId = `anon_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }
    return this.sessionId;
  }

  async clearSession(): Promise<void> {
    this.sessionId = null;
  }
}

export default new SessionManager();