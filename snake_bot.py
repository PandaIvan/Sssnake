import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.ext import CallbackContext

# Вставьте ваш токен бота сюда
TOKEN = '7369063766:AAHghLSmYzkvVt4Xwbd_sD3jmh3rX-IVov0'

# Логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Стартовая команда
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Это игра Змейка. Нажми /play, чтобы начать играть.")

# Команда для запуска игры
def play(update: Update, context: CallbackContext):
    # Отправляем HTML файл с игрой
    update.message.reply_text("Для запуска игры, перейдите по ссылке:")
    update.message.reply_text("https://ваш-сайт-с-игрой/index.html")

# Обработка ошибок
def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Создание Updater и передача ему токена бота
    updater = Updater(TOKEN, use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Команды
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("play", play))

    # Логирование ошибок
    dp.add_error_handler(error)

    # Запуск бота
    updater.start_polling()

    # Работа до принудительной остановки
    updater.idle()

if __name__ == '__main__':
    main()