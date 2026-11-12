"""Модуль аутентификации."""


class AuthService:
    """Сервис аутентификации пользователей."""

    def __init__(self):
        self.users = {}

    def register(self, username: str, password: str) -> bool:
        """Регистрация нового пользователя."""
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def login(self, username: str, password: str) -> bool:
        """Вход пользователя."""
        return self.users.get(username) == password