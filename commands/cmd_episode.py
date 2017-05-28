from commands import Command
from requests import get
from main import panda_stream


@Command(pass_args=True)
def episode(bot, update, args):
    'List a episode. Use: /episode dbs number'
    if len(args) == 2:
        if str(args[0]).lower() == "dbs":
            response = get("http://panda-streaming.net/dragon-ball-super-{}-vostfr/".format(args[1]))
            if response.status_code == 200:
                panda_stream.clear_dbs()
                panda_stream.dbs_feed(response.text)
                for link in panda_stream.dbs_episodes_links[:-1]:
                    bot.sendMessage(chat_id=update.message.chat_id, text="{}".format(link))
            else:
                bot.sendMessage(chat_id=update.message.chat_id, text="Error {}".format(response.status_code))
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text="Bad first argument")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Have no argument")
