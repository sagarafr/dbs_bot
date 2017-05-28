from telegram.ext import Job
from requests.exceptions import Timeout
from commands import Command
from utils.find_job import find_job
from main import admin_grp
from main import panda_stream


@Command(pass_job_queue=True, pass_args=True)
@admin_grp
def check(bot, update, job_queue, args):
    'Check the animate in argument. Available animate dbs'
    if len(args) == 1:
        if str(args[0]).lower() == "dbs":
            if not find_job(job_queue, "check_dbs_information"):
                try:
                    information = panda_stream.get_dbs_last_information()
                except Timeout:
                    bot.sendMessage(chat_id=update.message.chat_id, text="Request timeout")
                    return
                if information is not None:
                    bot.sendMessage(chat_id=update.message.chat_id, text="Information on the episode n°{}".format(panda_stream.last_dbs_episode))
                    bot.sendMessage(chat_id=update.message.chat_id, text='\n'.join(information))
                job_queue.put(Job(callback=check_dbs_information, interval=5 * 60, repeat=True, context=update.message.chat_id))
                bot.sendMessage(chat_id=update.message.chat_id, text="Check on {}".format(args[0]))
            else:
                bot.sendMessage(chat_id=update.message.chat_id, text="Check already on {}".format(args[0]))
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text="Don't found {}".format(args[0]))
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Have no argument")


def check_dbs_information(bot, job):
    try:
        information = panda_stream.get_dbs_last_information()
    except Timeout:
        bot.sendMessage(chat_id=job.context, text="Request timeout")
        return
    if information is not None:
        bot.sendMessage(chat_id=job.context, text="Information on the episode n°{}".format(panda_stream.last_dbs_episode))
        bot.sendMessage(chat_id=job.context, text='\n'.join(information))
