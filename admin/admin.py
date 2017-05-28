from functools import wraps


def admin(user_group):

    def group_restriction(func):

        @wraps(func)
        def wrapper(bot, update, *args, **kwargs):
            from main import config_file

            # extract user_id from arbitrary update
            try:
                user_id = update.message.from_user.id
            except (NameError, AttributeError):
                try:
                    user_id = update.inline_query.from_user.id
                except (NameError, AttributeError):
                    try:
                        user_id = update.chosen_inline_result.from_user.id
                    except (NameError, AttributeError):
                        try:
                            user_id = update.callback_query.from_user.id
                        except (NameError, AttributeError):
                            print("No user_id available in update.")
                            return

            if config_file.trust_admin_in_chan:
                for admin_info in bot.get_chat_administrators(update.message.chat_id):
                    admin_id = admin_info.user.id
                    if admin_id not in user_group:
                        user_group.append(admin_id)

            if user_id not in user_group:
                print(user_id, user_group, user_id in user_group)
                print("Unauthorized access denied : ", user_id)
                return
            return func(bot, update, *args, **kwargs)
        return wrapper
    return group_restriction
