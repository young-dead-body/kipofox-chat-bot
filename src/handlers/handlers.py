from src.handlers.commands import get_command_handlers
from src.handlers.messages import get_message_handlers
from src.routers.router import Router

class Handlers:
    def __init__(self, router=None):
        """
        Инициализация класса Handlers.
        Если router не передан, создается новый экземпляр Router.
        """
        self.router = router if router is not None else Router()
        # Регистрируем обработчики при инициализации
        self.registration()

    def registration(self):
        """
        Регистрирует все обработчики (команды и сообщения) в router.
        """
        # Добавляем обработчики команд
        self.router.add_handlers(get_command_handlers())
        # Добавляем обработчики сообщений
        self.router.add_handlers(get_message_handlers())

    def get_registered_handlers(self):
        """
        Возвращает все зарегистрированные обработчики.
        """
        return self.router.get_handlers()