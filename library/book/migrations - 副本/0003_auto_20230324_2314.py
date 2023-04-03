# Generated by Django 3.2.7 on 2023-03-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20230324_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('location_id', models.CharField(blank=True, max_length=500, null=True, verbose_name='地点编号')),
                ('location_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='地点名称')),
            ],
            options={
                'verbose_name': '地点',
                'verbose_name_plural': '地点',
            },
        ),
        migrations.AlterField(
            model_name='thebook',
            name='theBook_type',
            field=models.CharField(blank=True, choices=[('电子书', '电子书'), ('纸质书', '纸质书')], max_length=500, null=True, verbose_name='电子书/纸质书'),
        ),
    ]
