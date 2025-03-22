import json
from pathlib import Path
from typing import Optional, Any
import io

from src.services.storage.base_storage import BaseStorage


class JsonStorage(BaseStorage):
    def __init__(self, filename: str = 'blogger_id.json'):
        self.file_path = Path(filename)

    def load(self) -> Optional[int]:
        try:
            with self.file_path.open('r') as f:
                data: dict[str, Any] = json.load(f)
                return data.get('chat_id')
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def save(self, chat_id: int) -> bool:
        try:
            with self.file_path.open('wb') as f:
                wrapped_f = io.TextIOWrapper(f, encoding='utf-8')
                json.dump({'chat_id': chat_id}, wrapped_f, ensure_ascii=False)
            return True
        except (IOError, TypeError) as e:
            print(f"Ошибка сохранения: {str(e)}")
            return False