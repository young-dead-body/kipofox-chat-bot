from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from src.services.forwarding import MessageForwarder

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await MessageForwarder().forward(update, context)

def get_message_handlers():
    return [MessageHandler(filters.ALL & ~filters.COMMAND, handle_message)]