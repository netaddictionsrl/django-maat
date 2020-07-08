from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
try:
    from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:
    # Django < 1.9
    from django.contrib.contenttypes.generic import GenericForeignKey
from django.db import models

try:
    from django.utils.encoding import python_2_unicode_compatible
except ImportError:
    # Django > 2
    def python_2_unicode_compatible(klass):
        """
        A decorator that defines __unicode__ and __str__ methods under Python 2.
        Under Python 3 it does nothing.

        To support Python 2 and 3 with a single code base, define a __str__ method
        returning text and apply this decorator to the class.
        """
        return klass

@python_2_unicode_compatible
class MaatRanking(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    typology = models.CharField(max_length=255, db_index=True)
    usable = models.BooleanField(default=False)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        # This index is fundamental to avoid MySQL filesorting.
        # The first portion of the index is used to filter rows and, being
        # constant, the second can be used to order:
        # http://dev.mysql.com/doc/refman/5.0/en/order-by-optimization.html
        unique_together = ('content_type', 'typology', 'usable', 'position')

    def __str__(self):
        return 'Rank for {}'.format(self.content_object)
