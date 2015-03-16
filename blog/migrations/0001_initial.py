# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
