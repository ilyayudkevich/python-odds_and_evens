from django.apps import AppConfig


class GameConfig(AppConfig):
    name = 'game'
    verbose_name = 'Game Application'

    def ready(self):
        import game.signals 

