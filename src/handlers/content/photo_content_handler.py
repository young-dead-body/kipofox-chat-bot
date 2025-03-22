from src.handlers.content.base_content_handler import BaseContentHandler


class PhotoContentHandler(BaseContentHandler):
    def handle(self, message) -> tuple[str, str]:
        return "🖼 Фото", message.caption or "Без описания"
