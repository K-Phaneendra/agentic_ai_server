class ConversationMemory:
    def __init__(self):
        self._store = {}

    def get(self, session_id: str):
        return self._store.get(session_id, [])

    def append(self, session_id: str, message: str):
        self._store.setdefault(session_id, []).append(message)
