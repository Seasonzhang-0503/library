# Generated by Django 3.2.13 on 2023-04-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0034_delete_newmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dept',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='部门'),
        ),
    ]
