import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot('6320657267:AAENWFSec4FPHidRGbY2043BL0xFnvqojEg')


# Функция для получения chat_id
def get_chat_id():
    # Получаем список обновлений
    updates = bot.get_updates()

    # Проверяем, есть ли новые обновления
    if len(updates) > 0:
        # Берем последнее обновление
        last_update = updates[-1]

        # Получаем chat_id из обновления
        chat_id = last_update.message.chat.id

        return chat_id

    return None


# Вызываем функцию для получения chat_id
chat_id = get_chat_id()

# Выводим chat_id, если он был успешно получен
if chat_id:
    print("Chat ID:", chat_id)
else:
    print("Chat ID не найден")