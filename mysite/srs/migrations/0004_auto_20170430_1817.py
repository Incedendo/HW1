# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0003_auto_20170427_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('FridayWorkshop', models.CharField(max_length=30)),
                ('SaturdayWorkshop', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='card_number',
            field=models.CharField(max_length=16, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='expiration_MM',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='expiration_YY',
            field=models.CharField(max_length=4, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='job_title',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='payment_method',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=2, default=1, choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('DC', 'DC'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='street_address',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='work_phone',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='zip',
            field=models.CharField(max_length=5, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
