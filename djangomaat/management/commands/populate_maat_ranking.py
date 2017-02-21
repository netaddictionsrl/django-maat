from __future__ import unicode_literals

from django.core.management.base import BaseCommand
try:
    from django.apps import apps
    get_model = apps.get_model
except ImportError:
    # Django < 1.9
    from django.db.models import get_model

from djangomaat.register import maat


class Command(BaseCommand):
    args = '[<app_label.model_name app_label.model_name ...>]'
    help = "Delete the old ranking and store the new ones."

    def add_arguments(self, parser):
        parser.add_argument('models', nargs='*', type=str)
        
        parser.add_argument(
            '--simulate',
            action='store_true',
            dest='simulate',
            default=False,
            help='Simulation mode'
        )

    def _parse(self, model):
        """
        Parse a string like
            app_label.model_name:typology1,typology2
        into a tuple
            (app_label, model_name, [typology1, typology2])

        Typologies are not mandatory unless a colon char is in the string.
        """
        bits = model.split(':')
        app_label, model_name = bits[0].split('.')
        typologies = None
        if len(bits) > 1:
            typologies = [bit.strip() for bit in bits[1].split(',')]
            if not typologies:
                raise SyntaxError('Missing typologyes values after colon')
        return app_label, model_name, typologies

    def handle(self, *models, **options):
        simulate = options['simulate']
        verbosity = options['verbosity']

        if verbosity > 0:
            logger = self.stdout
        else:
            logger = None

        models = models or options.get('models')

        if models:
            for model in models:
                app_label, model_name, typologies = self._parse(model)
                model_obj = get_model(app_label, model_name)
                handler = maat.get_handler_for_model(model_obj)
                handler.flush_ordered_objects(
                    typologies=typologies,
                    logger=logger,
                    simulate=simulate
                )
        else:
            handlers = maat.get_registered_handlers()

            if not handlers and verbosity > 0:
                self.stdout.write('No registered handlers found.\n')

            for handler in handlers:
                handler.flush_ordered_objects(logger=logger, simulate=simulate)
