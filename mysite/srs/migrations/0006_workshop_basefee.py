# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0005_auto_20170430_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='basefee',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
    ]
