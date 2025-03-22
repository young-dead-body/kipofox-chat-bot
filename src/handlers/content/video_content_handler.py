from src.handlers.content.base_content_handler import BaseContentHandler


class VideoContentHandler(BaseContentHandler):
    def handle(self, message) -> tuple[str, str]:
        return "🎥 Видео", message.caption or "Без описания"