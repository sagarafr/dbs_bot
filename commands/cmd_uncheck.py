from commands import Command
from main import admin_grp


@Command(pass_job_queue=True, pass_args=True)
@admin_grp
def uncheck(bot, update, job_queue, args):
    'Unckeck the animate in argument. Available animate dbs'
    if len(args) == 1:
        if str(args[0]).lower() == "dbs":
            found = False
            for job in job_queue.jobs():
                if job.name == "check_dbs_information":
                    job.schedule_removal()
                    found = True
            if found:
                bot.sendMessage(chat_id=update.message.chat_id, text="Uncheck {}".format(args[0]))
            else:
                bot.sendMessage(chat_id=update.message.chat_id, text="Can't uncheck {}".format(args[0]))
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text="Don't found {}".format(args[0]))
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Have no argument")
