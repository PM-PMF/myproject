# Generated by Django 4.0.5 on 2022-06-09 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='username',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 9, 10, 14, 41, 279978, tzinfo=utc)),
        ),
    ]