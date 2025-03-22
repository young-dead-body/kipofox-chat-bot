from telegram.ext import Application, ContextTypes
from src.config.config_loader import ConfigLoader
from src.handlers.handlers import Handlers


class BotApplication:
    def __init__(self):
        self.config = ConfigLoader.load()
        self.app = Application.builder().token(self.config.token).build()
        self.app.add_error_handler(self.error_handler)
        self.handlers = Handlers()

    @staticmethod
    async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
        print(f"⚠️ Ошибка: {context.error}")
        if update and hasattr(update, 'message'):
            await update.message.reply_text("😢 Произошла ошибка, попробуйте позже")

    def setup_handlers(self):
        """Регистрируем все обработчики из роутера."""
        for handler in self.handlers.get_registered_handlers():
            self.app.add_handler(handler)

    def run(self):
        self.setup_handlers()
        print("Bot started...")
        self.app.run_polling()