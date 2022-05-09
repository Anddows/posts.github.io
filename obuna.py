import telebot
 
from telebot import types
 
bot = telebot.TeleBot("5311576722:AAFGbcfuGNgHLOKu5EH1yLp0nslNr3qnvaw")
 
 
@bot.message_handler(commands=['start'])
def welcome(message):
 
    # Keyboard
    button_hi = types.KeyboardButton("СТАРТ")
    start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_kb.add(button_hi)
 
    bot.send_message(message.chat.id, "Описание работы бота\nИтак нажмите кнопку <b>«СТАРТ»</b> и следуйте инструкциям!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=start_kb)
 
 
@bot.message_handler(content_types=['text'])
def send_message(message):
    button_next = types.KeyboardButton("ПРОДОЛЖИТЬ")
    next_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    next_kb.add(button_next)
    if message.chat.type == 'private':
        if message.text == "СТАРТ":
            bot.send_message(message.chat.id, "✉️ @Code_Idea_PerCode kanaliga obuna bo'ling", reply_markup=next_kb)
        elif message.text == 'ПРОДОЛЖИТЬ':
            button_next2 = types.KeyboardButton("К 2-МУ КАНАЛУ")
            next_kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            next_kb2.add(button_next2)
            status = ['creator', 'administrator', 'member']

            for chri in status:
                if chri == bot.get_chat_member('@code_idea_percode', message.from_user.id).status:
                    bot.send_message(message.chat.id, text = "Подписка подтверждена!")
                    break
            else:
                  bot.send_message(message.chat.id, "Кажется вы не подписались!")
        else:
                bot.send_message(message.chat.id, "Я не знаю что ответить")
 
 
# RUN
bot.polling(none_stop=True)