# Generated by Django 3.2.7 on 2023-03-24 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('category_id', models.CharField(blank=True, max_length=500, null=True, verbose_name='主题编号')),
                ('category_keyname', models.CharField(blank=True, max_length=500, null=True, verbose_name='主题主名称')),
                ('category_subname', models.CharField(blank=True, max_length=500, null=True, verbose_name='主题子名称')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='theUser',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('theUser_id', models.CharField(blank=True, max_length=500, null=True, verbose_name='用户ID')),
                ('theUser_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='用户名称')),
                ('theUser_logo', models.ImageField(blank=True, max_length=500, null=True, upload_to='images', verbose_name='用户LOGO')),
                ('theUser_password', models.CharField(blank=True, max_length=500, null=True, verbose_name='用户密码')),
                ('theUser_status1', models.CharField(blank=True, max_length=500, null=True, verbose_name='用户状态1')),
                ('theUser_status2', models.CharField(blank=True, max_length=500, null=True, verbose_name='用户状态2')),
                ('theUser_status3', models.CharField(blank=True, max_length=500, null=True, verbose_name='用户状态3')),
            ],
            options={
                'verbose_name': '自定义用户',
                'verbose_name_plural': '自定义用户',
            },
        ),
        migrations.CreateModel(
            name='theBook',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('theBook_id', models.CharField(blank=True, max_length=500, null=True, verbose_name='图书编号')),
                ('theBook_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='图书名称')),
                ('theBook_location', models.CharField(blank=True, max_length=500, null=True, verbose_name='图书所在地')),
                ('theBook_type', models.IntegerField(blank=True, null=True, verbose_name='图书类别')),
                ('theBook_logo', models.ImageField(blank=True, max_length=500, null=True, upload_to='images', verbose_name='图书照片1')),
                ('theBook_attachment', models.FileField(blank=True, max_length=10000, null=True, upload_to='file', verbose_name='图书附件')),
                ('theBook_status1', models.CharField(blank=True, max_length=500, null=True, verbose_name='图书状态1')),
                ('theBook_status2', models.CharField(blank=True, max_length=500, null=True, verbose_name='图书状态2')),
                ('theBook_status3', models.CharField(blank=True, max_length=500, null=True, verbose_name='图书状态3')),
                ('theBook_information1', models.TextField(blank=True, max_length=10000, null=True, verbose_name='图书信息1')),
                ('theBook_information2', models.TextField(blank=True, max_length=10000, null=True, verbose_name='图书信息2')),
                ('theBook_information3', models.TextField(blank=True, max_length=10000, null=True, verbose_name='图书信息3')),
                ('theBook_information4', models.TextField(blank=True, max_length=10000, null=True, verbose_name='图书信息4')),
                ('theBook_information5', models.TextField(blank=True, max_length=10000, null=True, verbose_name='图书信息5')),
                ('theBook_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='theBook_category', to='book.category')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
        migrations.CreateModel(
            name='borrow',
            fields=[
                ('boid', models.AutoField(primary_key=True, serialize=False)),
                ('borrow_datetime', models.DateTimeField(blank=True, max_length=500, null=True, verbose_name='借订编号')),
                ('borrow_status1', models.CharField(blank=True, max_length=500, null=True, verbose_name='借订状态1')),
                ('borrow_status2', models.CharField(blank=True, max_length=500, null=True, verbose_name='借订状态2')),
                ('borrow_status3', models.CharField(blank=True, max_length=500, null=True, verbose_name='借订状态3')),
                ('borrow_theBook', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrow_theBook', to='book.thebook')),
                ('borrow_theUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrow_theUser', to='book.theuser')),
            ],
            options={
                'verbose_name': '借订',
                'verbose_name_plural': '借订',
            },
        ),
    ]
