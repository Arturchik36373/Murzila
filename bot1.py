from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import BufferedInputFile, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

API_TOKEN = '7482863441:AAHcTxp7DZSCZ5bodD5-hQ2uhPXXJqFxUNg'  # Замените на ваш токен

# Настройка логирования
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    # Проверяем тип чата
    if message.chat.type != 'private':
        return

    logger.info(f"Получена команда /start от {message.from_user.first_name}")

    # Текст сообщения
    message_text = "Привет! Добро пожаловать в Murzik Kombat 🐈‍⬛. Жми кнопку чтобы начать!"

    # Создаем кнопку "Играть" с WebApp
    web_app_info = WebAppInfo(url="https://murzik-combat.netlify.app")
    keyboard_button = InlineKeyboardButton(text="Играть", web_app=web_app_info)

    # Создаем клавиатуру с этой кнопкой
    reply_markup = InlineKeyboardMarkup(inline_keyboard=[[keyboard_button]])

    # Отправляем сообщение с кнопкой
    await message.answer(message_text, reply_markup=reply_markup)
    logger.info("Отправлен ответ на команду /start")


@dp.message(Command("murzik"))
async def send_meow(message: types.Message):
    logger.info(f"Получена команда /murzik от {message.from_user.first_name}")

    # Отправка голосового сообщения
    voice_path = "Meow1.ogg"
    with open(voice_path, 'rb') as voice_file:
        voice = BufferedInputFile(voice_file.read(), filename="Meow1.ogg")
        await message.answer_voice(voice)

    logger.info("Отправлено голосовое сообщение в ответ на команду /murzik")

@dp.message(Command("skazka"))
async def send_skazka(message: types.Message):
    logger.info(f"Получена команда /skazka от {message.from_user.first_name}")

    # Отправка голосового сообщения
    voice_path = "skazka.ogg"
    with open(voice_path, 'rb') as voice_file:
        voice = BufferedInputFile(voice_file.read(), filename="skazka.ogg")
        await message.answer_voice(voice)

    logger.info("Отправлено голосовое сообщение в ответ на команду /skazka")

if __name__ == '__main__':
    logger.info("Бот запущен. Нажмите Ctrl+C для завершения.")
    dp.run_polling(bot)
