from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PROJECT.accounts'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this
    def ready(self):
        import users.signals  # noqa