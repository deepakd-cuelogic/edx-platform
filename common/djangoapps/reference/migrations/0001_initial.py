# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ref_name', models.CharField(max_length=30)),
                ('ref_type', models.CharField(default='link', max_length=15, choices=[('image', 'IMAGE'), ('video', 'VIDEO'), ('link', 'LINK'), ('document', 'DOCUMENT')])),
                ('ref_link', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('ref_desc', models.CharField(max_length=30)),
                ('ref_status', models.CharField(default='is_alive', max_length=10, choices=[('is_alive', 'IS ALIVE'), ('not_available', 'NOT AVAILABLE')])),
            ],
        ),
    ]
