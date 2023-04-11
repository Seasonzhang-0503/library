# Generated by Django 3.2.7 on 2023-04-11 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0036_auto_20230411_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theborrow',
            name='theBorrow_status1',
            field=models.CharField(choices=[('借订中', '借订中'), ('已归还', '已归还'), ('已学习', '已学习'), ('学习中', '学习中')], max_length=500, verbose_name='借订状态1'),
        ),
        migrations.AlterField(
            model_name='theborrow',
            name='theBorrow_theBook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.thebook'),
        ),
        migrations.AlterField(
            model_name='theborrow',
            name='theBorrow_theUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.user'),
        ),
    ]