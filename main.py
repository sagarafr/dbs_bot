from configuration.basic_configuration import BasicConfiguration
from admin.admin import admin

config_file = BasicConfiguration('./resources/configuration.ini')
admin_grp = admin(config_file.admins)


def main():
    from app import App
    app = App(config_file.token)
    app.run()


if __name__ == '__main__':
    main()
