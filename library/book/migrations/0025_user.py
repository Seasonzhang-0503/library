# Generated by Django 3.2.7 on 2023-04-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0024_delete_userplus'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('mobilenumber', models.CharField(max_length=500, verbose_name='电话号码')),
            ],
        ),
    ]
