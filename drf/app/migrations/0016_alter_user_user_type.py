# Generated by Django 4.2 on 2023-07-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_category_alter_user_user_type_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('1', 'vendor'), ('2', 'employee'), ('3', 'Customer')], max_length=10),
        ),
    ]
