# src/memory/session_service.py
class SessionService:
    """Lightweight in-memory session for current interaction."""
    def __init__(self):
        self._sessions = {}

    def create_session(self, session_id):
        self._sessions[session_id] = {}
        return session_id

    def set(self, session_id, key, value):
        s = self._sessions.setdefault(session_id, {})
        s[key] = value

    def get(self, session_id, key, default=None):
        return self._sessions.get(session_id, {}).get(key, default)

    def clear(self, session_id):
        if session_id in self._sessions:
            del self._sessions[session_id]
