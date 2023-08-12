import logging  # Импортируем модуль logging
from telegram import Update  # Импортируем класс Update из модуля telegram
from telegram.ext import Updater, CommandHandler, CallbackContext  # Импортируем различные классы из модуля telegram.ext
import praw  # Импортируем модуль praw для доступа к API Reddit

# Настраиваем библиотеку для ведения журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(name)

# Создаем экземпляр класса Reddit
reddit = praw.Reddit(
    client_id="ВАШ_ID_КЛИЕНТА_REDDIT",  # Замените на фактический ID клиента Reddit
    client_secret="ВАШ_СЕКРЕТНЫЙ_КОД_REDDIT",  # Замените на фактический секретный код Reddit
    user_agent="ВАШ_USER_AGENT_REDDIT",  # Замените на фактический user agent Reddit
)

# Функция для обработки команды start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который ищет бесплатные игры Steam на Reddit.')

# Функция для обработки команды search
def search(update: Update, context: CallbackContext) -> None:
    for submission in reddit.subreddit("FreeGameFindings").new(limit=10):
        if "steam" in submission.title.lower():
            update.message.reply_text(submission.url)

# Главная функция для запуска бота
def main() -> None:
    updater = Updater("ВАШ_ТОКЕН_ТЕЛЕГРАММА")  # Замените на фактический токен бота Telegram

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search))

    updater.start_polling()

    updater.idle()

if name == 'main':
    main()