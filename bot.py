import telebot
bot=telebot.TeleBot('933896975:AAGyUkazBbaq3cvrU88-YbBP4P2XPYwOQK0')
keybord1=telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('Hi','Bye')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Погнали',reply_markup=keybord1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text=='Hi':
        bot.send_message(message.chat.id, 'Привет мой создатиль')
    elif message.text=='Bye':
        bot.send_message(message.chat.id, 'Пока мой создатиль')


bot.polling()
