# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbirthapp', '0004_auto_20150214_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
    ]
