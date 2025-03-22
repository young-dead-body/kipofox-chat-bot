class Router:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        """Добавляет один обработчик."""
        self.handlers.append(handler)

    def add_handlers(self, handlers):
        """Добавляет несколько обработчиков."""
        self.handlers.extend(handlers)

    def get_handlers(self):
        """Возвращает все обработчики."""
        return self.handlers
