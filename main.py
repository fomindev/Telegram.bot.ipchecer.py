import telebot
import requests
import datetime
from config import token_bot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token_bot)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(
        f"✋ Привет {message.from_user.first_name}({message.from_user.id}), я бот для показа информации о IP-адрессе! 🤯\n\n"
        f"❕❕ [Внимание] ❕❕\n"
        f"✍️ Напиши мне IP Адрес и я выведу информацию о нём! 🍃\n"
        f"❔ Никакого 'Слеша'(Пример: 123.456.78.90 | Далее следует вывод информации со стороны бота)❔\n"
        f"📓 Мои команды: /start | /info 📓"
        )
    #await bot.send_photo(message.chat.id, types.InputFile('image/info.png')) # Отправка фотографии из папки

@dp.message_handler(commands=["info"])
async def info_command(message):
    await bot.send_message(message.chat.id, 'Средства связи с разработчиком \n↳ [VK](ССылка на вк) ✅\n    ↳ [Telegram](https://t.me/username) ✅\n        ↳ [GitHub](https://github.com/username) ✅\n            ↳ [Discord](https://discordapp.com/users/userid) ✅',parse_mode='Markdown')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://ip-api.com/json/{message.text}"
        )
        data = r.json()

        status = data['status']
        country = data['country']
        countryCode = data['countryCode']
        region = data['region']
        regionName = data['regionName']
        city = data['city']
        lat = data['lat']
        lon = data['lon']
        timezone = data['timezone']
        org = data['org']
        query = data['query']




        await message.reply(
            f"__________🕙 {datetime.datetime.now().strftime('%d-%m-%Y | %H:%M')} 🕙__________\n"
            f"🖥 IP: {query} 🖥\n"
            f"📉 Статус: {status} 📉\n"
            f"🏳️ Страна: {country} 🏳️\n"
            f"🔑 Код Страны: {countryCode} 🔑\n"
            f"🏛 Регион: {region} 🏛\n"
            f"🏛 Название региона: {regionName} 🏛\n"
            f"🏙 Город: {city} 🏙\n"
            f"🗺 Широта: {lat} 🗺 | 🗺 Долгота: {lon} 🗺\n"
            f"🕙 Временая зона: {timezone} 🕙\n"
            f"🌍 Провайдер: {org} 🌍\n"
            f"__________created by Vinograd__________\n"
        )
        await message.answer_sticker(r"CAACAgIAAxkBAAEERydiP1gO_1poxHRAFTbRBqMlsMGm-gACnQgAAhuWUUp-eUVnu4Mh8iME")

    except:
        await message.reply("[❌ Ошибка! ❌] Проверьте правильность IP Адресса")

if __name__ == '__main__':
    executor.start_polling(dp)
