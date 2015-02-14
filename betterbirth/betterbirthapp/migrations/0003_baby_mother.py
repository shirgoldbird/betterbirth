# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbirthapp', '0002_auto_20150214_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='baby',
            name='mother',
            field=models.ForeignKey(to='betterbirthapp.Mother', null=True),
            preserve_default=True,
        ),
    ]
