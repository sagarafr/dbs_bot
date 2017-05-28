from commands import Message


@Message()
def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Unknown command")
