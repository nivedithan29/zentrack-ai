# Session Service (placeholder)
class SessionService:
    def __init__(self):
        self.session = {}

    def set(self, key, value):
        self.session[key] = value

    def get(self, key):
        return self.session.get(key)
