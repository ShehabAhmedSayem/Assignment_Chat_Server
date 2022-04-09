from django.contrib.staticfiles.management.commands.runserver import Command as RunCommand
from django.core.management.base import CommandError
from django.conf import settings


class Command(RunCommand):
    def handle(self, *args, **options):
        port = '8000'
        if options['addrport']:
            if ':' in options['addrport']:
                port = options['addrport'].split(':')[1]
            else:
                port = options['addrport']
        else:
            options['addrport'] = '8000'
        settings.CHAT_SERVER_PORT = port
        super().handle(*args, **options)
        