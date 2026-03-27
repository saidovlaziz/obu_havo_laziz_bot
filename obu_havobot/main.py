"""
dastur:Obu-havo bot
Muallif:
Saidov Lazizjon
"""

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import requests

# ==================================
# Sozlamalar
# ==================================
Token = "8335867919:AAGIUZ_DXgQ3tBYMdrlrY59h6MxNYafgRMM"
API_KEY = "ad1a7110736ebbc4cfb9c2e68694d6a2"

bot = Bot(token=Token)
dp = Dispatcher()

# ==================================
# Buyruqlar
# ==================================

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Assalomu alaykum 👋\n"
        "Men obu-havo botiman \n\n"
        "Buyruqlar:\n"
        "/weather shahar_nomi - Masalan: /weather Toshkent\n"
        "/help - yordam"
    )

@dp.message(Command("weather"))
async def get_weather(message: types.Message):
    try:
        matn = message.text.split()
        if len(matn) < 2:
            await message.answer("❌ Iltimos, shahar nomini kiriting.\nMisol: /weather Toshkent")
            return

        shahar = "".join(matn[1:])
        url = "http://api.openweathermap.org/data/2.5/weather" # URL tuzatildi

        params = {
            'q': shahar,
            'appid': API_KEY,
            'units': 'metric', # 'metric' tuzatildi
            'lang': 'uz'
        }

        javob = requests.get(url, params=params)

        if javob.status_code != 200:
            if javob.status_code == 404: 
                await message.answer(f"❌ '{shahar}' nomli shahar topilmadi.")
            else:
                await message.answer(f"Xatolik yuz berdi. Kod: {javob.status_code}")
            return
  
        malumot = javob.json()
        harorat = malumot['main']['temp']
        his_etilayotgan = malumot['main']['feels_like']
        bosim = malumot['main']['pressure']
        namlik = malumot['main']['humidity']
        holat = malumot['weather'][0]['description']
        shamol = malumot['wind']['speed']
        bulut = malumot['clouds']['all']
        mamlakat = malumot['sys']['country'] # 'country' tuzatildi

        await message.answer(
             f"🌍 <b>{shahar.capitalize()}, {mamlakat}</b>\n"
             f"----------------------------\n"
             f"🌡 <b>Harorat:</b> {harorat:.1f}°C\n"
             f"🤔 <b>His etilayotgan:</b> {his_etilayotgan:.1f}°C\n"
             f"💹 <b>Bosim:</b> {bosim} hPa\n"
             f"💧 <b>Namlik:</b> {namlik}%\n"
             f"☁️ <b>Bulutlilik:</b> {bulut}%\n"
             f"💨 <b>Shamol:</b> {shamol} m/s\n"
             f"📃 <b>Tavsif:</b> {holat.capitalize()}",
             parse_mode="HTML"
        ) 
    except Exception as e:
        await message.answer(f"Xatolik: {str(e)}")

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("<b>Shahar nomini /weather buyrug'idan so'ng yozing.</b>\nMisol: /weather Chinoz", parse_mode="HTML")

# ====================================
# Botni ishga tushirish
# ====================================

async def main():
    print("Dastur ishga tushdi...")
    print(f"Bot token: {Token[:10]}...")
    await dp.start_polling(bot)

if __name__ == "__main__": # Bu qator tuzatildi
    asyncio.run(main()) # Bu qator tuzatildi