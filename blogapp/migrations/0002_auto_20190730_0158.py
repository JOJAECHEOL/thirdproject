# Generated by Django 2.1.8 on 2019-07-29 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pup_date',
            new_name='pub_date',
        ),
    ]
