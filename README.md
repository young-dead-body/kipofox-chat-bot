# Telegram Blogger Assistant Bot

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-20.0+-blue)](https://core.telegram.org/bots/api)

Telegram бот для управления сообщениями подписчиков. Бот позволяет зарегистрировать администратора (блогера) и пересылать ему сообщения от других пользователей с подробной информацией об отправителе.

## Основные функции

- 📝 Регистрация администратора (блогера)
- 🔔 Пересылка сообщений от подписчиков
- 📊 Информация о пользователях (ID, имя, фамилия, username)
- 🖼 Поддержка текстовых сообщений, фото и видео
- ⚙️ Простая настройка через .env файл

## Установка и настройка

### Требования

- Python 3.9 или выше
- Учетная запись Telegram
- Созданный бот через [BotFather](https://core.telegram.org/bots#botfather)

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/telegram-blogger-bot.git
   cd telegram-blogger-bot
   ```
   
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл .env в корне проекта и добавьте токен бота:

   ```bash
   TOKEN=ваш_токен_бота
   ```
   
### Запуск

#### Запустите бота:

   ```bash
      python bot.py
   ```

### Использование
1. Зарегистрируйте администратора:

   - Отправьте команду /administratorRegistration в чат с ботом

2. После регистрации:

   - Все сообщения от других пользователей будут пересылаться администратору

   - Сообщения содержат информацию об отправителе и тип контента

### Структура проекта

```
   project/
      ├── src/
      |      ├── config/            # Конфигурационные файлы
      |      ├── handlers/          # Обработчики
      |      ├── routers/           # "Роутеры"
      |      ├── services/          # Сервисы
      |      ├── utils/             # Утилиты
      |      └── application.py     # Приложение
      └── bot.py 
```

### Примеры использования
#### Регистрация администратора

```
Пользователь: /administratorRegistration
Бот: ✅ Вы успешно зарегистрированы как блогер!
```

### Получение сообщения от подписчика

```
Бот (администратору):
🔔 Новое сообщение от подписчика:

   🆔 ID: 123456789
   👤 Имя: Иван
   📝 Фамилия: Иванов
   🌐 Username: @ivanov

📝 Текст
📨 Сообщение: Привет! Как дела?
```

## Авторы

<a href="https://t.me/sssnakeMK" style="text-decoration: none; color: #2E86C1; font-weight: bold; font-size: 1.1em;">
  <img src="https://img.icons8.com/color/48/000000/telegram-app--v1.png" alt="Telegram" width="20" height="20" style="vertical-align: middle; margin-right: 8px;"/>
  Михаил Кравчук (MiKra)
</a>