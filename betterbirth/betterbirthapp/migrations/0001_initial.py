# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('date_of_birth', models.DateField()),
                ('status', models.CharField(max_length=2, choices=[(b'U', b'Unborn'), (b'LB', b'Live birth'), (b'SB', b'Still birth'), (b'DC', b'Deceased')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_type', models.CharField(max_length=2, choices=[(b'RC', b'Record Created'), (b'N', b'Note'), (b'DL', b'Delivered'), (b'DC', b'Deceased')])),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mother',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=2, choices=[(b'P', b'Pregnant'), (b'DL', b'Delivered'), (b'DC', b'Deceased')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eventlog',
            name='mother',
            field=models.ForeignKey(to='betterbirthapp.Mother'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventlog',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
