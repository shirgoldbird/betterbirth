# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbirthapp', '0003_baby_mother'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='status',
            field=models.CharField(max_length=2, choices=[(b'P', b'Pregnant'), (b'PP', b'Postpartum'), (b'DC', b'Deceased')]),
        ),
    ]
