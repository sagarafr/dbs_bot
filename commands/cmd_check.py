from telegram.ext import Job
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
                information = panda_stream.get_dbs_last_information()
                if information is not None:
                    bot.sendMessage(chat_id=update.message.chat_id, text='\n'.join(information))
                job_queue.put(Job(callback=check_dbs_information, interval=5 * 60, repeat=True, context=update.message.chat_id))
                bot.sendMessage(chat_id=update.message.chat_id, text="Check on {}".format(args[0]))
            else:
                bot.sendMessage("Check already on {}".format(args[0]))
        else:
            bot.sendMessage("Don't found {}".format(args[0]))
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Have no argument")


def check_dbs_information(bot, job):
    information = panda_stream.get_dbs_last_information()
    if information is not None:
        bot.sendMessage(chat_id=job.context, text='\n'.join(information))
