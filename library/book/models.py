from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
# from library.settings import AUTH_USER_MODEL


THEUSERSTATUS_TYPE = (('active', 'active'), ('inactive', 'inactive'))
class User(AbstractUser):
    # 继承并重写
    dept = models.IntegerField(verbose_name=('部门'),blank=True, null=True,)
    age = models.IntegerField(verbose_name=('年龄'),blank=True, null=True,)
    mobilenumber = models.CharField(max_length=500,verbose_name=('电话号码'),blank=True, null=True,)
    role = models.CharField(max_length=500,verbose_name=('角色'),blank=True, null=True,)
    theUser_status1 = models.CharField(max_length=500,verbose_name=('用户状态1'),choices=THEUSERSTATUS_TYPE,default='active')
    field1 = models.CharField(max_length=500,verbose_name=('属性1'),blank=True, null=True,)
    field2 = models.CharField(max_length=500,verbose_name=('属性2'),blank=True, null=True,)
    field3 = models.CharField(max_length=500,verbose_name=('属性3'),blank=True, null=True,)
    field4 = models.CharField(max_length=500,verbose_name=('属性4'),blank=True, null=True,)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'



class location(models.Model):
    lid = models.AutoField(primary_key=True)
    location_city = models.CharField(max_length=500,verbose_name=('城市'))
    location_name = models.CharField(max_length=500,verbose_name=('地点名称'))


    class Meta:
        verbose_name = ('地点')
        verbose_name_plural = ('地点')

    def __str__(self):
        return str(str(self.location_city) + '--' + self.location_name)


class category(models.Model):
    cid = models.AutoField(primary_key=True)
    category_id = models.CharField(max_length=500,verbose_name=('分类编号'),)
    category_keyname = models.CharField(max_length=500,verbose_name=('分类主名称'),)
    category_subname = models.CharField(max_length=500,verbose_name=('分类子名称'),)


    class Meta:
        verbose_name = ('分类')
        verbose_name_plural = ('分类')
        ordering = ['category_id'] # 返回值排序

    def __str__(self):
        return str(self.category_id + '--' + self.category_keyname + '--' + self.category_subname)


THEBOOK_TYPE = (('电子书', '电子书'), ('纸质书', '纸质书'), ('PPT', 'PPT'),('项目', '项目'), ('视频', '视频'),('其他', '其他'))
THESTATUS_TYPE = (('已借订', '已借订'), ('未借订', '未借订'))

class theBook(models.Model):
    bid = models.AutoField(primary_key=True)
    theBook_name = models.CharField(max_length=500,verbose_name=('图书名称'),)
    theBook_location = models.ForeignKey(location,blank=True, null=True, on_delete=models.CASCADE,related_name='Book_location')
    theBook_type = models.CharField(max_length=500, verbose_name=('电子书/纸质书'),choices=THEBOOK_TYPE,)
    theBook_category = models.ForeignKey(category,blank=True, null=True, on_delete=models.CASCADE,related_name='Book_category')
    theBook_logo = models.ImageField(max_length=500, verbose_name=('图书照片1'),upload_to='images/')
    theBook_attachment = models.FileField(max_length=10000,verbose_name=('图书附件(备用)'),blank=True, null=True,upload_to='file')
    theBook_status1 = models.CharField(max_length=500,verbose_name=('图书状态1'),choices=THESTATUS_TYPE,)
    theBook_status2 = models.CharField(max_length=500,verbose_name=('图书状态2(备用)'),blank=True, null=True,)
    theBook_status3 = models.CharField(max_length=500,verbose_name=('图书状态3(备用)'),blank=True, null=True,)
    theBook_id = models.CharField(max_length=500,verbose_name=('图书编号(备用)'),blank=True, null=True,)
    theBook_information1 = models.TextField(max_length=10000,verbose_name=('图书信息1'),blank=True, null=True,)
    theBook_information2 = models.TextField(max_length=10000,verbose_name=('图书信息2(备用)'),blank=True, null=True,)
    theBook_information3 = models.TextField(max_length=10000,verbose_name=('图书信息3(备用)'),blank=True, null=True,)
    theBook_information4 = models.TextField(max_length=10000,verbose_name=('图书信息4(备用)'),blank=True, null=True,)
    theBook_information5 = models.TextField(max_length=10000,verbose_name=('图书信息5(备用)'),blank=True, null=True,)

    class Meta:
        verbose_name = ('图书')
        verbose_name_plural = ('图书')
        ordering = ['theBook_category'] # 返回值排序


    def __str__(self):
        return str(self.theBook_name)




THEBORROWSTATUS_TYPE = (('借订中', '借订中'), ('已归还', '已归还'), ('已学习', '已学习'), ('学习中', '学习中'))
class theBorrow(models.Model):
    boid = models.AutoField(primary_key=True)
    theBorrow_add_datetime = models.DateTimeField(max_length=500,verbose_name=('创建日期'),auto_now_add=True)
    theBorrow_update_datetime = models.DateTimeField(max_length=500,verbose_name=('修改日期'),auto_now=True)
    theBorrow_theUser = models.ForeignKey(User,on_delete=models.CASCADE) #related_name='borrow_theUser',
    theBorrow_theBook = models.ForeignKey(theBook,on_delete=models.CASCADE)  #,related_name='borrow_theBook'
    theBorrow_duration = models.IntegerField(verbose_name=('借订天数'),blank=True, null=True,)
    theBorrow_status1 = models.CharField(max_length=500, choices=THEBORROWSTATUS_TYPE, verbose_name=('借订状态1'))
    theBorrow_status2 = models.CharField(max_length=500,verbose_name=('借订状态2'),blank=True, null=True,)
    theBorrow_status3 = models.CharField(max_length=500,verbose_name=('借订状态3'),blank=True, null=True,)

    class Meta:
        verbose_name = ('借订')
        verbose_name_plural = ('借订')
        # ordering = ['theBorrow_add_datetime'] # 返回值排序
        unique_together = [['theBorrow_theUser','theBorrow_theBook']] # 联合唯一


    def __str__(self):
        return str(self.boid)+ '--' +str(self.theBorrow_theUser)
    

