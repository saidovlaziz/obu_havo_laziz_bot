"""
dastur:Obu-havo bot
Muallif:
Saidov Lazizjon
"""

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import requests

#==================================
# Sozlamalar- bu yerga malumotlaringizni kiriting
#==================================
Token="8335867919:AAGIUZ_DXgQ3tBYMdrlrY59h6MxNYafgRMM"
API_KEY="ad1a7110736ebbc4cfb9c2e68694d6a2"

#==================================
#Bot va Dispatcher
#==================================

bot=Bot(token=Token)
dp=Dispatcher()

#==================================
#Buyruqlar
#==================================

@dp.message(Command("start"))
async def start(message):
    """Bot ishga tushganda"""
    await message.answer(
        "Assalomu alaykum 👋\n"
        "Men obu-havo botiman \n\n"
        "Buyruqlar: \n"
        "/weather shahar_nomi"
        )

@dp.message(Command("weather"))
async def weather(message):
    """Obu-havo malumoti"""

shahar= message.text.split()[1] 

url=f"http://api.openweathermap.org/data/2.5/weather"
params={
    'q':shahar,
    'appid':API_KEY,
    'units':'metric',
    'lang':'uz'

}

javob = requests.get(url, params=params)
malumot=javob.json()

harorat=malumot['main']['temp']
holat=malumot['weather'][0]['description']
@dp.message(Command("weather"))
async def weather(message):
    """Obu-havo malumoti"""
    await message.answer(
             f"🌍{shahar}\n"
             f"🌡Harorat:{harorat}C\n"
             f"☁️Holat:{holat}"
    ) 

#====================================
#Botni ishga tushirish
#====================================

async def main():
    await dp.start_polling(bot)

if __name__ =="__main__":
     asyncio.run(main())