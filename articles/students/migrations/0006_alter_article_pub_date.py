# Generated by Django 4.0.5 on 2022-06-12 18:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 18, 51, 2, 829427, tzinfo=utc)),
        ),
    ]
