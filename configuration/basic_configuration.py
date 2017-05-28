from configparser import ConfigParser


class BasicConfiguration(object):
    def __init__(self, file):
        self._parser = ConfigParser()
        with open(file, 'r') as fd_file:
            self._parser.read_file(fd_file)
            self._admin = None if not self._parser.has_option('DEFAULT', 'admins') else [int(e) for e in self._parser['DEFAULT']['admins'].split(';') if str(e).isdigit()]
            self._trust_admin_in_chan = None
            if self._parser.has_option('DEFAULT', 'trust_admin_in_chan'):
                try:
                    self._trust_admin_in_chan = self._parser.getboolean('DEFAULT', 'trust_admin_in_chan')
                except ValueError:
                    self._trust_admin_in_chan = None

    @property
    def token(self):
        return None if not self._parser.has_option('DEFAULT', 'token') else str(self._parser['DEFAULT']['token'])

    @property
    def admins(self):
        return self._admin

    @property
    def trust_admin_in_chan(self):
        return self._trust_admin_in_chan
