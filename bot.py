from telebot import TeleBot

bot = TeleBot("513218671:AAEa3DbXTXMfV8HH70RCx3naz9An_Z45dVQ")

@bot.message_handler(content_types=["text"])
	def handle_message(message):
		if message.chat.id == 497551952:
			bot.send_message(-1001257615874, message.text)
bot.polling(none_stop=True)