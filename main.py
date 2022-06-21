from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message,CallbackQuery
from button import *
logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def kirish(message: types.Message):
    await message.reply("Assalomu alaykum\nBotimizga xush kelibsiz\nIltimos tilni tanlang!",reply_markup = til)

@dp.callback_query_handler(text = "uz")
async def UZB(call:CallbackQuery):
    await call.message.answer("Assalomu alaykum\nTelefon bozorga xush kelibsiz\nIltimos telefon turini tanlang!",reply_markup = tur)

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""IPONE """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@dp.callback_query_handler(text = "ipone")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/iponmenu.jpg','rb'),
        caption = "IPONE TURINI TANLANG!",reply_markup = ipon_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "max")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO MAX TURINI TANLANG!",reply_markup = promax_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "max13")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/13promax.jpeg','rb'),
        caption = """Hurmatli mijoznsiz tanlagan IPONE 13 PRO MAX
Cтепень защиты: IP68
Процессор: Apple A15 Bionic
Версия ОС: iOS 15
Стандарт связи: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Материал корпуса: металл и стекло
Вес: 238 г
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2778x1284
Тип экрана: OLED
Диагональ экрана: 6.7"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Apple
Xozirda narxi:13 310 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back)
    await call.message.delete()
@dp.callback_query_handler(text = "a1")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "a2")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "a3")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "a4")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "r1")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r2")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r3")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r4")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()
@dp.message_handler(content_types = ['contact'])
async def asa(message):
    username = message.from_user.username
    telefon = message.contact['phone_number']
    # await bot.send_message(chat_id = ,text = "Username:{username}\nTelefon raqam:{telefon}")
    await message.answer("<b>Iltimos joylashuvni jo'nating</b>",parse_mode = 'HTML',reply_markup = joy)

@dp.message_handler(content_types = ['location'])
async def asa(message):
    await message.reply("<b>Hurmatli mijoz siz bilan tez orada aloqaga chiqamiz</b>",parse_mode = 'HTML',reply_markup = um_nazad)
@dp.callback_query_handler(text = "max12")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/12promax.jpeg','rb'),
        caption = """Hurmatli mijoz\nsiz tanlagan IPONE 12 PRO MAX
Частота обновления экрана: 60 Гц
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Процессор: Apple A14 Bionic
Версия ОС: iOS 14
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Вес: 226 г
Емкость аккумулятора: 3687 мА⋅ч
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2778x1284
Тип экрана: OLED
Диагональ экрана: 6.7"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Apple
Hozirda narxi:9 524 000

Iltimos xotira turini tanlang👇👇👇 """,reply_markup = back100)
    await call.message.delete()

@dp.callback_query_handler(text = "a6")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi1)
    await call.message.delete()

@dp.callback_query_handler(text = "a7")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi1)
    await call.message.delete()

@dp.callback_query_handler(text = "a8")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi1)
    await call.message.delete()

@dp.callback_query_handler(text = "r5")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r6")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r7")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r8")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "max11")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/11promax.jpeg','rb'),
        caption  = """"Hurmatli mijoz siz tanlagan
IPONE 11 PRO MAX
Частота обновления экрана: 60 Гц
Материал корпуса: металл и стекло
Процессор: Apple A13 Bionic
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Тип экрана: OLED
Версия ОС: iOS 13
Разрешение экрана: 2688x1242
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
NFC: Есть
Стандарт Bluetooth: 5.0
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Вес: 226 г
Емкость аккумулятора: 3969 мА⋅ч
Диагональ экрана: 6.5"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple
Hozirda narxi:8 210 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back101)
    await call.message.delete()

@dp.callback_query_handler(text = "a9")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi2)
    await call.message.delete()

@dp.callback_query_handler(text = "a10")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi2)
    await call.message.delete()

@dp.callback_query_handler(text = "a11")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi2)
    await call.message.delete()

@dp.callback_query_handler(text = "a12")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi2)
    await call.message.delete()

@dp.callback_query_handler(text = "r9")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r10")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r11")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r12")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "maxs")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/xsmax.jpeg','rb'),
        caption = """Hurmatli mijo siz tanlagan IPONE XS MAX
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Apple A12 Bionic
Версия ОС: iOS 12
NFC: Есть
Тип экрана: OLED
Разрешение экрана: 2688x1242
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Емкость аккумулятора: 3174 мА⋅ч
Фронтальная камера: 7 МП
Основная камера: 12 МП, 12 МП
Вес: 208 г
Диагональ экрана: 6.5"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple
Hozirda narxi:6 145 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back102)
    await call.message.delete()

@dp.callback_query_handler(text = "a17")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi3)
    await call.message.delete()

@dp.callback_query_handler(text = "a18")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi3)
    await call.message.delete()
@dp.callback_query_handler(text = "a19")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi3)
    await call.message.delete()

@dp.callback_query_handler(text = "a20")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi3)
    await call.message.delete()

@dp.callback_query_handler(text = "r13")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r14")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r15")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "r16")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "ort")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO TURINI TANLANG!",reply_markup = pro_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "pro13")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/13pro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 13 PRO
Cтепень защиты: IP68
Стандарт Bluetooth: 5.0
Процессор: Apple A15 Bionic
Версия ОС: iOS 15
Стандарт связи: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Материал корпуса: металл и стекло
Вес: 203 г
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2532x1170
Тип экрана: OLED
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Apple
Hozirda narxi:

Iltimos xotira turini tanlang 👇👇👇""",reply_markup = back4)
    await call.message.delete()

@dp.callback_query_handler(text = "b1")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi4)
    await call.message.delete()

@dp.callback_query_handler(text = "b2")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi4)
    await call.message.delete()

@dp.callback_query_handler(text = "b3")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi4)
    await call.message.delete()

@dp.callback_query_handler(text = "b4")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi4)
    await call.message.delete()

@dp.callback_query_handler(text = "c1")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c2")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c3")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c4")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "pro12")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/12pro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 12 PRO
Частота обновления экрана: 60 Гц
Тип экрана: OLED
Материал корпуса: металл и стекло
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: iOS 14
NFC: Есть
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Стандарт Bluetooth: 5.0
Емкость аккумулятора: 2815 мА⋅ч
Разрешение экрана: 2532x1170
Процессор: Apple A14 Bionic
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП
Вес: 187 г
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Apple
 Hozirda narxi ?

Iltimos xotira turini tanlang 👇👇👇""",reply_markup = back400)
    await call.message.delete()

@dp.callback_query_handler(text = "b5")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi5)
    await call.message.delete()

@dp.callback_query_handler(text = "b6")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi5)
    await call.message.delete()

@dp.callback_query_handler(text = "b7")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi5)
    await call.message.delete()

@dp.callback_query_handler(text = "c5")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c6")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c7")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c8")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "pro11")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/11pro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 11 PRO
Частота обновления экрана: 60 Гц
Разрешение экрана: 2436x1125
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Apple A13 Bionic
Версия ОС: iOS 13
Тип экрана: OLED
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
NFC: Есть
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Вес: 188 г
Емкость аккумулятора: 3190 мА⋅ч
Диагональ экрана: 5.8"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple
Hozirda narxi ?

Iltimos xotira turini tanlang 👇👇👇""",reply_markup = back401)
    await call.message.delete()
@dp.callback_query_handler(text = "b8")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi6)
    await call.message.delete()

@dp.callback_query_handler(text = "b9")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi6)
    await call.message.delete()

@dp.callback_query_handler(text = "b10")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi6)
    await call.message.delete()

@dp.callback_query_handler(text = "b11")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi6)
    await call.message.delete()

@dp.callback_query_handler(text = "c9")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c10")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c11")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c12")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "proxs")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/xs.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE XS
Частота обновления экрана: 60 Гц
Процессор: Apple A12 Bionic
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: iOS 12
NFC: Есть
Тип экрана: OLED
Разрешение экрана: 2436x1125
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Фронтальная камера: 7 МП
Основная камера: 12 МП, 12 МП
Вес: 177 г
Емкость аккумулятора: 2658 мА⋅ч
Диагональ экрана: 5.8"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple Hozirda narxi ?""",reply_markup = back402)
    await call.message.delete()

@dp.callback_query_handler(text = "b13")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi7)
    await call.message.delete()

@dp.callback_query_handler(text = "b14")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi7)
    await call.message.delete()

@dp.callback_query_handler(text = "b15")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi7)
    await call.message.delete()

@dp.callback_query_handler(text = "b16")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi7)
    await call.message.delete()

@dp.callback_query_handler(text = "c13")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c14")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c15")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c16")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "proxr")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/xr.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE XR
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Apple A12 Bionic
Версия ОС: iOS 12
NFC: Есть
Тип экрана: IPS
Разрешение экрана: 1792x828
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Фронтальная камера: 7 МП
Основная камера: 12 МП
Вес: 194 г
Емкость аккумулятора: 2942 мА⋅ч
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 3 ГБ
Бренд: Apple
Hozirda narxi """,reply_markup = back403)
    await call.message.delete()

@dp.callback_query_handler(text = "b17")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi8)
    await call.message.delete()


@dp.callback_query_handler(text = "b18")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi8)
    await call.message.delete()


@dp.callback_query_handler(text = "b19")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = iphone_rangi8)
    await call.message.delete()

@dp.callback_query_handler(text = "c17")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c18")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c19")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "c20")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "kich")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE TURINI TANLANG!",reply_markup = min_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "min13")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/13.jpeg','rb'),
        caption = """Hurmatli mijoz  siz tanlagan IPONE 13
Cтепень защиты: IP68
Стандарт Bluetooth: 5.0
Процессор: Apple A15 Bionic
Версия ОС: iOS 15
Стандарт связи: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП
Материал корпуса: алюминий и стекло
Вес: 173 г
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2532x1170
Тип экрана: OLED
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple 
Hozirda narxi

Iltimos xotira turini tanlang👇👇👇 """,reply_markup = back5)
    await call.message.delete()

@dp.callback_query_handler(text = "d1")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi1)
    await call.message.delete()

@dp.callback_query_handler(text = "d2")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi1)
    await call.message.delete()

@dp.callback_query_handler(text = "d3")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi1)
    await call.message.delete()


@dp.callback_query_handler(text = "g1")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g2")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g3")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g4")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "min12")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/12.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 12
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: iOS 14
NFC: Есть
Тип экрана: OLED
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Соотношение сторон экрана: 19.5:9
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.0
Емкость аккумулятора: 2815 мА⋅ч
Разрешение экрана: 2532x1170
Объем оперативной памяти: 4 ГБ
Процессор: Apple A14 Bionic
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП
Вес: 164 г
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Бренд: Apple 
Hozirda narxi

Iltimos xotira turini tanlang👇👇👇 """,reply_markup = back500)
    await call.message.delete()

@dp.callback_query_handler(text = "d4")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi2)
    await call.message.delete()

@dp.callback_query_handler(text = "d5")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi2)
    await call.message.delete()

@dp.callback_query_handler(text = "d6")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi2)
    await call.message.delete()

@dp.callback_query_handler(text = "g5")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g6")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g7")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g8")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "min11")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/11.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 11
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Apple A13 Bionic
Версия ОС: iOS 13
Тип экрана: IPS
Разрешение экрана: 1792x828
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
NFC: Есть
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП
Вес: 194 г
Емкость аккумулятора: 3110 мА⋅ч
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple 
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back501)
    await call.message.delete()

@dp.callback_query_handler(text = "d7")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi3)
    await call.message.delete()

@dp.callback_query_handler(text = "d8")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi3)
    await call.message.delete()

@dp.callback_query_handler(text = "d9")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi3)
    await call.message.delete()

@dp.callback_query_handler(text = "g9")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g10")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g11")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g12")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "minx")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/x.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE x
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
NFC: Есть
Тип экрана: OLED
Разрешение экрана: 2436x1125
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.0
Процессор: Apple A11 Bionic
Фронтальная камера: 7 МП
Основная камера: 12 МП, 12 МП
Вес: 174 г
Емкость аккумулятора: 2716 мА⋅ч
Диагональ экрана: 5.8"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 3 ГБ
Бренд: Apple
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back502)
    await call.message.delete()

@dp.callback_query_handler(text = "d10")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi4)
    await call.message.delete()

@dp.callback_query_handler(text = "d11")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi4)
    await call.message.delete()

@dp.callback_query_handler(text = "d12")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi4)
    await call.message.delete()

@dp.callback_query_handler(text = "g13")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g14")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g15")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g16")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "min8+")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/8+.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 8+
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
NFC: Есть
Тип экрана: IPS
Соотношение сторон экрана: 16:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.0
Процессор: Apple A11 Bionic
Бренд: Apple
Объем оперативной памяти: 3 ГБ
Объем встроенной памяти: 64 ГБ
Диагональ экрана: 5.5"
Емкость аккумулятора: 2691 мА⋅ч
Вес: 202 г
Основная камера: 12 МП, 12 МП
Фронтальная камера: 7 МП
Разрешение экрана: 1920x1080 
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back503)
    await call.message.delete()

@dp.callback_query_handler(text = "d13")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi5)
    await call.message.delete()

@dp.callback_query_handler(text = "d14")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi5)
    await call.message.delete()

@dp.callback_query_handler(text = "d15")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi5)
    await call.message.delete()

@dp.callback_query_handler(text = "g17")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g18")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g19")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g20")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "min8")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/8.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 8
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
NFC: Есть
Тип экрана: IPS
Соотношение сторон экрана: 16:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 1334x750
Процессор: Apple A11 Bionic
Фронтальная камера: 7 МП
Основная камера: 12 МП
Вес: 148 г
Емкость аккумулятора: 1820 мА⋅ч
Диагональ экрана: 4.7"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 2 ГБ
Бренд: Apple 
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back504)
    await call.message.delete()

@dp.callback_query_handler(text = "d16")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi6)
    await call.message.delete()

@dp.callback_query_handler(text = "d17")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi6)
    await call.message.delete()

@dp.callback_query_handler(text = "d18")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi6)
    await call.message.delete()

@dp.callback_query_handler(text = "g21")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g22")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g23")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g24")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "min7+")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/7+.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 7+
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
Материал корпуса: алюминий и стекло
NFC: Есть
Стандарт Bluetooth: 4.2
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Процессор: Apple A10 Fusion
Версия ОС: iOS 10
Фронтальная камера: 7 МП
Основная камера: 12 МП, 12 МП
Вес: 188 г
Емкость аккумулятора: 2900 мА⋅ч
Соотношение сторон экрана: 16:9
Разрешение экрана: 1920x1080
Тип экрана: IPS
Диагональ экрана: 5.5"
Объем встроенной памяти: 32 ГБ
Объем оперативной памяти: 3 ГБ
Бренд: Apple 
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back505)
    await call.message.delete()

@dp.callback_query_handler(text = "d19")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi7)
    await call.message.delete()

@dp.callback_query_handler(text = "d20")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi7)
    await call.message.delete()

@dp.callback_query_handler(text = "d21")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi7)
    await call.message.delete()
@dp.callback_query_handler(text = "d22")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi7)
    await call.message.delete()

@dp.callback_query_handler(text = "g25")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g26")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g27")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g28")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "min7")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/7.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 7 
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
Версия ОС: iOS 10
Тип экрана: IPS
NFC: Есть
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Соотношение сторон экрана: 16:9
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 4.2
Разрешение экрана: 1334x750
Процессор: Apple A10 Fusion
Фронтальная камера: 7 МП
Основная камера: 12 МП
Вес: 138 г
Емкость аккумулятора: 1960 мА⋅ч
Диагональ экрана: 4.7"
Объем встроенной памяти: 32 ГБ
Объем оперативной памяти: 2 ГБ
Бренд: Apple
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back506)
    await call.message.delete()

@dp.callback_query_handler(text = "d23")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi8)
    await call.message.delete()

@dp.callback_query_handler(text = "d24")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi8)
    await call.message.delete()

@dp.callback_query_handler(text = "d25")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi8)
    await call.message.delete()

@dp.callback_query_handler(text = "d26")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = ihone_min_rangi8)
    await call.message.delete()

@dp.callback_query_handler(text = "g29")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g30")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g31")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "g32")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


#""""""""""""""""""""""""""""""""""""""""""""""""SAMSUNG"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@dp.callback_query_handler(text = "samsung")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/sammenu.jpeg','rb'),
        caption = "Samsung TURINI TANLANG!",reply_markup = sam_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "s")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu )
    await call.message.delete()


@dp.callback_query_handler(text = "not")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung NOT seria TURINI TANLANG!",reply_markup = not_menu )
    await call.message.delete()


@dp.callback_query_handler(text = "a")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu )
    await call.message.delete()


@dp.callback_query_handler(text = "z")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung Z seria TURINI TANLANG!",reply_markup = z_menu )
    await call.message.delete()



@dp.callback_query_handler(text = "s22u")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
    photo = open('image/s22ultra.jpeg','rb'),
    caption =  """Hurmatli mijos siz tanlagan
samsung galaxy s22 ultra
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Стандарт Bluetooth: 5.2
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Процессор: Samsung Exynos 2200
Фронтальная камера: 40 МП
Основная камера: 108 МП, 12 МП, 10 МП, 10 МП
Вес: 228 г
Емкость аккумулятора: 5000 мА⋅ч
Соотношение сторон экрана: 19:9
Разрешение экрана: 3088x1440
Диагональ экрана: 6.8"
Тип экрана: Dynamic AMOLED 2X
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
Hozirda narxi:16 000 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back1 )
    await call.message.delete()

@dp.callback_query_handler(text = "s1")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s22ultra_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s2")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s22ultra_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s3")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s22ultra_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "e1")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e2")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e3")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e4")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "s21f")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s21fe.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s21 fe
Частота обновления экрана: 120 Гц
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Процессор: Qualcomm Snapdragon 888
Стандарт связи: 3G, 4G LTE, 5G
Фронтальная камера: 32 МП
Основная камера: 12 МП, 12 МП, 8 МП
Вес: 177 г
Емкость аккумулятора: 4500 мА⋅ч
Тип экрана: Dynamic AMOLED 2X
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2340x1080
Диагональ экрана: 6.4"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:7 875 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back2 )
    await call.message.delete()

@dp.callback_query_handler(text = "s4")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s21fe_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s5")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s21fe_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "e5")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e6")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()
@dp.callback_query_handler(text = "e7")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e8")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "s20f")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s20fe.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s20 fe
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Макс. объем карты памяти: 1024ГБ
Слот для карты памяти: Есть
Соотношение сторон экрана: 20:9
Стандарт связи: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Материал корпуса: пластик
Стандарт Bluetooth: 5.0
Версия ОС: Android 10
Процессор: Samsung Exynos 990
Вес: 190 г
Емкость аккумулятора: 4500 мА⋅ч
Фронтальная камера: 32 МП
Основная камера: 12 МП, 12 МП, 8 МП
Тип экрана: AMOLED
Разрешение экрана: 2400x1080
Диагональ экрана: 6.5"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsung
hozirda narxi:5 290 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back3 )
    await call.message.delete()

@dp.callback_query_handler(text = "s6")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s20fe_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s7")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s20fe_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "e9")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e10")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()
@dp.callback_query_handler(text = "e11")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e12")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e13")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "s21u")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s21ultra.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s21 ultra
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.2
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Версия ОС: Android 11
Процессор: Samsung Exynos 2100
Фронтальная камера: 40 МП
Основная камера: 108 МП, 12 МП, 10 МП, 10 МП
Вес: 228 г
Емкость аккумулятора: 5000 мА⋅ч
Соотношение сторон экрана: 20:9
Разрешение экрана: 3200x1440
Диагональ экрана: 6.8"
Тип экрана: Dynamic AMOLED 2X
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 12 ГБ
Бренд: Samsung
hozirda narxi:11 600 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back4 )
    await call.message.delete()

@dp.callback_query_handler(text = "s8")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s21ultra_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s9")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s21ultra_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "e14")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e15")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "s21+")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s21+.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s21+5G
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Samsung Exynos 2100
Версия ОС: Android 11
NFC: Есть
Стандарт связи: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Bluetooth: Есть
Фронтальная камера: 10 МП
Основная камера: 64 МП, 12 МП, 12 МП
Вес: 202 г
Емкость аккумулятора: 4800 мА⋅ч
Разрешение экрана: 2400x1080
Соотношение сторон экрана: 20:9
Тип экрана: Dynamic AMOLED 2X
Диагональ экрана: 6.7"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:10 387 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back5 )
    await call.message.delete()
@dp.callback_query_handler(text = "s10")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s21plusG_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s11")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s21plusG_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "e16")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e17")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e18")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "sam21")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s21.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s21
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.1
Процессор: Samsung Exynos 2100
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Версия ОС: Android 11
Фронтальная камера: 10 МП
Основная камера: 64 МП, 12 МП, 12 МП
Вес: 171 г
Емкость аккумулятора: 4000 мА⋅ч
Тип экрана: Dynamic AMOLED 2X
Соотношение сторон экрана: 20:9
Разрешение экрана: 2400x1080
Диагональ экрана: 6.2"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:7 875 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back6)
    await call.message.delete()

@dp.callback_query_handler(text = "s12")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s21g_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s13")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s21g_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "e19")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e20")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e21")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e22")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "s20u")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s20ultra.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s20 ultra
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 10
Тип экрана: AMOLED
Соотношение сторон экрана: 20:9
NFC: Есть
Слот для карты памяти: Есть
Стандарт связи: 3G, 4G LTE, 5G, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 3200x1440
Процессор: Samsung Exynos 990
Фронтальная камера: 40 МП
Основная камера: 108 МП, 48 МП, 12 МП
Вес: 220 г
Емкость аккумулятора: 5000 мА⋅ч
Диагональ экрана: 6.9"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 12 ГБ
Бренд: Samsung
hozirda narxi:10 200 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back8 )
    await call.message.delete()

@dp.callback_query_handler(text = "s14")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s20ultra_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "e23")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e24")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "s20+")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s20+.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsun galaxy s20
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 10
NFC: Есть
Слот для карты памяти: Есть
Тип экрана: AMOLED
Соотношение сторон экрана: 20:9
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 3200x1440
Процессор: Samsung Exynos 990
Фронтальная камера: 10 МП
Основная камера: 64 МП, 12 МП, 12 МП
Вес: 163 г
Емкость аккумулятора: 4000 мА⋅ч
Диагональ экрана: 6.2"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back9)
    await call.message.delete()

@dp.callback_query_handler(text = "s15")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s20plus_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "e25")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e26")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e27")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "sam10")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s10.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s10
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 9.0
NFC: Есть
Слот для карты памяти: Есть
Соотношение сторон экрана: 19:9
Тип экрана: AMOLED
Стандарт связи: 3G, 4G LTE, LTE-A, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 3040x1440
Процессор: Samsung Exynos 9820
Фронтальная камера: 10 МП
Основная камера: 16 МП, 12 МП, 12 МП
Вес: 175 г
Емкость аккумулятора: 4100 мА⋅ч
Диагональ экрана: 6.4"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:4 000 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back10 )
    await call.message.delete()

@dp.callback_query_handler(text = "s16")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = s10_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "e28")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e29")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e30")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "e31")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "not20u")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not20ultra.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy not s20 ultra
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 10
NFC: Есть
Слот для карты памяти: Есть
Тип экрана: Dynamic AMOLED 2X
Соотношение сторон экрана: 19:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 3088x1440
Процессор: Samsung Exynos 990
Фронтальная камера: 10 МП
Основная камера: 108 МП, 12 МП, 12 МП
Вес: 208 г
Емкость аккумулятора: 4500 мА⋅ч
Диагональ экрана: 6.9"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:10 214 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = samnot_back1 )
    await call.message.delete()

@dp.callback_query_handler(text = "s17")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = not20ultra_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s18")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = not20ultra_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s19")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = not20ultra_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "f4")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f5")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f6")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "not20")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not20.png','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy not s20
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 10
Слот для карты памяти: Есть
NFC: Есть
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Соотношение сторон экрана: 20:9
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Процессор: Samsung Exynos 990
Фронтальная камера: 10 МП
Основная камера: 64 МП, 12 МП, 12 МП
Вес: 195 г
Емкость аккумулятора: 4300 мА⋅ч
Разрешение экрана: 2400x1080
Тип экрана: Super AMOLED
Диагональ экрана: 6.7"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:8 854 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = samnot_back2 )
    await call.message.delete()

@dp.callback_query_handler(text = "s20")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = not20_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s21")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = not20_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "f1")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f2")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f3")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "not10")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not10.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy not s10
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Samsung Exynos 9825
Стандарт связи: 3G, 4G LTE, LTE-A, GSM 900/1800/1900
NFC: Есть
Слот для карты памяти: Есть
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Версия ОС: Android 9.0
Фронтальная камера: 10 МП
Основная камера: 12 МП, 16 МП, 12 МП
Вес: 168 г
Емкость аккумулятора: 3500 мА⋅ч
Соотношение сторон экрана: 19:9
Разрешение экрана: 2280x1080
Тип экрана: AMOLED
Диагональ экрана: 6.3"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:5 245 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = samnot_back3 )
    await call.message.delete()

@dp.callback_query_handler(text = "s22")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = not10_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "f7")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f8")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f9")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "not10+")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not10+.jpeg','rb'),
        caption = """Hurmatli mijjoz siz tanlagan
samsung galaxy not 10 plus
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Samsung Exynos 9825
Стандарт связи: 3G, 4G LTE, LTE-A, GSM 900/1800/1900
NFC: Есть
Слот для карты памяти: Есть
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Версия ОС: Android 9.0
Фронтальная камера: 10 МП
Основная камера: 12 МП, 16 МП, 12 МП
Вес: 168 г
Емкость аккумулятора: 3500 мА⋅ч
Соотношение сторон экрана: 19:9
Разрешение экрана: 2280x1080
Тип экрана: AMOLED
Диагональ экрана: 6.3"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung

Iltimos xotira turini tanlang👇👇👇
""",reply_markup = samnot_back4 )
    await call.message.delete()

@dp.callback_query_handler(text = "s23")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = not10plus_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "f10")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f11")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f12")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "zfold3")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/zfold3.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy z fold 3
Стандарт связи: 3G, 4G LTE, 5G, GSM 900/1800
NFC: Есть
Стандарт Bluetooth: 5.2
Материал корпуса: алюминий
Версия ОС: Android 11
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Тип экрана: Dynamic AMOLED 2X
Разрешение экрана: 2208x1768
Процессор: Qualcomm Snapdragon 888
Фронтальная камера: 10 МП
Основная камера: 12 МП, 12 МП, 12 МП
Вес: 271 г
Емкость аккумулятора: 4400 мА⋅ч
Диагональ экрана: 7.6"
Объем встроенной памяти: 512 ГБ
Объем оперативной памяти: 12 ГБ
Бренд: Samsung
hozirda narxi:17 055 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = zfold3_back )
    await call.message.delete()

@dp.callback_query_handler(text = "s24")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = zfold3_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s25")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = zfold3_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "f13")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f14")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f15")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "zflip3")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/zflip3.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy z flip 3
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Версия ОС: Android 11
Процессор: Qualcomm Snapdragon 888
NFC: Есть
Стандарт связи: 3G, 4G LTE, 5G, GSM 900/1800/1900
Стандарт Bluetooth: 5.0
Фронтальная камера: 10 МП
Основная камера: 12 МП, 12 МП
Вес: 183 г
Материал корпуса: алюминий
Емкость аккумулятора: 3300 мА⋅ч
Разрешение экрана: 2640х1080
Соотношение сторон экрана: 22:9
Диагональ экрана: 6.7"
Тип экрана: AMOLED
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:9 000 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = zflip3_back )
    await call.message.delete()

@dp.callback_query_handler(text = "s26")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = zflip3_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s27")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = zflip3_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "f16")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f17")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f18")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f19")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "zfold")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/zfold2.jpeg','rb'),
        caption = """
        Hurmatli mijoz siz tanlagan 
samsung galaxy z flip 2
Бренд: Samsung
Объем оперативной памяти: 12 ГБ
Объем встроенной памяти: 256 ГБ
Диагональ экрана: 7.6"
Емкость аккумулятора: 4500 мА⋅ч
Вес: 282 г
Основная камера: 12 МП, 12 МП, 12 МП
Фронтальная камера: 10 МП
Процессор: Qualcomm Snapdragon 865 Plus
Разрешение экрана: 2208x1768
hozirda narxi:14 344 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = zfold2_back)
    await call.message.delete()

@dp.callback_query_handler(text = "s28")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = zfold2_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "f20")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f21")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "zflip")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/zflip.jpg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy z flip 2
Бренд: Samsung
Объем оперативной памяти: 12 ГБ
Объем встроенной памяти: 256 ГБ
Диагональ экрана: 7.6"
Емкость аккумулятора: 4500 мА⋅ч
Вес: 282 г
Основная камера: 12 МП, 12 МП, 12 МП
Фронтальная камера: 10 МП
Процессор: Qualcomm Snapdragon 865 Plus
Разрешение экрана: 2208x1768
hozirda narxi:7 144 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = zflip_back)
    await call.message.delete()

@dp.callback_query_handler(text = "s29")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = zfold2_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "f22")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "f23")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()




@dp.callback_query_handler(text = "a73")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a73.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a73
Версия ОС   Android 12
Вес (гр)    181
Встроенная память (ROM) (ГБ)    128
Год выпуска 2022
Диагональ дисплея (дюймы)   6.7
Емкость аккумулятора (мА/ч) 5000
Количество SIM карт 2
количество камер    4
Количество ядер 8
Максимальный объем карты памяти, Гб 1024
Материал корпуса    пластик
Оперативная память (RAM) (ГБ)   6
Основная камера МПикс   108
Отпечаток пальца    есть
Процессор   Qualcomm Snapdragon 778G
Разрешение экрана   2400x1080
Тип SIM карты   nano-SIM
Тип аккумулятора    Li-Pol
Фронтальная камера МПикс    32
Функция быстрой зарядки есть
Цвет    светло-зеленый
Цветной экран   есть
Ширина  76.1 мм
hozirda anrxi:9 255 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back8 )
    await call.message.delete()

@dp.callback_query_handler(text = "s30")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama73_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "k1")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k2")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k3")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "a53")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a53.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a53
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Samsung Exynos 1280
Версия ОС: Android 12
Слот для карты памяти: Есть
NFC: Есть
Стандарт связи: 3G, 4G LTE, 5G
Стандарт Bluetooth: 5.1
Фронтальная камера: 32 МП
Основная камера: 64 МП, 12 МП, 5 МП, 5 МП
Вес: 189 г
Емкость аккумулятора: 5000 мА⋅ч
Материал корпуса: пластик
Разрешение экрана: 2400x1080
Соотношение сторон экрана: 20:9
Тип экрана: Super AMOLED
Диагональ экрана: 6.5"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsung
hozirda narxi:4 452 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back800 )
    await call.message.delete()

@dp.callback_query_handler(text = "s31")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama53_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "k4")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k5")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k6")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k7")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "a33")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a33.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a33
Макс. объем карты памяти: 1024ГБ
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Samsung Exynos 1280
Версия ОС: Android 11
Слот для карты памяти: Есть
NFC: Есть
Стандарт связи: 3G, 4G LTE, 5G
Стандарт Bluetooth: 5.1
Фронтальная камера: 13 МП
Основная камера: 48 МП, 8 МП, 5 МП, 2 МП
Вес: 186 г
Емкость аккумулятора: 5000 мА⋅ч
Материал корпуса: пластик
Разрешение экрана: 2400x1080
Соотношение сторон экрана: 20:9
Тип экрана: Super AMOLED
Диагональ экрана: 6.4"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsung
hozirda narxi:3 831 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back801 )
    await call.message.delete()

@dp.callback_query_handler(text = "s32")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama33_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "k8")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k9")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k10")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k11")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "a22")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a22.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a22
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Макс. объем карты памяти: 512ГБ
Слот для карты памяти: Есть
Процессор: MediaTek Helio G80
Версия ОС: Android 11
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
NFC: Есть
Стандарт Bluetooth: 5.0
Фронтальная камера: 13 МП
Основная камера: 48 МП, 8 МП, 2 МП, 2 МП
Вес: 186 г
Емкость аккумулятора: 5000 мА⋅ч
Разрешение экрана: 1600x720
Соотношение сторон экрана: 20:9
Диагональ экрана: 6.4"
Тип экрана: Super AMOLED
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Samsung
hozirda narxi:2 890 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back802 )
    await call.message.delete()


@dp.callback_query_handler(text = "s33")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama22_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "k15")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k16")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k17")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k18")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "a23")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a23.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a23
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Макс. объем карты памяти: 1024ГБ
Слот для карты памяти: Есть
Процессор: Qualcomm Snapdragon 680
Версия ОС: Android 12
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
NFC: Есть
Стандарт Bluetooth: 5.0
Фронтальная камера: 8 МП
Основная камера: 50 МП, 5 МП, 2 МП, 2 МП
Вес: 195 г
Емкость аккумулятора: 5000 мА⋅ч
Разрешение экрана: 2408x1080
Соотношение сторон экрана: 20:9
Диагональ экрана: 6.6"
Тип экрана: TFT
Объем встроенной памяти: 64 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Samsung
hozirda narxi:2 690 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back803 )
    await call.message.delete()

@dp.callback_query_handler(text = "s34")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama23_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "k12")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k13")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k14")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "a13")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a13.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a13
Слот для карты памяти: Есть
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
NFC: Есть
Стандарт Bluetooth: 5.0
Материал корпуса: пластик
Стандарт связи: 3G, 4G LTE
Процессор: Samsung Exynos 850
Версия ОС: Android 11
Фронтальная камера: 5 МП
Основная камера: 50 МП, 5 МП, 2 МП, 2 МП
Вес: 205 г
Емкость аккумулятора: 5000 мА⋅ч
Соотношение сторон экрана: 20:9
Разрешение экрана: 1600x720
Тип экрана: PLS
Диагональ экрана: 6.5"
Объем встроенной памяти: 64 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Samsung
hozirda narxi: 2 225 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back804 )
    await call.message.delete()


@dp.callback_query_handler(text = "s35")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama13_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s36")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama13_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "k19")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k20")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k21")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "a72")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a72.png','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a72
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Qualcomm Snapdragon 720G
Версия ОС: Android 11
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
Слот для карты памяти: Есть
NFC: Есть
Стандарт Bluetooth: 5.0
Фронтальная камера: 32 МП
Основная камера: 64 МП, 12 МП, 8 МП, 5 МП
Вес: 203 г
Емкость аккумулятора: 5000 мА⋅ч
Материал корпуса: пластик
Соотношение сторон экрана: 20:9
Тип экрана: Super AMOLED
Разрешение экрана: 2400x1080
Диагональ экрана: 6.7"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:4 859 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back805 )
    await call.message.delete()

@dp.callback_query_handler(text = "s37")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama72_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s38")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama72_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s39")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama72_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k22")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k23")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k24")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k25")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "a52")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a52.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a72
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Qualcomm Snapdragon 720G
Версия ОС: Android 11
Слот для карты памяти: Есть
NFC: Есть
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
Стандарт Bluetooth: 5.0
Фронтальная камера: 32 МП
Основная камера: 64 МП, 12 МП, 5 МП, 5 МП
Вес: 187 г
Емкость аккумулятора: 4500 мА⋅ч
Материал корпуса: пластик
Разрешение экрана: 2400x1080
Соотношение сторон экрана: 20:9
Тип экрана: Super AMOLED
Диагональ экрана: 6.5"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsung
hozirda narxi:3 581 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back806 )
    await call.message.delete()

@dp.callback_query_handler(text = "s40")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama52_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s41")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama52_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s42")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama52_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s43")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama52_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k26")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()
@dp.callback_query_handler(text = "k27")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k28")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k29")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "a32")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a32.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a32
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Процессор: MediaTek Helio G80
Версия ОС: Android 11
NFC: Есть
Макс. объем карты памяти: 1024ГБ
Слот для карты памяти: Есть
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
Стандарт Bluetooth: 5.0
Фронтальная камера: 20 МП
Основная камера: 64 МП, 8 МП, 5 МП, 5 МП
Вес: 184 г
Емкость аккумулятора: 5000 мА⋅ч
Материал корпуса: пластик
Соотношение сторон экрана: 20:9
Разрешение экрана: 2400x1080
Тип экрана: Super AMOLED
Диагональ экрана: 6.4"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsun
hozirda narxi:2 904 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back807 )
    await call.message.delete()


@dp.callback_query_handler(text = "s44")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama32_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s45")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama32_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s46")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama32_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k30")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k31")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k32")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k33")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "a03")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a03s.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a03s
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Стандарт Bluetooth: 5.0
Стандарт связи: 3G, 4G LTE, LTE-A, GSM 900/1800/1900
Версия ОС: Android 11
Процессор: MediaTek Helio P35
Фронтальная камера: 5 МП
Основная камера: 13 МП, 2 МП, 2 МП
Вес: 196 г
Емкость аккумулятора: 5000 мА⋅ч
Соотношение сторон экрана: 20:9
Разрешение экрана: 1600x720
Диагональ экрана: 6.5"
Тип экрана: PLS
Объем встроенной памяти: 32 ГБ
Объем оперативной памяти: 2 ГБ
Бренд: Samsung
hozirda narxi:1 903 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back808 )
    await call.message.delete()


@dp.callback_query_handler(text = "s47")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama03s_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s48")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama03s_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "s49")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = sama03s_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k34")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k35")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k36")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


# """""""""""""""""""""""""""""""""""""""""""""""""REDMI"""""""""""""""""""""""""""""""""""""""""""""""""""""''


@dp.callback_query_handler(text = "redmi")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "m11")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mi11.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
xiomi mi 11 Lite
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Bluetooth standarti: 5.1
Old Kamera: 20 МП
Orqa kamera: 48 МП, 8 МП, 5 МП
Vazn: 196 г
Batareya quvvati: 4520 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.67"
Protsessor: Qualcomm Snapdragon 870 5G
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
hozirda narxi:5 281 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back2 )
    await call.message.delete()

@dp.callback_query_handler(text = "n1")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomim11_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "n2")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomim11_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k37")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k38")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "mi10")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mi10tpro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
xiomi mi 10t pro
Ekran yangilanish chastotasi: 144 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Operatsion tizim versiyasi: Android 10
Protsessor: Qualcomm Snapdragon 865
NFC: Есть
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Bluetooth standarti: 5.1
Old Kamera: 20 МП
Orqa kamera: 108 МП, 13 МП, 5 МП
Vazn: 218 г
Batareya quvvati: 5000 мА⋅ч
Korpus materiali: металл и стекло
Ekran tomonlari nisbati: 20:9
Ekran piksellari o'lchamlari: 2400x1080
Ekran texnologiyasi: IPS
Ekran o'lchami: 6.67"
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Xiaomi
hozirda narxi:6 241 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back200 )
    await call.message.delete()

@dp.callback_query_handler(text = "n3")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomim10tpro_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "n4")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomim10tpro_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k39")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "k40")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k41")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "pocof3")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/pocof3.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Poco F3
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 20 МП
Orqa kamera: 48 МП, 8 МП, 5 МП
Vazn: 196 г
Batareya quvvati: 4520 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.67"
Protsessor: Qualcomm Snapdragon 870 5G
Doimiy xotira hajmi: 256 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Xiaomi
xozirda narxi:4 410 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back201 )
    await call.message.delete()

@dp.callback_query_handler(text = "n5")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomipocof3_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "n6")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomipocof3_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k42")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k43")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k44")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "mit10")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mi10t.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Mi 10T
Ekran yangilanish chastotasi: 144 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Protsessor: Qualcomm Snapdragon 865
Operatsion tizim versiyasi: Android 10
Aloqa standarti: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 20 МП
Orqa kamera: 64 МП, 13 МП, 5 МП
Vazn: 216 г
Batareya quvvati: 5000 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran o'lchami: 6.67"
Ekran texnologiyasi: IPS
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
xozirda narxi:6 200 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back202 )
    await call.message.delete()

@dp.callback_query_handler(text = "n7")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomim10t_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "n8")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomim10t_rangi)
    await call.message.delete()



@dp.callback_query_handler(text = "k45")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k46")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "minot10")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/minot10.jpeg','rb'),
        caption = """
xiomi not 10
Protsessor: Qualcomm Snapdragon 678
Ekran yangilanish chastotasi: 60 Гц
Korpus materiali: стекло и пластик
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Himoya darajasi: IP53
Operatsion tizim versiyasi: Android 11
Xotira kartasi sloti: Есть
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Bluetooth standarti: 5.0
Old Kamera: 13 МП
Orqa kamera: 48 МП, 8 МП, 2 МП, 2 МП
Vazn: 179 г
Batareya quvvati: 5000 мА⋅ч
Ekran texnologiyasi: Super AMOLED
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran o'lchami: 6.43"
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 4 ГБ
Brend: Xiaomi
xozirda narxi:2 341 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back203 )
    await call.message.delete()


@dp.callback_query_handler(text = "n9")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomimnot10_rangi)
    await call.message.delete()



@dp.callback_query_handler(text = "n10")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomimnot10_rangi)
    await call.message.delete()



@dp.callback_query_handler(text = "n11")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomimnot10_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k47")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k48")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k49")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k50")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "n0t9")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not10pro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Redmi not 10 pro
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Himoya darajasi: IP53
Protsessor: Qualcomm Snapdragon 732G
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Xotira kartasi sloti: Есть
Bluetooth standarti: 5.1
Old Kamera: 16 МП
Orqa kamera: 108 МП, 8 МП, 5 МП, 2 МП
Vazn: 193 г
Batareya quvvati: 5020 мА⋅ч
Korpus materiali: стекло и пластик
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.67"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
xozirda narxi:2 712 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back204 )
    await call.message.delete()


@dp.callback_query_handler(text = "n12")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomimnot10pro_rangi)
    await call.message.delete()



@dp.callback_query_handler(text = "n13")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomimnot10pro_rangi)
    await call.message.delete()



@dp.callback_query_handler(text = "n14")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomimnot10pro_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "k51")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k52")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k53")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k54")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "pocox3")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/pocox3.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
xiomi poco x3
Ekran yangilanish chastotasi: 120 Гц
SIM-kartalar soni: 2
SIM-karta formati: nano SIM
Himoya darajasi: IP53
NFC: Есть
Xotira kartasi maksimal hajmi: 256ГБ
Xotira kartasi sloti: Есть
Korpus materiali: пластик
Bluetooth standarti: 5.1
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Ekran tomonlari nisbati: 20:9
Operatsion tizim versiyasi: Android 10
Protsessor: Qualcomm Snapdragon 732G
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 2400x1080
Old Kamera: 20 МП
Orqa kamera: 64 МП, 13 МП, 2 МП
Vazn: 215 г
Batareya quvvati: 5160 мА⋅ч
Ekran o'lchami: 6.67"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
xozirda narxi:2 726 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back205 )
    await call.message.delete()

@dp.callback_query_handler(text = "n15")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = pocox3_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "n16")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = pocox3_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "k55")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k56")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "mi9t")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mi9t.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Redmi 9T
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
NFC: Есть
Korpus materiali: пластик
Bluetooth standarti: 5.0
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Operatsion tizim versiyasi: Android 10
Protsessor: Qualcomm Snapdragon 662
Old Kamera: 2 МП
Orqa kamera: 48 МП, 8 МП, 2 МП, 2 МП
Vazn: 198 г
Batareya quvvati: 6000 мА⋅ч
Ekran tomonlari nisbati: 19.5:9
Ekran piksellari o'lchamlari: 2340x1080
Ekran texnologiyasi: IPS
Ekran o'lchami: 6.53
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 4 ГБ
Brend: Xiaomi
xozirda narxi:2 019 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back206 )
    await call.message.delete()

@dp.callback_query_handler(text = "n17")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomi9t_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "n18")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiomi9t_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k57")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "k58")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "k59")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "k60")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "mi9pro")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not9pro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Redmi not 9 pro
Ekran yangilanish chastotasi: 60 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Protsessor: Qualcomm Snapdragon 720G
Operatsion tizim versiyasi: Android 10
Xotira kartasi sloti: Есть
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Korpus materiali: стекло и пластик
Bluetooth standarti: 5.0
Old Kamera: 16 МП
Orqa kamera: 64 МП, 8 МП, 5 МП, 2 МП
Vazn: 209 г
Batareya quvvati: 5020 мА⋅ч
Ekran o'lchami: 6.67"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
hozirda narxi:2 763 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back207 )
    await call.message.delete()

@dp.callback_query_handler(text = "n19")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiominot9pro_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "n20")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiominot9pro_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k61")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k62")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k63")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "mir9")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/minot9.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Redmi not 9
Ekran yangilanish chastotasi: 60 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Operatsion tizim versiyasi: Android 10
Xotira kartasi sloti: Есть
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 2340x1080
Ekran tomonlari nisbati: 19.5:9
Aloqa standarti: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Korpus materiali: стекло и пластик
Bluetooth standarti: 5.0
Old Kamera: 13 МП
Orqa kamera: 48 МП, 8 МП, 2 МП, 2 МП
Vazn: 199 г
Batareya quvvati: 5020 мА⋅ч
Ekran o'lchami: 6.53"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 3 ГБ
Brend: Xiaomi
hozirda narxi 1 990 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back208 )
    await call.message.delete()

@dp.callback_query_handler(text = "n21")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiominot9_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "n22")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = xiominot9_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k64")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "k65")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "k66")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



@dp.callback_query_handler(text = "k67")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()




# """"""""""""""""""""""""""""""""""""""""""""""VIVO"""""""""""""""""""""""""""""""""""""""""""""""""""''

@dp.callback_query_handler(text = "vivo")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/vivomenu.jpeg','rb'),
        caption = "VIVO TURINI TANLANG!",reply_markup = vivo_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "x60")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/x60.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo x60
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Protsessor: Qualcomm Snapdragon 870 5G
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 32 МП
Orqa kamera: 48 МП, 13 МП, 13 МП
Vazn: 179 г
Batareya quvvati: 4200 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2376x1080
Ekran tomonlari nisbati: 19.5:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.56"
Doimiy xotira hajmi: 256 ГБ
Operativ xotira hajmi: 12 ГБ
Brend: Vivo
hozirda narxi:9 061 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back3 )
    await call.message.delete()


@dp.callback_query_handler(text = "kl1")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivox60_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "kl2")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivox60_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k68")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k69")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "x50")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/x50.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo x50
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Protsessor: Qualcomm Snapdragon 870 5G
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 32 МП
Orqa kamera: 48 МП, 13 МП, 13 МП
Vazn: 177 г
Batareya quvvati: 4200 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2376x1080
Ekran tomonlari nisbati: 19.5:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.56"
Doimiy xotira hajmi: 256 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Vivo
hozirda narxi:6 061 000


Iltimos xotira turini tanlang👇👇👇""",reply_markup = back300 )
    await call.message.delete()


@dp.callback_query_handler(text = "kl3")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivox50_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k70")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k71")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k72")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "v21")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/v21.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo v21
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Xotira kartasi sloti: Есть
Protsessor: MediaTek Dimensity 800
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 44 МП
Orqa kamera: 64 МП, 8 МП, 2 МП
Vazn: 177 г
Batareya quvvati: 4000 мА⋅ч
Ekran piksellari o'lchamlari: 2404x1080
Ekran tomonlari nisbati: 20:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.44"
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Vivo
hozirda narxi:4 527 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back301)
    await call.message.delete()


@dp.callback_query_handler(text = "kl4")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivov21_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "kl5")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivov21_rangi)
    await call.message.delete()



@dp.callback_query_handler(text = "k73")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k74")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "v20")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/v20.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivi v20
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
NFC: Есть
Xotira kartasi sloti: Есть
Korpus materiali: стекло и пластик
Bluetooth standarti: 5.1
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
Protsessor: Qualcomm Snapdragon 720G
Old Kamera: 44 МП
Orqa kamera: 64 МП, 8 МП, 2 МП
Vazn: 171 г
Batareya quvvati: 4000 мА⋅ч
Ekran tomonlari nisbati: 20:9
Ekran piksellari o'lchamlari: 2400x1080
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.44"
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Vivo
hozirda narxi:4 220 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back302 )
    await call.message.delete()

@dp.callback_query_handler(text = "kl6")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivov20_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k74")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k75")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "y30")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/y30.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo y30
Ekran yangilanish chastotasi: 60 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
NFC: Есть
Xotira kartasi maksimal hajmi: 256ГБ
Xotira kartasi sloti: Есть
Ekran texnologiyasi: IPS
Korpus materiali: пластик
Bluetooth standarti: 5.0
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
Protsessor: MediaTek Helio G35
Operatsion tizim versiyasi: Android 10
Old Kamera: 8 МП
Orqa kamera: 13 МП, 8 МП, 2 МП, 2 МП
Vazn: 197 г
Batareya quvvati: 5000 мА⋅ч
Ekran tomonlari nisbati: 19.5:9
Ekran piksellari o'lchamlari: 1560x720
Ekran o'lchami: 6.47"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 4 ГБ
Brend: Vivo
hozirda narxi:2 100 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back303)
    await call.message.delete()


@dp.callback_query_handler(text = "kl7")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivoy30_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k76")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k77")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k78")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()

@dp.callback_query_handler(text = "y20")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/y20.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivi y20
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Xotira kartasi sloti: Есть
Korpus materiali: пластик
Bluetooth standarti: 5.0
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
Protsessor: Qualcomm Snapdragon 460
Operatsion tizim versiyasi: Android 10
Old Kamera: 8 МП
Orqa kamera: 13 МП, 2 МП, 2 МП
Vazn: 192 г
Batareya quvvati: 5000 мА⋅ч
Ekran tomonlari nisbati: 20:9
Ekran piksellari o'lchamlari: 1600x720
Ekran texnologiyasi: IPS
Ekran o'lchami: 6.51"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 4 ГБ
Brend: Vivo
hozirda narxi:2 000 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back304 )
    await call.message.delete()


@dp.callback_query_handler(text = "kl8")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivoy20_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k79")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k80")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k81")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "y19")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/y19.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivi y19
Brend: Vivo
Operativ xotira hajmi: 4 ГБ
Doimiy xotira hajmi: 32 ГБ
Ekran o'lchami: 6.51"
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 1600x720
Ekran tomonlari nisbati: 20:9
Batareya quvvati: 5000 мА⋅ч
Vazn: 191 г
Orqa kamera: 13 МП, 2 МП
Old Kamera: 8 МП
Operatsion tizim versiyasi: Android 10
Protsessor: MediaTek Helio G35
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
SIM-kartalar soni: 2
SIM-karta formati: nano SIM


Iltimos xotira turini tanlang👇👇👇""",reply_markup = back305 )
    await call.message.delete()


@dp.callback_query_handler(text = "kl9")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivoy19_rangi)
    await call.message.delete()


@dp.callback_query_handler(text = "k82")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k83")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "y12s")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/y12s.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo y12s
Brend: Vivo
Operativ xotira hajmi: 3 ГБ
Doimiy xotira hajmi: 32 ГБ
Ekran o'lchami: 6.51"
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 1600x720
Ekran tomonlari nisbati: 20:9
Batareya quvvati: 5000 мА⋅ч
Vazn: 191 г
Orqa kamera: 13 МП, 2 МП
Old Kamera: 8 МП
Operatsion tizim versiyasi: Android 10
Protsessor: MediaTek Helio G35
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
SIM-kartalar soni: 2
SIM-karta formati: nano SIM
hozirda narxi 1 819 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back306 )
    await call.message.delete()


@dp.callback_query_handler(text = "kl10")
async def UZB(call:CallbackQuery):
    await call.message.answer("Iltimos rangini tanlang👇👇👇",reply_markup = vivoy12s_rangi)
    await call.message.delete()

@dp.callback_query_handler(text = "k84")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()


@dp.callback_query_handler(text = "k85")
async def UZ(call:CallbackQuery):
    await call.message.answer("Iltimos telefon raqamingizni jo'nating",reply_markup = raqam)
    await call.message.delete()



# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""nazad"""""""""""""""""""""""""""""""""""""""""""""""""""""""
# ipone
@dp.callback_query_handler(text = "nazad1")
async def UZB(call:CallbackQuery):
    await call.message.answer("Assalomu alaykum\nTelefon bozorga xush kelibsiz\nIltimos telefon turini tanlang!",reply_markup = tur)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad2")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/iponmenu.jpg','rb'),
        caption = "IPONE TURINI TANLANG!",reply_markup = ipon_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad3")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/iponmenu.jpg','rb'),
        caption = "IPONE TURINI TANLANG!",reply_markup = ipon_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad4")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/iponmenu.jpg','rb'),
        caption = "IPONE TURINI TANLANG!",reply_markup = ipon_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad12")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO MAX TURINI TANLANG!",reply_markup = promax_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa1")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO MAX TURINI TANLANG!",reply_markup = promax_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad21")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/13promax.jpeg','rb'),
        caption = """Hurmatli mijoznsiz tanlagan IPONE 13 PRO MAX
Cтепень защиты: IP68
Процессор: Apple A15 Bionic
Версия ОС: iOS 15
Стандарт связи: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Материал корпуса: металл и стекло
Вес: 238 г
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2778x1284
Тип экрана: OLED
Диагональ экрана: 6.7"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Apple
Xozirda narxi:13 310 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad22")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/12promax.jpeg','rb'),
        caption = """Hurmatli mijoz\nsiz tanlagan IPONE 12 PRO MAX
Частота обновления экрана: 60 Гц
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Процессор: Apple A14 Bionic
Версия ОС: iOS 14
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Вес: 226 г
Емкость аккумулятора: 3687 мА⋅ч
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2778x1284
Тип экрана: OLED
Диагональ экрана: 6.7"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Apple
Hozirda narxi:9 524 000

Iltimos xotira turini tanlang👇👇👇 """,reply_markup = back100)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad23")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/11promax.jpeg','rb'),
        caption  = """"Hurmatli mijoz siz tanlagan
IPONE 11 PRO MAX
Частота обновления экрана: 60 Гц
Материал корпуса: металл и стекло
Процессор: Apple A13 Bionic
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Тип экрана: OLED
Версия ОС: iOS 13
Разрешение экрана: 2688x1242
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
NFC: Есть
Стандарт Bluetooth: 5.0
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Вес: 226 г
Емкость аккумулятора: 3969 мА⋅ч
Диагональ экрана: 6.5"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple
Hozirda narxi:8 210 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back101)
    await call.message.delete()


@dp.callback_query_handler(text = "orqa2")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO MAX TURINI TANLANG!",reply_markup = promax_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "orqa3")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO MAX TURINI TANLANG!",reply_markup = promax_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa4")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO TURINI TANLANG!",reply_markup = pro_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa5")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO TURINI TANLANG!",reply_markup = pro_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa6")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO TURINI TANLANG!",reply_markup = pro_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa7")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO TURINI TANLANG!",reply_markup = pro_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa8")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO TURINI TANLANG!",reply_markup = pro_menu)
    await call.message.delete()



@dp.callback_query_handler(text = "nazad24")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/xsmax.jpeg','rb'),
        caption = """Hurmatli mijo siz tanlagan IPONE XS MAX
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Apple A12 Bionic
Версия ОС: iOS 12
NFC: Есть
Тип экрана: OLED
Разрешение экрана: 2688x1242
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Емкость аккумулятора: 3174 мА⋅ч
Фронтальная камера: 7 МП
Основная камера: 12 МП, 12 МП
Вес: 208 г
Диагональ экрана: 6.5"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple
Hozirda narxi:6 145 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back102)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad16")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE PRO TURINI TANLANG!",reply_markup = pro_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad25")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/13pro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 13 PRO
Cтепень защиты: IP68
Стандарт Bluetooth: 5.0
Процессор: Apple A15 Bionic
Версия ОС: iOS 15
Стандарт связи: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Материал корпуса: металл и стекло
Вес: 203 г
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2532x1170
Тип экрана: OLED
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Apple
Hozirda narxi:

Iltimos xotira turini tanlang 👇👇👇""",reply_markup = back4)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad26")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/12pro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 12 PRO
Частота обновления экрана: 60 Гц
Тип экрана: OLED
Материал корпуса: металл и стекло
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: iOS 14
NFC: Есть
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Стандарт Bluetooth: 5.0
Емкость аккумулятора: 2815 мА⋅ч
Разрешение экрана: 2532x1170
Процессор: Apple A14 Bionic
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП
Вес: 187 г
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Apple
 Hozirda narxi ?

Iltimos xotira turini tanlang 👇👇👇""",reply_markup = back400)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad27")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
    photo = open('image/11pro.jpeg','rb'),
    caption = """Hurmatli mijoz siz tanlagan IPONE 11 PRO
Частота обновления экрана: 60 Гц
Разрешение экрана: 2436x1125
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Apple A13 Bionic
Версия ОС: iOS 13
Тип экрана: OLED
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
NFC: Есть
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП, 12 МП
Вес: 188 г
Емкость аккумулятора: 3190 мА⋅ч
Диагональ экрана: 5.8"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple
Hozirda narxi ?

Iltimos xotira turini tanlang 👇👇👇""",reply_markup = back401)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad28")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/xs.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE XS
Частота обновления экрана: 60 Гц
Процессор: Apple A12 Bionic
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: iOS 12
NFC: Есть
Тип экрана: OLED
Разрешение экрана: 2436x1125
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Фронтальная камера: 7 МП
Основная камера: 12 МП, 12 МП
Вес: 177 г
Емкость аккумулятора: 2658 мА⋅ч
Диагональ экрана: 5.8"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple Hozirda narxi ?""",reply_markup = back402)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad29")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/xr.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE XR
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Apple A12 Bionic
Версия ОС: iOS 12
NFC: Есть
Тип экрана: IPS
Разрешение экрана: 1792x828
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Фронтальная камера: 7 МП
Основная камера: 12 МП
Вес: 194 г
Емкость аккумулятора: 2942 мА⋅ч
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 3 ГБ
Бренд: Apple
Hozirda narxi """,reply_markup = back403)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad17")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE TURINI TANLANG!",reply_markup = min_menu)
    await call.message.delete()
@dp.callback_query_handler(text = "orqa9")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE TURINI TANLANG!",reply_markup = min_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa10")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE TURINI TANLANG!",reply_markup = min_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa11")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE TURINI TANLANG!",reply_markup = min_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa12")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE TURINI TANLANG!",reply_markup = min_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa13")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE TURINI TANLANG!",reply_markup = min_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa14")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE TURINI TANLANG!",reply_markup = min_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "orqa15")
async def UZB(call:CallbackQuery):
    await call.message.answer("IPONE TURINI TANLANG!",reply_markup = min_menu)
    await call.message.delete()



@dp.callback_query_handler(text = "nazad30")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/13.jpeg','rb'),
        caption = """Hurmatli mijoz  siz tanlagan IPONE 13
Cтепень защиты: IP68
Стандарт Bluetooth: 5.0
Процессор: Apple A15 Bionic
Версия ОС: iOS 15
Стандарт связи: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП
Материал корпуса: алюминий и стекло
Вес: 173 г
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2532x1170
Тип экрана: OLED
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple 
Hozirda narxi

Iltimos xotira turini tanlang👇👇👇 """,reply_markup = back5)
    await call.message.delete()
    

@dp.callback_query_handler(text = "nazad31")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/12.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 12
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: iOS 14
NFC: Есть
Тип экрана: OLED
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Соотношение сторон экрана: 19.5:9
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.0
Емкость аккумулятора: 2815 мА⋅ч
Разрешение экрана: 2532x1170
Объем оперативной памяти: 4 ГБ
Процессор: Apple A14 Bionic
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП
Вес: 164 г
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Бренд: Apple 
Hozirda narxi

Iltimos xotira turini tanlang👇👇👇 """,reply_markup = back500)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad32")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/11.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 11
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Apple A13 Bionic
Версия ОС: iOS 13
Тип экрана: IPS
Разрешение экрана: 1792x828
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
NFC: Есть
Фронтальная камера: 12 МП
Основная камера: 12 МП, 12 МП
Вес: 194 г
Емкость аккумулятора: 3110 мА⋅ч
Диагональ экрана: 6.1"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Apple 
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back501)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad33")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/x.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE x
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
NFC: Есть
Тип экрана: OLED
Разрешение экрана: 2436x1125
Соотношение сторон экрана: 19.5:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.0
Процессор: Apple A11 Bionic
Фронтальная камера: 7 МП
Основная камера: 12 МП, 12 МП
Вес: 174 г
Емкость аккумулятора: 2716 мА⋅ч
Диагональ экрана: 5.8"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 3 ГБ
Бренд: Apple
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back502)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad34")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/8+.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 8+
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
NFC: Есть
Тип экрана: IPS
Соотношение сторон экрана: 16:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.0
Процессор: Apple A11 Bionic
Бренд: Apple
Объем оперативной памяти: 3 ГБ
Объем встроенной памяти: 64 ГБ
Диагональ экрана: 5.5"
Емкость аккумулятора: 2691 мА⋅ч
Вес: 202 г
Основная камера: 12 МП, 12 МП
Фронтальная камера: 7 МП
Разрешение экрана: 1920x1080 
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back503)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad35")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/8.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 8
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
NFC: Есть
Тип экрана: IPS
Соотношение сторон экрана: 16:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 1334x750
Процессор: Apple A11 Bionic
Фронтальная камера: 7 МП
Основная камера: 12 МП
Вес: 148 г
Емкость аккумулятора: 1820 мА⋅ч
Диагональ экрана: 4.7"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 2 ГБ
Бренд: Apple 
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back504)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad36")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/7+.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 7+
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
Материал корпуса: алюминий и стекло
NFC: Есть
Стандарт Bluetooth: 4.2
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Процессор: Apple A10 Fusion
Версия ОС: iOS 10
Фронтальная камера: 7 МП
Основная камера: 12 МП, 12 МП
Вес: 188 г
Емкость аккумулятора: 2900 мА⋅ч
Соотношение сторон экрана: 16:9
Разрешение экрана: 1920x1080
Тип экрана: IPS
Диагональ экрана: 5.5"
Объем встроенной памяти: 32 ГБ
Объем оперативной памяти: 3 ГБ
Бренд: Apple 
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back505)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad37")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/7.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan IPONE 7 
Тип SIM-карты: nano SIM
Количество SIM-карт: 1
Cтепень защиты: IP67
Версия ОС: iOS 10
Тип экрана: IPS
NFC: Есть
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Соотношение сторон экрана: 16:9
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 4.2
Разрешение экрана: 1334x750
Процессор: Apple A10 Fusion
Фронтальная камера: 7 МП
Основная камера: 12 МП
Вес: 138 г
Емкость аккумулятора: 1960 мА⋅ч
Диагональ экрана: 4.7"
Объем встроенной памяти: 32 ГБ
Объем оперативной памяти: 2 ГБ
Бренд: Apple
Hozirda narxi 

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back506)
    await call.message.delete()

# samsung
@dp.callback_query_handler(text = "nazad5")
async def UZB(call:CallbackQuery):
    await call.message.answer("Assalomu alaykum\nTelefon bozorga xush kelibsiz\nIltimos telefon turini tanlang!",reply_markup = tur)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad6")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/sammenu.jpeg','rb'),
        caption = "Samsung TURINI TANLANG!",reply_markup = sam_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad7")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/sammenu.jpeg','rb'),
        caption = "Samsung TURINI TANLANG!",reply_markup = sam_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad8")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/sammenu.jpeg','rb'),
        caption = "Samsung TURINI TANLANG!",reply_markup = sam_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad9")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/sammenu.jpeg','rb'),
        caption = "Samsung TURINI TANLANG!",reply_markup = sam_menu)
    await call.message.delete()



@dp.callback_query_handler(text = "nazad13")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad47")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
    photo = open('image/s22ultra.jpeg','rb'),
    caption =  """Hurmatli mijos siz tanlagan
samsung galaxy s22 ultra
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Стандарт Bluetooth: 5.2
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Процессор: Samsung Exynos 2200
Фронтальная камера: 40 МП
Основная камера: 108 МП, 12 МП, 10 МП, 10 МП
Вес: 228 г
Емкость аккумулятора: 5000 мА⋅ч
Соотношение сторон экрана: 19:9
Разрешение экрана: 3088x1440
Диагональ экрана: 6.8"
Тип экрана: Dynamic AMOLED 2X
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
Hozirda narxi:16 000 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back1 )
    await call.message.delete()
    
@dp.callback_query_handler(text = "nazad38")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad39")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad40")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad41")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad42")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad44")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad45")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad46")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung S seria TURINI TANLANG!",reply_markup = s_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad48")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s21fe.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s21 fe
Частота обновления экрана: 120 Гц
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Процессор: Qualcomm Snapdragon 888
Стандарт связи: 3G, 4G LTE, 5G
Фронтальная камера: 32 МП
Основная камера: 12 МП, 12 МП, 8 МП
Вес: 177 г
Емкость аккумулятора: 4500 мА⋅ч
Тип экрана: Dynamic AMOLED 2X
Соотношение сторон экрана: 19.5:9
Разрешение экрана: 2340x1080
Диагональ экрана: 6.4"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:7 875 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back2 )
    await call.message.delete()

@dp.callback_query_handler(text = "nazad49")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s20fe.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s20 fe
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Макс. объем карты памяти: 1024ГБ
Слот для карты памяти: Есть
Соотношение сторон экрана: 20:9
Стандарт связи: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Материал корпуса: пластик
Стандарт Bluetooth: 5.0
Версия ОС: Android 10
Процессор: Samsung Exynos 990
Вес: 190 г
Емкость аккумулятора: 4500 мА⋅ч
Фронтальная камера: 32 МП
Основная камера: 12 МП, 12 МП, 8 МП
Тип экрана: AMOLED
Разрешение экрана: 2400x1080
Диагональ экрана: 6.5"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsung
hozirda narxi:5 290 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back3 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad50")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s21ultra.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s21 ultra
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.2
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Версия ОС: Android 11
Процессор: Samsung Exynos 2100
Фронтальная камера: 40 МП
Основная камера: 108 МП, 12 МП, 10 МП, 10 МП
Вес: 228 г
Емкость аккумулятора: 5000 мА⋅ч
Соотношение сторон экрана: 20:9
Разрешение экрана: 3200x1440
Диагональ экрана: 6.8"
Тип экрана: Dynamic AMOLED 2X
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 12 ГБ
Бренд: Samsung
hozirda narxi:11 600 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back4 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad51")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s21+.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s21+5G
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Samsung Exynos 2100
Версия ОС: Android 11
NFC: Есть
Стандарт связи: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Bluetooth: Есть
Фронтальная камера: 10 МП
Основная камера: 64 МП, 12 МП, 12 МП
Вес: 202 г
Емкость аккумулятора: 4800 мА⋅ч
Разрешение экрана: 2400x1080
Соотношение сторон экрана: 20:9
Тип экрана: Dynamic AMOLED 2X
Диагональ экрана: 6.7"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:10 387 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back5 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad52")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s21.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s21
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Cтепень защиты: IP68
NFC: Есть
Материал корпуса: алюминий и стекло
Стандарт Bluetooth: 5.1
Процессор: Samsung Exynos 2100
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
Версия ОС: Android 11
Фронтальная камера: 10 МП
Основная камера: 64 МП, 12 МП, 12 МП
Вес: 171 г
Емкость аккумулятора: 4000 мА⋅ч
Тип экрана: Dynamic AMOLED 2X
Соотношение сторон экрана: 20:9
Разрешение экрана: 2400x1080
Диагональ экрана: 6.2"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:7 875 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back6)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad53")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s20ultra.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s20 ultra
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 10
Тип экрана: AMOLED
Соотношение сторон экрана: 20:9
NFC: Есть
Слот для карты памяти: Есть
Стандарт связи: 3G, 4G LTE, 5G, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 3200x1440
Процессор: Samsung Exynos 990
Фронтальная камера: 40 МП
Основная камера: 108 МП, 48 МП, 12 МП
Вес: 220 г
Емкость аккумулятора: 5000 мА⋅ч
Диагональ экрана: 6.9"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 12 ГБ
Бренд: Samsung
hozirda narxi:10 200 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back8 )
    await call.message.delete()
    
@dp.callback_query_handler(text = "nazad54")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s20+.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsun galaxy s20
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 10
NFC: Есть
Слот для карты памяти: Есть
Тип экрана: AMOLED
Соотношение сторон экрана: 20:9
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 3200x1440
Процессор: Samsung Exynos 990
Фронтальная камера: 10 МП
Основная камера: 64 МП, 12 МП, 12 МП
Вес: 163 г
Емкость аккумулятора: 4000 мА⋅ч
Диагональ экрана: 6.2"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back9)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad55")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/s10.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy s10
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 9.0
NFC: Есть
Слот для карты памяти: Есть
Соотношение сторон экрана: 19:9
Тип экрана: AMOLED
Стандарт связи: 3G, 4G LTE, LTE-A, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 3040x1440
Процессор: Samsung Exynos 9820
Фронтальная камера: 10 МП
Основная камера: 16 МП, 12 МП, 12 МП
Вес: 175 г
Емкость аккумулятора: 4100 мА⋅ч
Диагональ экрана: 6.4"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:4 000 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = sam_back10 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad18")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung NOT seria TURINI TANLANG!",reply_markup = not_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad56")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung NOT seria TURINI TANLANG!",reply_markup = not_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad57")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung NOT seria TURINI TANLANG!",reply_markup = not_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad58")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung NOT seria TURINI TANLANG!",reply_markup = not_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad59")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung NOT seria TURINI TANLANG!",reply_markup = not_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad61")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not20ultra.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy not s20 ultra
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 10
NFC: Есть
Слот для карты памяти: Есть
Тип экрана: Dynamic AMOLED 2X
Соотношение сторон экрана: 19:9
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Разрешение экрана: 3088x1440
Процессор: Samsung Exynos 990
Фронтальная камера: 10 МП
Основная камера: 108 МП, 12 МП, 12 МП
Вес: 208 г
Емкость аккумулятора: 4500 мА⋅ч
Диагональ экрана: 6.9"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:10 214 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = samnot_back1)
    await call.message.delete()
    

@dp.callback_query_handler(text = "nazad60")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
    photo = open('image/not20.png','rb'),
    caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy not s20
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Версия ОС: Android 10
Слот для карты памяти: Есть
NFC: Есть
Стандарт связи: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Соотношение сторон экрана: 20:9
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Процессор: Samsung Exynos 990
Фронтальная камера: 10 МП
Основная камера: 64 МП, 12 МП, 12 МП
Вес: 195 г
Емкость аккумулятора: 4300 мА⋅ч
Разрешение экрана: 2400x1080
Тип экрана: Super AMOLED
Диагональ экрана: 6.7"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:8 854 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = samnot_back2 )
    await call.message.delete()

@dp.callback_query_handler(text = "nazad62")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not10.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy not s10
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Samsung Exynos 9825
Стандарт связи: 3G, 4G LTE, LTE-A, GSM 900/1800/1900
NFC: Есть
Слот для карты памяти: Есть
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Версия ОС: Android 9.0
Фронтальная камера: 10 МП
Основная камера: 12 МП, 16 МП, 12 МП
Вес: 168 г
Емкость аккумулятора: 3500 мА⋅ч
Соотношение сторон экрана: 19:9
Разрешение экрана: 2280x1080
Тип экрана: AMOLED
Диагональ экрана: 6.3"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:5 245 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = samnot_back3 )
    await call.message.delete()

@dp.callback_query_handler(text = "nazad63")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not10+.jpeg','rb'),
        caption = """Hurmatli mijjoz siz tanlagan
samsung galaxy not 10 plus
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP68
Процессор: Samsung Exynos 9825
Стандарт связи: 3G, 4G LTE, LTE-A, GSM 900/1800/1900
NFC: Есть
Слот для карты памяти: Есть
Материал корпуса: металл и стекло
Стандарт Bluetooth: 5.0
Версия ОС: Android 9.0
Фронтальная камера: 10 МП
Основная камера: 12 МП, 16 МП, 12 МП
Вес: 168 г
Емкость аккумулятора: 3500 мА⋅ч
Соотношение сторон экрана: 19:9
Разрешение экрана: 2280x1080
Тип экрана: AMOLED
Диагональ экрана: 6.3"
Объем встроенной памяти: 256 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung

Iltimos xotira turini tanlang👇👇👇""",reply_markup = samnot_back4)
    await call.message.delete()



@dp.callback_query_handler(text = "nazad20")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad72")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad73")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad74")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad75")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad76")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad77")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad78")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad79")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad80")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung A seria TURINI TANLANG!",reply_markup = a_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad81")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a73.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a73
Версия ОС   Android 12
Вес (гр)    181
Встроенная память (ROM) (ГБ)    128
Год выпуска 2022
Диагональ дисплея (дюймы)   6.7
Емкость аккумулятора (мА/ч) 5000
Количество SIM карт 2
количество камер    4
Количество ядер 8
Максимальный объем карты памяти, Гб 1024
Материал корпуса    пластик
Оперативная память (RAM) (ГБ)   6
Основная камера МПикс   108
Отпечаток пальца    есть
Процессор   Qualcomm Snapdragon 778G
Разрешение экрана   2400x1080
Тип SIM карты   nano-SIM
Тип аккумулятора    Li-Pol
Фронтальная камера МПикс    32
Функция быстрой зарядки есть
Цвет    светло-зеленый
Цветной экран   есть
Ширина  76.1 мм
hozirda anrxi:9 255 000""",reply_markup = back8 )
    await call.message.delete()

@dp.callback_query_handler(text = "nazad82")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a53.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a53
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Samsung Exynos 1280
Версия ОС: Android 12
Слот для карты памяти: Есть
NFC: Есть
Стандарт связи: 3G, 4G LTE, 5G
Стандарт Bluetooth: 5.1
Фронтальная камера: 32 МП
Основная камера: 64 МП, 12 МП, 5 МП, 5 МП
Вес: 189 г
Емкость аккумулятора: 5000 мА⋅ч
Материал корпуса: пластик
Разрешение экрана: 2400x1080
Соотношение сторон экрана: 20:9
Тип экрана: Super AMOLED
Диагональ экрана: 6.5"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsung
hozirda narxi:4 452 000""",reply_markup = back800 )
    await call.message.delete()

@dp.callback_query_handler(text = "nazad83")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a33.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a33
Макс. объем карты памяти: 1024ГБ
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Samsung Exynos 1280
Версия ОС: Android 11
Слот для карты памяти: Есть
NFC: Есть
Стандарт связи: 3G, 4G LTE, 5G
Стандарт Bluetooth: 5.1
Фронтальная камера: 13 МП
Основная камера: 48 МП, 8 МП, 5 МП, 2 МП
Вес: 186 г
Емкость аккумулятора: 5000 мА⋅ч
Материал корпуса: пластик
Разрешение экрана: 2400x1080
Соотношение сторон экрана: 20:9
Тип экрана: Super AMOLED
Диагональ экрана: 6.4"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsung
hozirda narxi:3 831 000""",reply_markup = back801 )
    await call.message.delete()
 

@dp.callback_query_handler(text = "nazad84")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a23.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a23
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Макс. объем карты памяти: 1024ГБ
Слот для карты памяти: Есть
Процессор: Qualcomm Snapdragon 680
Версия ОС: Android 12
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
NFC: Есть
Стандарт Bluetooth: 5.0
Фронтальная камера: 8 МП
Основная камера: 50 МП, 5 МП, 2 МП, 2 МП
Вес: 195 г
Емкость аккумулятора: 5000 мА⋅ч
Разрешение экрана: 2408x1080
Соотношение сторон экрана: 20:9
Диагональ экрана: 6.6"
Тип экрана: TFT
Объем встроенной памяти: 64 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Samsung
hozirda narxi:2 690 000""",reply_markup = back803 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad85")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a22.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a22
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Макс. объем карты памяти: 512ГБ
Слот для карты памяти: Есть
Процессор: MediaTek Helio G80
Версия ОС: Android 11
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
NFC: Есть
Стандарт Bluetooth: 5.0
Фронтальная камера: 13 МП
Основная камера: 48 МП, 8 МП, 2 МП, 2 МП
Вес: 186 г
Емкость аккумулятора: 5000 мА⋅ч
Разрешение экрана: 1600x720
Соотношение сторон экрана: 20:9
Диагональ экрана: 6.4"
Тип экрана: Super AMOLED
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Samsung
hozirda narxi:2 890 000""",reply_markup = back802 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad86")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a13.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a13
Слот для карты памяти: Есть
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
NFC: Есть
Стандарт Bluetooth: 5.0
Материал корпуса: пластик
Стандарт связи: 3G, 4G LTE
Процессор: Samsung Exynos 850
Версия ОС: Android 11
Фронтальная камера: 5 МП
Основная камера: 50 МП, 5 МП, 2 МП, 2 МП
Вес: 205 г
Емкость аккумулятора: 5000 мА⋅ч
Соотношение сторон экрана: 20:9
Разрешение экрана: 1600x720
Тип экрана: PLS
Диагональ экрана: 6.5"
Объем встроенной памяти: 64 ГБ
Объем оперативной памяти: 4 ГБ
Бренд: Samsung
hozirda narxi: 2 225 000""",reply_markup = back804 )
    await call.message.delete()
 
@dp.callback_query_handler(text = "nazad87")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a72.png','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a72
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Qualcomm Snapdragon 720G
Версия ОС: Android 11
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
Слот для карты памяти: Есть
NFC: Есть
Стандарт Bluetooth: 5.0
Фронтальная камера: 32 МП
Основная камера: 64 МП, 12 МП, 8 МП, 5 МП
Вес: 203 г
Емкость аккумулятора: 5000 мА⋅ч
Материал корпуса: пластик
Соотношение сторон экрана: 20:9
Тип экрана: Super AMOLED
Разрешение экрана: 2400x1080
Диагональ экрана: 6.7"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:4 859 000""",reply_markup = back805 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad88")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a52.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a52
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Cтепень защиты: IP67
Процессор: Qualcomm Snapdragon 720G
Версия ОС: Android 11
Слот для карты памяти: Есть
NFC: Есть
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
Стандарт Bluetooth: 5.0
Фронтальная камера: 32 МП
Основная камера: 64 МП, 12 МП, 5 МП, 5 МП
Вес: 187 г
Емкость аккумулятора: 4500 мА⋅ч
Материал корпуса: пластик
Разрешение экрана: 2400x1080
Соотношение сторон экрана: 20:9
Тип экрана: Super AMOLED
Диагональ экрана: 6.5"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsung
hozirda narxi:3 581 000""",reply_markup = back806 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad89")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a32.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a32
Частота обновления экрана: 90 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Процессор: MediaTek Helio G80
Версия ОС: Android 11
NFC: Есть
Макс. объем карты памяти: 1024ГБ
Слот для карты памяти: Есть
Стандарт связи: 3G, 4G LTE, GSM 900/1800/1900
Стандарт Bluetooth: 5.0
Фронтальная камера: 20 МП
Основная камера: 64 МП, 8 МП, 5 МП, 5 МП
Вес: 184 г
Емкость аккумулятора: 5000 мА⋅ч
Материал корпуса: пластик
Соотношение сторон экрана: 20:9
Разрешение экрана: 2400x1080
Тип экрана: Super AMOLED
Диагональ экрана: 6.4"
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 6 ГБ
Бренд: Samsun
hozirda narxi:2 904 000""",reply_markup = back807 )
    await call.message.delete()
 
@dp.callback_query_handler(text = "nazad90")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/a03s.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
samsung galaxy a03s
Частота обновления экрана: 60 Гц
Тип SIM-карты: nano SIM
Количество SIM-карт: 2
Стандарт Bluetooth: 5.0
Стандарт связи: 3G, 4G LTE, LTE-A, GSM 900/1800/1900
Версия ОС: Android 11
Процессор: MediaTek Helio P35
Фронтальная камера: 5 МП
Основная камера: 13 МП, 2 МП, 2 МП
Вес: 196 г
Емкость аккумулятора: 5000 мА⋅ч
Соотношение сторон экрана: 20:9
Разрешение экрана: 1600x720
Диагональ экрана: 6.5"
Тип экрана: PLS
Объем встроенной памяти: 32 ГБ
Объем оперативной памяти: 2 ГБ
Бренд: Samsung
hozirda narxi:1 903 000""",reply_markup = back808 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad19")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung NOT seria TURINI TANLANG!",reply_markup = z_menu)
    await call.message.delete()

# redmi

@dp.callback_query_handler(text = "nazad10")
async def UZB(call:CallbackQuery):
    await call.message.answer("Assalomu alaykum\nTelefon bozorga xush kelibsiz\nIltimos telefon turini tanlang!",reply_markup = tur)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad14")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()
@dp.callback_query_handler(text = "nazad91")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad92")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad93")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad94")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad95")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad96")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad97")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad98")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad99")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mimenu.jpeg','rb'),
        caption = "REDMI TURINI TANLANG!",reply_markup = red_menu)
    await call.message.delete()


@dp.callback_query_handler(text = "nazad100")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mi11.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
xiomi mi 11 Lite
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Bluetooth standarti: 5.1
Old Kamera: 20 МП
Orqa kamera: 48 МП, 8 МП, 5 МП
Vazn: 196 г
Batareya quvvati: 4520 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.67"
Protsessor: Qualcomm Snapdragon 870 5G
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
hozirda narxi:5 281 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back2 )
    await call.message.delete()
 

@dp.callback_query_handler(text = "nazad101")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mi10tpro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
xiomi mi 10t pro
Ekran yangilanish chastotasi: 144 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Operatsion tizim versiyasi: Android 10
Protsessor: Qualcomm Snapdragon 865
NFC: Есть
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
Bluetooth standarti: 5.1
Old Kamera: 20 МП
Orqa kamera: 108 МП, 13 МП, 5 МП
Vazn: 218 г
Batareya quvvati: 5000 мА⋅ч
Korpus materiali: металл и стекло
Ekran tomonlari nisbati: 20:9
Ekran piksellari o'lchamlari: 2400x1080
Ekran texnologiyasi: IPS
Ekran o'lchami: 6.67"
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Xiaomi
hozirda narxi:6 241 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back200 )
    await call.message.delete()
 

@dp.callback_query_handler(text = "nazad102")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/pocof3.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Poco F3
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 20 МП
Orqa kamera: 48 МП, 8 МП, 5 МП
Vazn: 196 г
Batareya quvvati: 4520 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.67"
Protsessor: Qualcomm Snapdragon 870 5G
Doimiy xotira hajmi: 256 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Xiaomi
xozirda narxi:4 410 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back201 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad103")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mi10t.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Mi 10T
Ekran yangilanish chastotasi: 144 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Protsessor: Qualcomm Snapdragon 865
Operatsion tizim versiyasi: Android 10
Aloqa standarti: 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 20 МП
Orqa kamera: 64 МП, 13 МП, 5 МП
Vazn: 216 г
Batareya quvvati: 5000 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran o'lchami: 6.67"
Ekran texnologiyasi: IPS
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
xozirda narxi:6 200 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back202 )
    await call.message.delete()


@dp.callback_query_handler(text = "nazad104")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/minot10.jpeg','rb'),
        caption = """
xiomi not 10
Protsessor: Qualcomm Snapdragon 678
Ekran yangilanish chastotasi: 60 Гц
Korpus materiali: стекло и пластик
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Himoya darajasi: IP53
Operatsion tizim versiyasi: Android 11
Xotira kartasi sloti: Есть
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Bluetooth standarti: 5.0
Old Kamera: 13 МП
Orqa kamera: 48 МП, 8 МП, 2 МП, 2 МП
Vazn: 179 г
Batareya quvvati: 5000 мА⋅ч
Ekran texnologiyasi: Super AMOLED
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran o'lchami: 6.43"
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 4 ГБ
Brend: Xiaomi
xozirda narxi:2 341 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back203 )
    await call.message.delete()
  
@dp.callback_query_handler(text = "nazad105")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not10pro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Redmi not 10 pro
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Himoya darajasi: IP53
Protsessor: Qualcomm Snapdragon 732G
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Xotira kartasi sloti: Есть
Bluetooth standarti: 5.1
Old Kamera: 16 МП
Orqa kamera: 108 МП, 8 МП, 5 МП, 2 МП
Vazn: 193 г
Batareya quvvati: 5020 мА⋅ч
Korpus materiali: стекло и пластик
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.67"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
xozirda narxi:2 712 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back204 )
    await call.message.delete()

@dp.callback_query_handler(text = "nazad106")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/pocox3.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
xiomi poco x3
Ekran yangilanish chastotasi: 120 Гц
SIM-kartalar soni: 2
SIM-karta formati: nano SIM
Himoya darajasi: IP53
NFC: Есть
Xotira kartasi maksimal hajmi: 256ГБ
Xotira kartasi sloti: Есть
Korpus materiali: пластик
Bluetooth standarti: 5.1
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Ekran tomonlari nisbati: 20:9
Operatsion tizim versiyasi: Android 10
Protsessor: Qualcomm Snapdragon 732G
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 2400x1080
Old Kamera: 20 МП
Orqa kamera: 64 МП, 13 МП, 2 МП
Vazn: 215 г
Batareya quvvati: 5160 мА⋅ч
Ekran o'lchami: 6.67"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
xozirda narxi:2 726 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back205 )
    await call.message.delete()

@dp.callback_query_handler(text = "nazad107")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/mi9t.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Redmi 9T
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
NFC: Есть
Korpus materiali: пластик
Bluetooth standarti: 5.0
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Operatsion tizim versiyasi: Android 10
Protsessor: Qualcomm Snapdragon 662
Old Kamera: 2 МП
Orqa kamera: 48 МП, 8 МП, 2 МП, 2 МП
Vazn: 198 г
Batareya quvvati: 6000 мА⋅ч
Ekran tomonlari nisbati: 19.5:9
Ekran piksellari o'lchamlari: 2340x1080
Ekran texnologiyasi: IPS
Ekran o'lchami: 6.53
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 4 ГБ
Brend: Xiaomi
xozirda narxi:2 019 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back206 )
    await call.message.delete()
  
@dp.callback_query_handler(text = "nazad108")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/not9pro.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Redmi not 9 pro
Ekran yangilanish chastotasi: 60 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Protsessor: Qualcomm Snapdragon 720G
Operatsion tizim versiyasi: Android 10
Xotira kartasi sloti: Есть
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 2400x1080
Ekran tomonlari nisbati: 20:9
Aloqa standarti: 3G, 4G LTE, VoLTE, GSM 900/1800/1900
Korpus materiali: стекло и пластик
Bluetooth standarti: 5.0
Old Kamera: 16 МП
Orqa kamera: 64 МП, 8 МП, 5 МП, 2 МП
Vazn: 209 г
Batareya quvvati: 5020 мА⋅ч
Ekran o'lchami: 6.67"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 6 ГБ
Brend: Xiaomi
hozirda narxi:2 763 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back207 )
    await call.message.delete()

@dp.callback_query_handler(text = "nazad109")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/minot9.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
Xiomi Redmi not 9
Ekran yangilanish chastotasi: 60 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Operatsion tizim versiyasi: Android 10
Xotira kartasi sloti: Есть
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 2340x1080
Ekran tomonlari nisbati: 19.5:9
Aloqa standarti: 3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900
Korpus materiali: стекло и пластик
Bluetooth standarti: 5.0
Old Kamera: 13 МП
Orqa kamera: 48 МП, 8 МП, 2 МП, 2 МП
Vazn: 199 г
Batareya quvvati: 5020 мА⋅ч
Ekran o'lchami: 6.53"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 3 ГБ
Brend: Xiaomi
hozirda narxi 1 990 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back208 )
    await call.message.delete()



# vivo ???????????????????????????????????????????????????????????????????????????????????????????????
@dp.callback_query_handler(text = "nazad11")
async def UZB(call:CallbackQuery):
    await call.message.answer("Assalomu alaykum\nTelefon bozorga xush kelibsiz\nIltimos telefon turini tanlang!",reply_markup = tur)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad64")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung Z seria TURINI TANLANG!",reply_markup = z_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad65")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung Z seria TURINI TANLANG!",reply_markup = z_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad66")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung Z seria TURINI TANLANG!",reply_markup = z_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad71")
async def UZB(call:CallbackQuery):
    await call.message.answer("Samsung Z seria TURINI TANLANG!",reply_markup = z_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad67")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/zfold3.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy z fold 3
Стандарт связи: 3G, 4G LTE, 5G, GSM 900/1800
NFC: Есть
Стандарт Bluetooth: 5.2
Материал корпуса: алюминий
Версия ОС: Android 11
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Тип экрана: Dynamic AMOLED 2X
Разрешение экрана: 2208x1768
Процессор: Qualcomm Snapdragon 888
Фронтальная камера: 10 МП
Основная камера: 12 МП, 12 МП, 12 МП
Вес: 271 г
Емкость аккумулятора: 4400 мА⋅ч
Диагональ экрана: 7.6"
Объем встроенной памяти: 512 ГБ
Объем оперативной памяти: 12 ГБ
Бренд: Samsung
hozirda narxi:17 055 000""",reply_markup = zfold3_back )
    await call.message.delete()

    
@dp.callback_query_handler(text = "nazad68")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/zflip3.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy z flip 3
Частота обновления экрана: 120 Гц
Тип SIM-карты: nano SIM+eSIM
Количество SIM-карт: 2
Версия ОС: Android 11
Процессор: Qualcomm Snapdragon 888
NFC: Есть
Стандарт связи: 3G, 4G LTE, 5G, GSM 900/1800/1900
Стандарт Bluetooth: 5.0
Фронтальная камера: 10 МП
Основная камера: 12 МП, 12 МП
Вес: 183 г
Материал корпуса: алюминий
Емкость аккумулятора: 3300 мА⋅ч
Разрешение экрана: 2640х1080
Соотношение сторон экрана: 22:9
Диагональ экрана: 6.7"
Тип экрана: AMOLED
Объем встроенной памяти: 128 ГБ
Объем оперативной памяти: 8 ГБ
Бренд: Samsung
hozirda narxi:9 000 000""",reply_markup = zflip3_back )
    await call.message.delete()

    
@dp.callback_query_handler(text = "nazad69")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/zfold2.jpeg','rb'),
        caption = """
        Hurmatli mijoz siz tanlagan 
samsung galaxy z flip 2
Бренд: Samsung
Объем оперативной памяти: 12 ГБ
Объем встроенной памяти: 256 ГБ
Диагональ экрана: 7.6"
Емкость аккумулятора: 4500 мА⋅ч
Вес: 282 г
Основная камера: 12 МП, 12 МП, 12 МП
Фронтальная камера: 10 МП
Процессор: Qualcomm Snapdragon 865 Plus
Разрешение экрана: 2208x1768
hozirda narxi:14 344 000""",reply_markup = zfold2_back)
    await call.message.delete()
    
@dp.callback_query_handler(text = "nazad70")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/zflip.jpg','rb'),
        caption = """Hurmatli mijoz siz tanlagan 
samsung galaxy z flip 2
Бренд: Samsung
Объем оперативной памяти: 12 ГБ
Объем встроенной памяти: 256 ГБ
Диагональ экрана: 7.6"
Емкость аккумулятора: 4500 мА⋅ч
Вес: 282 г
Основная камера: 12 МП, 12 МП, 12 МП
Фронтальная камера: 10 МП
Процессор: Qualcomm Snapdragon 865 Plus
Разрешение экрана: 2208x1768
hozirda narxi:7 144 000""",reply_markup = zflip_back)
    await call.message.delete()
    

@dp.callback_query_handler(text = "nazad15")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/vivomenu.jpeg','rb'),
        caption = "VIVO TURINI TANLANG!",reply_markup = vivo_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad110")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/vivomenu.jpeg','rb'),
        caption = "VIVO TURINI TANLANG!",reply_markup = vivo_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad111")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/vivomenu.jpeg','rb'),
        caption = "VIVO TURINI TANLANG!",reply_markup = vivo_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad112")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/vivomenu.jpeg','rb'),
        caption = "VIVO TURINI TANLANG!",reply_markup = vivo_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad113")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/vivomenu.jpeg','rb'),
        caption = "VIVO TURINI TANLANG!",reply_markup = vivo_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad114")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/vivomenu.jpeg','rb'),
        caption = "VIVO TURINI TANLANG!",reply_markup = vivo_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad115")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/vivomenu.jpeg','rb'),
        caption = "VIVO TURINI TANLANG!",reply_markup = vivo_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad116")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/vivomenu.jpeg','rb'),
        caption = "VIVO TURINI TANLANG!",reply_markup = vivo_menu)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad117")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/x60.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo x60
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Protsessor: Qualcomm Snapdragon 870 5G
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 32 МП
Orqa kamera: 48 МП, 13 МП, 13 МП
Vazn: 179 г
Batareya quvvati: 4200 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2376x1080
Ekran tomonlari nisbati: 19.5:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.56"
Doimiy xotira hajmi: 256 ГБ
Operativ xotira hajmi: 12 ГБ
Brend: Vivo
hozirda narxi:9 061 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back3 )
    await call.message.delete()

@dp.callback_query_handler(text = "nazad118")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/x50.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo x50
Ekran yangilanish chastotasi: 120 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Protsessor: Qualcomm Snapdragon 870 5G
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 32 МП
Orqa kamera: 48 МП, 13 МП, 13 МП
Vazn: 177 г
Batareya quvvati: 4200 мА⋅ч
Korpus materiali: металл и стекло
Ekran piksellari o'lchamlari: 2376x1080
Ekran tomonlari nisbati: 19.5:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.56"
Doimiy xotira hajmi: 256 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Vivo
hozirda narxi:6 061 000


Iltimos xotira turini tanlang👇👇👇""",reply_markup = back300 )
    await call.message.delete()
 
@dp.callback_query_handler(text = "nazad119")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/v21.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo v21
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Xotira kartasi sloti: Есть
Protsessor: MediaTek Dimensity 800
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900
NFC: Есть
Bluetooth standarti: 5.1
Old Kamera: 44 МП
Orqa kamera: 64 МП, 8 МП, 2 МП
Vazn: 177 г
Batareya quvvati: 4000 мА⋅ч
Ekran piksellari o'lchamlari: 2404x1080
Ekran tomonlari nisbati: 20:9
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.44"
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Vivo
hozirda narxi:4 527 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back301)
    await call.message.delete()
 
 
@dp.callback_query_handler(text = "nazad120")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/v20.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivi v20
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
NFC: Есть
Xotira kartasi sloti: Есть
Korpus materiali: стекло и пластик
Bluetooth standarti: 5.1
Operatsion tizim versiyasi: Android 11
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
Protsessor: Qualcomm Snapdragon 720G
Old Kamera: 44 МП
Orqa kamera: 64 МП, 8 МП, 2 МП
Vazn: 171 г
Batareya quvvati: 4000 мА⋅ч
Ekran tomonlari nisbati: 20:9
Ekran piksellari o'lchamlari: 2400x1080
Ekran texnologiyasi: AMOLED
Ekran o'lchami: 6.44"
Doimiy xotira hajmi: 128 ГБ
Operativ xotira hajmi: 8 ГБ
Brend: Vivo
hozirda narxi:4 220 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back302 )
    await call.message.delete()
 
 
@dp.callback_query_handler(text = "nazad121")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/y30.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo y30
Ekran yangilanish chastotasi: 60 Гц
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
NFC: Есть
Xotira kartasi maksimal hajmi: 256ГБ
Xotira kartasi sloti: Есть
Ekran texnologiyasi: IPS
Korpus materiali: пластик
Bluetooth standarti: 5.0
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
Protsessor: MediaTek Helio G35
Operatsion tizim versiyasi: Android 10
Old Kamera: 8 МП
Orqa kamera: 13 МП, 8 МП, 2 МП, 2 МП
Vazn: 197 г
Batareya quvvati: 5000 мА⋅ч
Ekran tomonlari nisbati: 19.5:9
Ekran piksellari o'lchamlari: 1560x720
Ekran o'lchami: 6.47"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 4 ГБ
Brend: Vivo
hozirda narxi:2 100 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back303)
    await call.message.delete()

@dp.callback_query_handler(text = "nazad122")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/y20.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivi y20
SIM-karta formati: nano SIM
SIM-kartalar soni: 2
Xotira kartasi sloti: Есть
Korpus materiali: пластик
Bluetooth standarti: 5.0
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
Protsessor: Qualcomm Snapdragon 460
Operatsion tizim versiyasi: Android 10
Old Kamera: 8 МП
Orqa kamera: 13 МП, 2 МП, 2 МП
Vazn: 192 г
Batareya quvvati: 5000 мА⋅ч
Ekran tomonlari nisbati: 20:9
Ekran piksellari o'lchamlari: 1600x720
Ekran texnologiyasi: IPS
Ekran o'lchami: 6.51"
Doimiy xotira hajmi: 64 ГБ
Operativ xotira hajmi: 4 ГБ
Brend: Vivo
hozirda narxi:2 000 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back304 )
    await call.message.delete()
 
@dp.callback_query_handler(text = "nazad123")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/y19.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivi y19
Brend: Vivo
Operativ xotira hajmi: 4 ГБ
Doimiy xotira hajmi: 32 ГБ
Ekran o'lchami: 6.51"
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 1600x720
Ekran tomonlari nisbati: 20:9
Batareya quvvati: 5000 мА⋅ч
Vazn: 191 г
Orqa kamera: 13 МП, 2 МП
Old Kamera: 8 МП
Operatsion tizim versiyasi: Android 10
Protsessor: MediaTek Helio G35
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
SIM-kartalar soni: 2
SIM-karta formati: nano SIM


Iltimos xotira turini tanlang👇👇👇""",reply_markup = back305 )
    await call.message.delete()
 
@dp.callback_query_handler(text = "nazad124")
async def UZB(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('image/y12s.jpeg','rb'),
        caption = """Hurmatli mijoz siz tanlagan
vivo y12s
Brend: Vivo
Operativ xotira hajmi: 3 ГБ
Doimiy xotira hajmi: 32 ГБ
Ekran o'lchami: 6.51"
Ekran texnologiyasi: IPS
Ekran piksellari o'lchamlari: 1600x720
Ekran tomonlari nisbati: 20:9
Batareya quvvati: 5000 мА⋅ч
Vazn: 191 г
Orqa kamera: 13 МП, 2 МП
Old Kamera: 8 МП
Operatsion tizim versiyasi: Android 10
Protsessor: MediaTek Helio G35
Aloqa standarti: 3G, 4G LTE, GSM 900/1800/1900
SIM-kartalar soni: 2
SIM-karta formati: nano SIM
hozirda narxi 1 819 000

Iltimos xotira turini tanlang👇👇👇""",reply_markup = back306 )
    await call.message.delete()

@dp.callback_query_handler(text = "umnazad")
async def UZB(call:CallbackQuery):
    await call.message.answer("Assalomu alaykum\nTelefon bozorga xush kelibsiz\nIltimos telefon turini tanlang!",reply_markup = tur)
    await call.message.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)