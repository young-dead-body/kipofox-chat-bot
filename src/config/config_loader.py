from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()

@dataclass
class BotConfig:
    token: str

class ConfigLoader:
    @staticmethod
    def load() -> BotConfig:
        token = os.getenv("TOKEN")
        if not token:
            raise ValueError("Token not found")
        return BotConfig(token=token)