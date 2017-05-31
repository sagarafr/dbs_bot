from commands import Command
from main import db_ultimate


@Command()
def news(bot, update):
    'Give the last 10 news from dragon ball ultimate web site'
    db_ultimate.update()
    for article in db_ultimate.article_update:
        bot.sendMessage(chat_id=update.message.chat_id, text=article.link)
