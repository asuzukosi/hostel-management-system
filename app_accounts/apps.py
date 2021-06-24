from django.apps import AppConfig

# This app manages the default user model and all its functionality
class AppAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_accounts'
