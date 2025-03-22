from src.handlers.content.base_content_handler import BaseContentHandler


class TextContentHandler(BaseContentHandler):
    def handle(self, message) -> tuple[str, str]:
        return "📝 Текст", message.text
