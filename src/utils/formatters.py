from typing import Optional

from telegram import User


class UserInfoFormatter:
    @staticmethod
    def format(user: Optional[User]) -> str:
        return f"""
        🆔 ID: {user.id}
        👤 Name: {user.first_name}
        📝 Last Name: {user.last_name}
        🌐 Username: @{user.username}
        """