# Generated by Django 3.2.7 on 2023-04-03 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0026_auto_20230403_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobilenumber',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='电话号码'),
        ),
    ]
