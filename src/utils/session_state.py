from typing import Dict, Any

class SessionStateManager:
    def __init__(self):
        self.store: Dict[str, Dict[str, Any]] = {}

    def init_session(self, session_id: str):
        self.store.setdefault(session_id, {"history": [], "analysis": [], "patches": []})

    def append(self, session_id: str, key: str, value: Any):
        self.init_session(session_id)
        self.store[session_id]["history"].append({key: value})

    def get(self, session_id: str):
        return self.store.get(session_id, {})

    def clear(self, session_id: str):
        if session_id in self.store:
            del self.store[session_id]

state_manager = SessionStateManager()
