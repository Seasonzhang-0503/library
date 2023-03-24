from django.db import models



class category(models.Model):
    cid = models.AutoField(primary_key=True)
    category_id = models.CharField(max_length=500,verbose_name=('主题编号'),blank=True, null=True,)
    category_keyname = models.CharField(max_length=500,verbose_name=('主题主名称'),blank=True, null=True,)
    category_subname = models.CharField(max_length=500,verbose_name=('主题子名称'),blank=True, null=True,)


    class Meta:
        verbose_name = ('分类')
        verbose_name_plural = ('分类')

    def __str__(self):
        return str(self.category_id,self.category_keyname,self.category_subname)




class theBook(models.Model):
    bid = models.AutoField(primary_key=True)
    theBook_id = models.CharField(max_length=500,verbose_name=('图书编号'),blank=True, null=True,)
    theBook_name = models.CharField(max_length=500,verbose_name=('图书名称'),blank=True, null=True,)
    theBook_location = models.CharField(max_length=500,verbose_name=('图书所在地'),blank=True, null=True,)
    theBook_type = models.IntegerField(verbose_name=('图书类别'),blank=True, null=True,)
    theBook_category = models.ForeignKey(category,blank=True, null=True, on_delete=models.CASCADE,related_name='theBook_category')
    theBook_logo = models.ImageField(max_length=500, blank=True, null=True, verbose_name=('图书照片1'),upload_to='images')
    theBook_attachment = models.FileField(max_length=10000,verbose_name=('图书附件'),blank=True, null=True,upload_to='file')
    theBook_status1 = models.CharField(max_length=500,verbose_name=('图书状态1'),blank=True, null=True,)
    theBook_status2 = models.CharField(max_length=500,verbose_name=('图书状态2'),blank=True, null=True,)
    theBook_status3 = models.CharField(max_length=500,verbose_name=('图书状态3'),blank=True, null=True,)
    theBook_information1 = models.TextField(max_length=10000,verbose_name=('图书信息1'),blank=True, null=True,)
    theBook_information2 = models.TextField(max_length=10000,verbose_name=('图书信息2'),blank=True, null=True,)
    theBook_information3 = models.TextField(max_length=10000,verbose_name=('图书信息3'),blank=True, null=True,)
    theBook_information4 = models.TextField(max_length=10000,verbose_name=('图书信息4'),blank=True, null=True,)
    theBook_information5 = models.TextField(max_length=10000,verbose_name=('图书信息5'),blank=True, null=True,)

    class Meta:
        verbose_name = ('图书')
        verbose_name_plural = ('图书')

    def __str__(self):
        return str(self.theBook_id,self.theBook_name)



class theUser(models.Model):
    uid = models.AutoField(primary_key=True)
    theUser_id = models.CharField(max_length=500,verbose_name=('用户ID'),blank=True, null=True,)
    theUser_name = models.CharField(max_length=500,verbose_name=('用户名称'),blank=True, null=True,)
    theUser_logo = models.ImageField(max_length=500, blank=True, null=True, verbose_name=('用户LOGO'),upload_to='images')
    theUser_password = models.CharField(max_length=500,verbose_name=('用户密码'),blank=True, null=True,)
    theUser_status1 = models.CharField(max_length=500,verbose_name=('用户状态1'),blank=True, null=True,)
    theUser_status2 = models.CharField(max_length=500,verbose_name=('用户状态2'),blank=True, null=True,)
    theUser_status3 = models.CharField(max_length=500,verbose_name=('用户状态3'),blank=True, null=True,)


    class Meta:
        verbose_name = ('自定义用户')
        verbose_name_plural = ('自定义用户')

    def __str__(self):
        return str(self.subject_id,self.subject_mainname,self.subject_subname)





class borrow(models.Model):
    boid = models.AutoField(primary_key=True)
    borrow_datetime = models.DateTimeField(max_length=500,verbose_name=('借订编号'),blank=True, null=True,)
    borrow_theUser = models.ForeignKey(theUser,blank=True, null=True, on_delete=models.CASCADE,related_name='borrow_theUser')
    borrow_theBook = models.ForeignKey(theBook,blank=True, null=True, on_delete=models.CASCADE,related_name='borrow_theBook')
    borrow_status1 = models.CharField(max_length=500,verbose_name=('借订状态1'),blank=True, null=True,)
    borrow_status2 = models.CharField(max_length=500,verbose_name=('借订状态2'),blank=True, null=True,)
    borrow_status3 = models.CharField(max_length=500,verbose_name=('借订状态3'),blank=True, null=True,)

    class Meta:
        verbose_name = ('借订')
        verbose_name_plural = ('借订')

    def __str__(self):
        return str(self.subject_id,self.subject_name)
    

