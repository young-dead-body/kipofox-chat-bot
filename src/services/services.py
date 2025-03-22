# В registration.py
from src.services.storage.json_storage import JsonStorage


class RegistrationService:
    def __init__(self, storage=JsonStorage()):
        self.storage = storage

    async def register(self, chat_id: int) -> str:
        try:
            existing_id = self.storage.load()

            if existing_id:
                return "⚠️ Вы уже зарегистрированы!" if existing_id == chat_id else "🚫 Блогер уже существует!"

            if self.storage.save(chat_id):
                return "✅ Регистрация успешна!"

            return "❌ Ошибка сохранения данных"

        except Exception as e:
            print(f"Registration error: {str(e)}")
            return "⚠️ Ошибка сервера, попробуйте позже"