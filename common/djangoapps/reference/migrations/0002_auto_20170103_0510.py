# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referenceinfo',
            name='ref_status',
            field=models.CharField(default='is_alive', max_length=20, choices=[('is_alive', 'IS ALIVE'), ('not_available', 'NOT AVAILABLE')]),
        ),
        migrations.AlterField(
            model_name='referenceinfo',
            name='ref_type',
            field=models.CharField(default='link', max_length=30, choices=[('image', 'IMAGE'), ('video', 'VIDEO'), ('link', 'LINK'), ('document', 'DOCUMENT')]),
        ),
    ]
