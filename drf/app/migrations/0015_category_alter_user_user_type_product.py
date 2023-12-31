# Generated by Django 4.2 on 2023-07-04 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_customuser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=500)),
                ('category_desc', models.CharField(default='', max_length=5000)),
                ('category_img', models.ImageField(default='', upload_to='images/')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('is_active', models.IntegerField(blank=True, choices=[(1, 'Active'), (0, 'Inactive')], default=1, help_text='1->Active, 0->Inactive', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('1', 'vendor'), ('2', 'employee')], max_length=10),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=500)),
                ('product_img', models.ImageField(default='', upload_to='images/')),
                ('product_desc', models.CharField(max_length=5000)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('is_active', models.IntegerField(blank=True, choices=[(1, 'Active'), (0, 'Inactive')], default=1, help_text='1->Active, 0->Inactive', null=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='app.category')),
            ],
        ),
    ]
