from telebot import TeleBot, types
from worker import Worker

bot = TeleBot("513218671:AAEa3DbXTXMfV8HH70RCx3naz9An_Z45dVQ")
_worker = Worker(bot)

keyboard = types.ReplyKeyboardMarkup(True)
keyboard.row("❌Стереть❌", "✅Отправить✅")

@bot.message_handler(commands=["start"])
def command_handler(message):
    if message.chat.id == 497551952 or message.chat.id == 327793280:
        bot.send_message(message.chat.id, "Выберите команду", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Тебе сюда нельзя😏")

@bot.message_handler(commands=["stat"])
def stat_handler(message):
    if message.chat.id == 497551952 or message.chat.id == 327793280:
        _worker.StatCommand()

@bot.message_handler(content_types=["photo", "audio", "document", "sticker", "video", "contact", "voice"])
def handle_other_types(message):
    _worker.Counter(message.from_user.id)

@bot.message_handler(content_types=["text"])
def handle_message(message):
    if message.chat.id == 497551952 or message.chat.id == 327793280:
        if message.text == "❌Стереть❌":
            _worker.ClearDB(message.from_user.id)
        elif message.text == "✅Отправить✅":
            _worker.SendStat(message.from_user.id)
        return
    if message.chat.id == -1001257615874:
        _worker.Counter(message.from_user.id)

bot.polling(none_stop=True)