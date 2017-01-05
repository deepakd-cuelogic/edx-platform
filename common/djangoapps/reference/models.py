from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator


LINK_TYPE_CHOICES = (
    ('image','IMAGE'),
    ('video', 'VIDEO'),
    ('link','LINK'),
    ('document','DOCUMENT'),
)

STATUS_CHOICES = (
    ('is_alive', 'IS ALIVE'),
    ('not_available', 'NOT AVAILABLE'),
)

class ReferenceInfo(models.Model):
    """
    Should create reference info.
    """
    ref_name = models.CharField(max_length=30)
    ref_type = models.CharField(max_length=30, choices=LINK_TYPE_CHOICES, default='link')
    ref_link = models.TextField(validators=[URLValidator()])
    ref_desc = models.CharField(max_length=30)
    ref_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='is_alive')

    def __str__(self):
        return unicode(self.ref_name)

    def get_absolute_url(self):
        return reverse('reference_edit', kwargs={'pk': self.pk})
