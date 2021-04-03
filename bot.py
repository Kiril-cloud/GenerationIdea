import telebot


bot = telebot.TeleBot('1669270082:AAEETxmFXtqGYAOB8M1DenfMQDMY0bHTY2M')


@bot.message_handler(commands = ['start', 'help'])
def start():
	bot.send_message(message.chat.id, 'Привет')
	
	
bot.polling()