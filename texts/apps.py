from django.apps import AppConfig


class TextsConfig(AppConfig):
    name = 'texts'

    def ready(self):
        try:
            import texts.signals
        except ModuleNotFoundError as err:
            print(err)
