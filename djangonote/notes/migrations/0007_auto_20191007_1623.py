# Generated by Django 2.2.5 on 2019-10-07 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20191007_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user2',
            new_name='user',
        ),
    ]
