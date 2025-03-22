from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from src.services.services import RegistrationService


async def handle_registration(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    if not update.message:
        return

    service = RegistrationService()
    response = await service.register(update.effective_chat.id)
    response = response or "⚠️ Произошла неизвестная ошибка"

    await update.message.reply_text(response)


def get_command_handlers():
    return [CommandHandler("administratorRegistration", handle_registration)]