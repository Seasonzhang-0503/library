# Generated by Django 3.2.7 on 2023-04-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0027_auto_20230403_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='field1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='属性1'),
        ),
        migrations.AddField(
            model_name='user',
            name='field2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='属性2'),
        ),
        migrations.AddField(
            model_name='user',
            name='field3',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='属性3'),
        ),
        migrations.AddField(
            model_name='user',
            name='field4',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='属性4'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='角色'),
        ),
    ]