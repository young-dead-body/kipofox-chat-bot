from abc import ABC, abstractmethod


class BaseStorage(ABC):
    @abstractmethod
    def load(self) -> int | None: ...

    @abstractmethod
    def save(self, chat_id: int) -> bool: ...