# Generated by Django 3.2.13 on 2023-04-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0037_auto_20230411_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('permission', models.CharField(max_length=64, verbose_name='权限')),
            ],
        ),
    ]
