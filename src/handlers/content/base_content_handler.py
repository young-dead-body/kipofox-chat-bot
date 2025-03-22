from abc import abstractmethod, ABC


class BaseContentHandler(ABC):
    @abstractmethod
    def handle(self, message) -> tuple[str, str]:
        pass
