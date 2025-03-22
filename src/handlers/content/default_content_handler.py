from src.handlers.content.base_content_handler import BaseContentHandler


class DefaultContentHandler(BaseContentHandler):
    def handle(self, message) -> tuple[str, str]:
        return "🔍 Неизвестный тип", "Содержимое недоступно"