from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from utils.get_module import get_module


class Command(object):
    _functions = {}
    _doc_functions = {}

    def __init__(self, pass_args=False, pass_update_queue=False,
                 pass_job_queue=False, pass_user_data=False,
                 pass_chat_data=False):
        self._tmp = {"pass_args": pass_args,
                     "pass_update_queue": pass_update_queue,
                     "pass_job_queue": pass_job_queue,
                     "pass_user_data": pass_user_data,
                     "pass_chat_data": pass_chat_data}

    def __call__(self, f, *args, **kwargs):
        from inspect import getdoc
        self._functions[f.__name__] = (f, self._tmp)
        self._doc_functions[f.__name__] = getdoc(f)
        return f

    def _help(self):
        def help(bot, update):
            bot.sendMessage(chat_id=update.message.chat_id, text='\n'.join(["/{} : {}".format(key, self._doc_functions[key]) for key in self._doc_functions if self._doc_functions[key] is not None]))
        return help

    def init_dispatcher(self, updater: Updater):
        dispatcher = updater.dispatcher
        for cmd in self._functions:
            tuple_function = self._functions[cmd]
            command_function = tuple_function[0]
            command_args = tuple_function[1]
            dispatcher.add_handler(CommandHandler(cmd, command_function, pass_args=command_args["pass_args"],
                                                  pass_update_queue=command_args["pass_update_queue"],
                                                  pass_job_queue=command_args["pass_job_queue"],
                                                  pass_user_data=command_args["pass_user_data"],
                                                  pass_chat_data=command_args["pass_chat_data"]))
        dispatcher.add_handler(CommandHandler("help", self._help()))


class Message(object):
    _functions = {}

    def __init__(self, allow_edited=False, pass_update_queue=False,
                 pass_job_queue=False, pass_user_data=False,
                 pass_chat_data=False, message_updates=True,
                 channel_posts_updates=True):
        self._tmp = {"allow_edited": allow_edited,
                     "pass_update_queue": pass_update_queue,
                     "pass_job_queue": pass_job_queue,
                     "pass_user_data": pass_user_data,
                     "pass_chat_data": pass_chat_data,
                     "message_updates": message_updates,
                     "channel_posts_updates": channel_posts_updates}

    def __call__(self, f, *args, **kwargs):
        self._functions[f.__name__] = (f, self._tmp)
        return f

    def init_dispatcher(self, updater: Updater):
        dispatcher = updater.dispatcher
        for cmd in self._functions:
            tuple_function = self._functions[cmd]
            command_function = tuple_function[0]
            command_args = tuple_function[1]
            dispatcher.add_handler(MessageHandler(Filters.command, command_function,
                                                  allow_edited=command_args["allow_edited"],
                                                  pass_update_queue=command_args["pass_update_queue"],
                                                  pass_job_queue=command_args["pass_job_queue"],
                                                  pass_user_data=command_args["pass_user_data"],
                                                  pass_chat_data=command_args["pass_chat_data"],
                                                  message_updates=command_args["message_updates"],
                                                  channel_posts_updates=command_args["channel_posts_updates"]))

__all__ = get_module(__path__)
