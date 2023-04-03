# Generated by Django 3.2.7 on 2023-03-31 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20230328_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theuser',
            name='theUser_id',
            field=models.CharField(max_length=500, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='theuser',
            name='theUser_name',
            field=models.CharField(max_length=500, verbose_name='用户名称'),
        ),
        migrations.AlterField(
            model_name='theuser',
            name='theUser_password',
            field=models.CharField(max_length=500, verbose_name='用户密码'),
        ),
        migrations.AlterField(
            model_name='theuser',
            name='theUser_phone',
            field=models.CharField(max_length=500, verbose_name='用户电话'),
        ),
        migrations.AlterField(
            model_name='theuser',
            name='theUser_status1',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=500, verbose_name='用户状态1'),
        ),
    ]
