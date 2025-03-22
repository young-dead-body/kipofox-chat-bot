from src.handlers.content.base_content_handler import BaseContentHandler
from src.handlers.content.default_content_handler import DefaultContentHandler
from src.handlers.content.photo_content_handler import PhotoContentHandler
from src.handlers.content.text_content_handler import TextContentHandler
from src.handlers.content.video_content_handler import VideoContentHandler


class ContentProcessor:
    def __init__(self):
        self.handlers = {
            'text': TextContentHandler(),
            'photo': PhotoContentHandler(),
            'video': VideoContentHandler()
        }

    def process(self, message) -> tuple[str, str]:
        handler = self.detect_handler(message)
        return handler.handle(message)

    def detect_handler(self, message) -> BaseContentHandler:
        if message.text:
            return self.handlers['text']
        if message.photo:
            return self.handlers['photo']
        if message.video:
            return self.handlers['video']
        return DefaultContentHandler()