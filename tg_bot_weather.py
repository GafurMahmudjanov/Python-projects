import requests
import datetime
from config import open_weather_token,token_bot
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=token_bot)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    await message.answer('Привет) Напиши мне название города и я пришлю тебе прогноз погоды!')


@dp.message_handler()
async def get_weather(massage: types.Message):

    weather_conditions = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'
    }


    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={massage.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        weather_description = data['weather'][0]['main']

        if weather_description in weather_conditions:
            wd = weather_conditions[weather_description]
        else:
            wd = 'Посмотри в окно я не понимаю, что там!'


        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        await massage.reply(f'***** {today} *****\n'
              f'Погода в городе: {city}\nТемпература: {cur_weather} °C {wd}\n'
              f'Влажность: {humidity}\nДавление: {pressure}\n'
              f'Скорость ветра: {wind} M.c\nВосход coлнца: {sunrise_timestamp}\n'
              f'Закад солнца: {sunset_timestamp}\n'
              f'Продолжительность дня: {length_of_the_day}\n'
              f'Have a greate day dear!')

    except:
        await  massage.reply('\U00002620 Упс, что-то пошло не так, проверьте название города.\U00002620 ')





if __name__ == '__main__':
    executor.start_polling(dp)

