from django.db import models

class theBook(models.Model):
    bid = models.AutoField(primary_key=True)
    theBook_id = models.CharField(max_length=500,verbose_name=('图书编号'),blank=True, null=True,)
    theBook_name = models.CharField(max_length=500,verbose_name=('图书名称'),blank=True, null=True,)
    theBook_location = models.CharField(max_length=500,verbose_name=('图书所在地'),blank=True, null=True,)
    theBook_type = models.IntegerField(verbose_name=('图书类别'),blank=True, null=True,)
    theBook_subject = models.IntegerField(verbose_name=('图书主题'),blank=True, null=True,)
    theBook_logo = models.ImageField(max_length=500, blank=True, null=True, verbose_name=('图书照片1'),upload_to='images')
    theBook_attachment = models.FileField(max_length=10000,verbose_name=('图书附件'),blank=True, null=True,upload_to='file')
    theBook_status1 = models.CharField(max_length=500,verbose_name=('图书状态1'),blank=True, null=True,)
    theBook_status2 = models.CharField(max_length=500,verbose_name=('图书状态2'),blank=True, null=True,)
    theBook_status3 = models.CharField(max_length=500,verbose_name=('图书状态3'),blank=True, null=True,)
    theBook_information1 = models.CharField(max_length=10000,verbose_name=('图书信息1'),blank=True, null=True,)
    theBook_information2 = models.CharField(max_length=10000,verbose_name=('图书信息2'),blank=True, null=True,)
    theBook_information3 = models.CharField(max_length=10000,verbose_name=('图书信息3'),blank=True, null=True,)
    theBook_information4 = models.CharField(max_length=10000,verbose_name=('图书信息4'),blank=True, null=True,)
    theBook_information5 = models.CharField(max_length=10000,verbose_name=('图书信息5'),blank=True, null=True,)

    class Meta:
        verbose_name = ('图书')
        verbose_name_plural = ('图书')

    def __str__(self):
        return str(self.theBook_id,self.theBook_name)


class subject(models.Model):
    sid = models.AutoField(primary_key=True)
    subject_id = models.CharField(max_length=500,verbose_name=('图书编号'),blank=True, null=True,)
    subject_name = models.CharField(max_length=500,verbose_name=('图书名称'),blank=True, null=True,)

    class Meta:
        verbose_name = ('分类')
        verbose_name_plural = ('分类')

    def __str__(self):
        return str(self.subject_id,self.subject_name)



class borrow(models.Model):
    boid = models.AutoField(primary_key=True)
    borrow_datetime = models.DateTimeField(max_length=500,verbose_name=('图书编号'),blank=True, null=True,)
    borrow_datetime = models.CharField(max_length=500,verbose_name=('图书名称'),blank=True, null=True,)

    class Meta:
        verbose_name = ('借定')
        verbose_name_plural = ('借定')

    def __str__(self):
        return str(self.subject_id,self.subject_name)