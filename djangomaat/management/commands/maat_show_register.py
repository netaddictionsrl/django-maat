from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.db.models.loading import get_model

from ...register import maat

class Command(BaseCommand):
    help = "Shows all registered handlers."

    def handle(self, *args, **options):
        
        handlers = maat.get_registered_handlers()

        if not handlers:
            self.stdout.write('No registered handlers found.\n')

        for handler in handlers:
            self.stdout.write(u'%s\n' % handler)