# Generated by Django 4.2 on 2023-07-03 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_user_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]