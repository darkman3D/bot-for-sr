import telebot
import config
import markups as m
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    text = message.text
    bot.send_photo(chat_id, photo='https://imgur.com/hxQn7Ob')
    msg = bot.send_message(chat_id, 'Здравствуй, абитуриент! Ты стоишь на пороге одного из лучших учебных заведений Макеевки - "Макеевский политехнический колледж".''', reply_markup=m.open_markup)
    bot.register_next_step_handler(msg, open_hall)


@bot.message_handler(content_types=['text', 'photo'])
def open_hall(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == 'Войти😁':
        bot.send_photo(chat_id, photo='https://i.imgur.com/H65riQH.jpg')
        mg = bot.send_message(chat_id, '''Ты стоишь в холле колледжа. Зачем ты сюда пришел и что собрался делать, меня не интересует, раз пришел - значит нужно.
Справа от тебя закрытый гардероб, слева стена объявлений с разной информацией. Ты поднимаешься по трем ступенькам и видишь на 3 часа вахту и бухгалтерию. 
Слева лестница для передвижения между этажами и длинный коридор спереди.
Куда отправишься, друг?''', reply_markup=m.source_markup)
        bot.register_next_step_handler(mg, start_hall)

# Выбор движения на лестнице 1 этажа:
def start_hall(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == 'Второй этаж':
        bot.send_photo(chat_id, photo='https://i.imgur.com/7H2VNIe.jpg')
        bot.send_photo(chat_id, photo='https://i.imgur.com/vh4ZUF7.jpg')
        msg = bot.send_message(chat_id, '''На этом этаже кроме учебных аудиторий находится огромная библиотека, приемная и спортзал. Куда хочешь заглянуть?''', reply_markup=m.chose_markup)
        bot.register_next_step_handler(msg, second_floor)
    elif message.text == 'Коридор':
        bot.send_photo(chat_id, photo='https://i.imgur.com/w9wH9Ay.jpg')
        msg = bot.send_message(chat_id, '''На этом этаже находится отдел кадров, (10) кабинет конструкций путевых и строительных машин. Технического обслуживания и ремонта дорог, 
(14) кабинет строительных материалов и изделий. Основ инженерной геологии при производстве работ на строительной площадке и секретные мастерские,
которые ты не увидешь, но не факт :) ''', reply_markup=m.first_floor_markup)
        bot.register_next_step_handler(msg, Kabibi)


def Kabibi(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == '10 кабинет':
        bot.send_photo(chat_id, photo='https://i.imgur.com/WzzFUlb.jpg')
        ms1 = bot.send_message(chat_id, 'Кабинет наглядно описывающий основные принципы работы строительных машин. При желании миниатюры можно даже потрогать, они полностью рабочие', reply_markup=m.return_markup)
        bot.register_next_step_handler(ms1, returne)
    elif message.text == '14 кабинет':
        bot.send_photo(chat_id, photo='https://i.imgur.com/aalJQAW.jpg')
        ms = bot.send_message(chat_id, 'Комната, стены которой обвешены различными строительными материалами: синтетикой, керамикой, металлами и это не все, что еще есть в аудитории.', reply_markup=m.iventinpodv_markup)
        bot.send_message(chat_id, 'Ты cлышишь свое имя')
        bot.register_next_step_handler(ms, ivent_in_podval)
    elif message.text == 'Обратно':
        gg = bot.send_message(chat_id, 'Куда дальше?', reply_markup=m.source_markup)
        bot.register_next_step_handler(gg, start_hall)


def ivent_in_podval(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == 'Пойти на голос':
        bot.send_photo(chat_id, photo='https://i.imgur.com/h4aGzot.jpg')
        mg = bot.send_message(chat_id, '''Подойдя к неизвестной фигуре, она спрашивает тебя, в какую мастерскую ты хочешь отправиться?
Какую ты выбираешь?''', reply_markup=m.podval_markup)
        bot.register_next_step_handler(mg, podval)
    elif message.text == 'Уйти обратно в холл':
        mm = bot.send_message(chat_id, 'Наверное показалось', reply_markup=m.first_floor_markup)
        bot.register_next_step_handler(mm, Kabibi)


def podval(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == 'Строительную':
        bot.send_photo(chat_id, photo='https://i.imgur.com/BhaG8bG.jpg')
        mg = bot.send_message(chat_id, 'Огромная комната длиной 15 метров оснащенная разнообразным оборудованием, несколькими видами прессов, весов и методическими указаниями по использованию на стенах', reply_markup=m.return_markup)
        bot.register_next_step_handler(mg, returne2)
    elif message.text == 'Механическую':
        bot.send_photo(chat_id, photo='https://i.imgur.com/qpQX0KL.jpg')
        ms = bot.send_message(chat_id, 'Только зайдя в эту комнату, сразу бросается в глаза разобранная "буханка" и еще несколько двигателей. Здорово, правда!?', reply_markup=m.return_markup)
        bot.register_next_step_handler(ms, returne2)
    elif message.text =='Вернуться назад':
        mg = bot.send_message(chat_id, 'Ухожу',reply_markup=m.first_floor_markup)
        bot.register_next_step_handler(mg, Kabibi)


def returne2(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == 'Вернуться назад':
        m1 = bot.send_message(chat_id, 'Куда дальше ?', reply_markup=m.podval_markup)
        bot.register_next_step_handler(m1, podval)
    return


def returne(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == 'Вернуться назад':
        m1 = bot.send_message(chat_id, 'Куда дальше ?', reply_markup=m.first_floor_markup)
        bot.register_next_step_handler(m1, Kabibi)
    return


def second_floor(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == 'Библиотека':
        mg = bot.send_message(chat_id, 'Вот оно, хранилище всех знаний техникума, такой библиотекой не могла похвастаться даже древняя Александрия.', reply_markup=m.return_markup)
        bot.send_photo(chat_id, photo='https://i.imgur.com/q4vWAI0.jpg')
        bot.send_photo(chat_id, photo='https://i.imgur.com/180xJrY.jpg')
        bot.register_next_step_handler(mg, second_returne)
    elif message.text == 'Приемная':
        mm = bot.send_photo(chat_id, photo='https://i.imgur.com/LsA46rt.jpg', reply_markup=m.return_markup)
        bot.send_message(chat_id, 'Главное место во всем техникуме, тут распологаются директор и заместитель директора.')
        bot.register_next_step_handler(mm, second_returne)
    elif message.text =='Первый этаж':
        gm = bot.send_message(chat_id, 'Спускаюсь', reply_markup=m.source_markup)
        bot.register_next_step_handler(gm, start_hall)

# уход с этажа или оставние и выбор
def second_returne(message):
    chat_id = message.chat.id
    text = message.text
    if message.text == 'Вернуться назад':
        mmg = bot.send_message(chat_id, 'Куда хочешь?', reply_markup=m.chose_markup)
        bot.register_next_step_handler(mmg, second_floor)


bot.polling()
