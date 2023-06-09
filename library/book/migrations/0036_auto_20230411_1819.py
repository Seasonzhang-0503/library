# Generated by Django 3.2.7 on 2023-04-11 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0035_alter_user_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theborrow',
            name='theBorrow_status1',
            field=models.CharField(blank=True, choices=[('借订中', '借订中'), ('已归还', '已归还'), ('已学习', '已学习'), ('学习中', '学习中')], max_length=500, null=True, verbose_name='借订状态1'),
        ),
        migrations.AlterField(
            model_name='theborrow',
            name='theBorrow_theBook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.thebook'),
        ),
        migrations.AlterField(
            model_name='theborrow',
            name='theBorrow_theUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
