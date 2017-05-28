from configuration.basic_configuration import BasicConfiguration
from admin.admin import admin
from panda_stream.panda_stream_parser import PandaStreamParser


config_file = BasicConfiguration('./resources/configuration.ini')
admin_grp = admin(config_file.admins)
panda_stream = PandaStreamParser()


def main():
    from app import App
    app = App(config_file.token)
    app.run()


if __name__ == '__main__':
    main()
