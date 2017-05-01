# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('organization', models.CharField(max_length=30)),
                ('job_title', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.IntegerField()),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('work_phone', models.IntegerField()),
                ('payment_method', models.CharField(max_length=30)),
                ('card_number', models.IntegerField()),
                ('expiration_MM', models.IntegerField()),
                ('expiration_YY', models.IntegerField()),
            ],
        ),
    ]
