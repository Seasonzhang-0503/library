# Generated by Django 3.2.7 on 2023-03-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_theborrow_theborrow_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thebook',
            name='theBook_id',
            field=models.CharField(max_length=500, verbose_name='图书编号(备用)'),
        ),
        migrations.AlterField(
            model_name='thebook',
            name='theBook_logo',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='images/', verbose_name='图书照片1'),
        ),
        migrations.AlterField(
            model_name='thebook',
            name='theBook_name',
            field=models.CharField(max_length=500, verbose_name='图书名称'),
        ),
        migrations.AlterField(
            model_name='thebook',
            name='theBook_status1',
            field=models.CharField(choices=[('已借订', '已借订'), ('未借订', '未借订')], max_length=500, verbose_name='图书状态1'),
        ),
        migrations.AlterField(
            model_name='thebook',
            name='theBook_type',
            field=models.CharField(choices=[('电子书', '电子书'), ('纸质书', '纸质书')], max_length=500, verbose_name='电子书/纸质书'),
        ),
        migrations.AlterField(
            model_name='theborrow',
            name='theBorrow_datetime',
            field=models.DateTimeField(max_length=500, verbose_name='借订日期'),
        ),
    ]
