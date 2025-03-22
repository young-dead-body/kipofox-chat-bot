from telegram import Update
from telegram.ext import ContextTypes

from src.handlers.content.processor import ContentProcessor
from src.services.storage.json_storage import JsonStorage
from src.utils.formatters import UserInfoFormatter


class MessageForwarder:
    def __init__(self):
        self.storage = JsonStorage()
        self.processor = ContentProcessor()
        self.formatter = UserInfoFormatter()

    async def forward(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            blogger_id = self.storage.load()

            print(f"Blogger ID from storage: {blogger_id}")
            print(f"Message from: {update.effective_chat.id}")

            if not blogger_id:
                print("❌ Blogger not registered")
                return

            if update.effective_chat.id == blogger_id:
                print("⚠️ Message from blogger, ignoring")
                return

            user = update.effective_user
            message = update.effective_message

            if not message:
                print("❌ Empty message received")
                return

            user_info = self.formatter.format(user)
            content_type, content = self.processor.process(message)

            full_message = (
                "🔔 Новое сообщение от подписчика:\n\n"
                f"{user_info}\n\n{content_type}\n📨 Сообщение: {content}"
            )

            print(f"Forwarding message to {blogger_id}: {full_message}")
            await context.bot.send_message(chat_id=blogger_id, text=full_message)

        except Exception as e:
            print(f"🔥 Forwarding error: {str(e)}")