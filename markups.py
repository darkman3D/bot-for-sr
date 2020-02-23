from telebot import types

open_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
open_markup_btn1 = types.KeyboardButton('Войти😁')
open_markup.add(open_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Второй этаж')
source_markup_btn2 = types.KeyboardButton('Коридор')
source_markup.add(source_markup_btn1, source_markup_btn2)

chose_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
chose_markup_btn1 = types.KeyboardButton('Библиотека')
chose_markup_btn2 = types.KeyboardButton('Приемная')
chose_markup_btn3 = types.KeyboardButton('Первый этаж')
chose_markup.add(chose_markup_btn1, chose_markup_btn2, chose_markup_btn3)

return_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
return_markup_btn = types.KeyboardButton('Вернуться назад')
return_markup.add(return_markup_btn)

first_floor_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
first_floor_markup_btn1 = types.KeyboardButton('Обратно')
first_floor_markup_btn2 = types.KeyboardButton('10 кабинет')
first_floor_markup_btn3 = types.KeyboardButton('14 кабинет')
first_floor_markup.add(first_floor_markup_btn1, first_floor_markup_btn2, first_floor_markup_btn3)


iventinpodv_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
iventinpodv_markup_btn1 = types.KeyboardButton('Пойти на голос')
iventinpodv_markup_btn2 = types.KeyboardButton('Уйти обратно в холл')
iventinpodv_markup.add(iventinpodv_markup_btn1, iventinpodv_markup_btn2)

podval_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
podval_markup_btn1 = types.KeyboardButton('Строительную')
podval_markup_btn2 = types.KeyboardButton('Механическую')
podval_markup_btn3 = types.KeyboardButton('Вернуться назад')
podval_markup.add(podval_markup_btn1, podval_markup_btn2, podval_markup_btn3)
