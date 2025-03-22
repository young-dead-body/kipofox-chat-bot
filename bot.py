from src.application import BotApplication

if __name__ == "__main__":
    try:
        bot = BotApplication()
        bot.run()
    except Exception as e:
        print(f"Error: {str(e)}")