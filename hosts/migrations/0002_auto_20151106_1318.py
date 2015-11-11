# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='os',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='type',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
