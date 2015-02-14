# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbirthapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateField(null=True)),
                ('temperature', models.IntegerField(max_length=3, blank=True)),
                ('weight', models.IntegerField(max_length=3, blank=True)),
                ('blood_pressure', models.CharField(max_length=50, blank=True)),
                ('mother', models.ForeignKey(to='betterbirthapp.Mother')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mother',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mother',
            name='height',
            field=models.IntegerField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mother',
            name='picture',
            field=models.FileField(null=True, upload_to=b'/images/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baby',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='baby',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='eventlog',
            name='event_type',
            field=models.CharField(max_length=2, choices=[(b'RC', b'Record Created'), (b'N', b'Note'), (b'V', b'Visit'), (b'DL', b'Delivered'), (b'DC', b'Deceased')]),
        ),
    ]
