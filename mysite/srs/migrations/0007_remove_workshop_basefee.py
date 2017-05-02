# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0006_workshop_basefee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='basefee',
        ),
    ]
