# Generated by Django 2.2.4 on 2019-08-13 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='put_date',
            new_name='pub_date',
        ),
    ]
