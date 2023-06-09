# Generated by Django 3.2.7 on 2023-04-03 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_auto_20230403_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theborrow',
            options={'verbose_name': '借订', 'verbose_name_plural': '借订'},
        ),
        migrations.RemoveField(
            model_name='theborrow',
            name='theBorrow_datetime',
        ),
        migrations.AddField(
            model_name='theborrow',
            name='theBorrow_add_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, max_length=500, verbose_name='创建日期'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theborrow',
            name='theBorrow_update_datetime',
            field=models.DateTimeField(auto_now=True, max_length=500, verbose_name='修改日期'),
        ),
    ]
