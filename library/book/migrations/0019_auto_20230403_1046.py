# Generated by Django 3.2.7 on 2023-04-03 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_alter_theuser_theuser_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_id'], 'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.AlterModelOptions(
            name='thebook',
            options={'ordering': ['theBook_category'], 'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelOptions(
            name='theborrow',
            options={'ordering': ['theBorrow_datetime'], 'verbose_name': '借订', 'verbose_name_plural': '借订'},
        ),
        migrations.AlterField(
            model_name='thebook',
            name='theBook_type',
            field=models.CharField(choices=[('电子书', '电子书'), ('纸质书', '纸质书'), ('PPT', 'PPT'), ('项目', '项目'), ('视频', '视频'), ('其他', '其他')], max_length=500, verbose_name='电子书/纸质书'),
        ),
        migrations.AlterField(
            model_name='theborrow',
            name='theBorrow_datetime',
            field=models.DateTimeField(auto_now_add=True, max_length=500, verbose_name='借订日期'),
        ),
        migrations.AlterField(
            model_name='theborrow',
            name='theBorrow_status1',
            field=models.CharField(choices=[('借订中', '借订中'), ('已归还', '已归还'), ('已学习', '已学习'), ('学习中', '学习中')], max_length=500, verbose_name='借订状态1'),
        ),
        migrations.AlterUniqueTogether(
            name='theborrow',
            unique_together={('theBorrow_theUser', 'theBorrow_theBook')},
        ),
    ]
