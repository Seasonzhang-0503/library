# Generated by Django 3.2.7 on 2023-04-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0029_user_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='theUser_status1',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=500, verbose_name='用户状态1'),
        ),
    ]
