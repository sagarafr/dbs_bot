from telegram.ext import Updater
from commands import Command
from commands import Message


class App(object):
    def __init__(self, token: str):
        self._command = Command()
        self._message = Message()
        self._updater = Updater(token)

    def run(self):
        self.command.init_dispatcher(self.updater)
        self.message.init_dispatcher(self.updater)
        self.updater.start_polling()
        self.updater.idle()

    @property
    def command(self):
        return self._command

    @property
    def message(self):
        return self._message

    @property
    def updater(self):
        return self._updater
