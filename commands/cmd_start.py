from commands import Command


@Command()
def start(bot, update):
    'Check if the bot is alive'
    bot.sendMessage(chat_id=update.message.chat_id, text="start")
