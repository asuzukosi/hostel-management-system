from django.apps import AppConfig

# This is the application that handles the school processes 
# All the activities that handle the management of the school generally
class AppSchoolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_school'
