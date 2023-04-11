from django.db import models
from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import widgets as wid  #因为重名，所以起个别名
from django.forms.widgets  import  SelectDateWidget

class locationForm(ModelForm):
    class Meta:
        model = location
        fields = '__all__'


    # 循环找到所有的插件,加入css样式,添加 "class": "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field)
            field.widget.attrs = {"class": "form-control"}


class categoryForm(ModelForm):
    class Meta:
        model = category
        fields = '__all__'


    # 循环找到所有的插件,加入css样式,添加 "class": "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field)
            field.widget.attrs = {"class": "form-control"}




class theBookForm(ModelForm):
    class Meta:
        model = theBook
        fields = '__all__'
        exclude = ['theBook_id','theBook_attachment','theBook_status1','theBook_status2','theBook_status3','theBook_information2',
                   'theBook_information3','theBook_information4','theBook_information5',]
        error_messages = {
            'theBook_name':{'required':"theBook_name不能为空",},
        }

        # labels= {
        #     "theBook_name":"自定义书名"
        # }

        widgets = {
            "theBook_name":wid.Input(attrs={"class":"c1"}) #还可以自定义属性
        }


    # 循环找到所有的插件,加入css样式,添加 "class": "form-control"
    bootstrap_exclude_fields = ['theBook_logo',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段,给每个字段的插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            # class属性追加form-control，其他属性保留
            if field.widget.attrs:
                field.widget.attrs["class"] = field.widget.attrs.get('class','') + ' ' + 'form-control'
            else:
                field.widget.attrs = {
                    "class": "form-control",
                }






class theBorrowForm(ModelForm):
    class Meta:
        model = theBorrow
        fields = '__all__'
        exclude = ['theBorrow_duration','theBorrow_status2','theBorrow_status3',]

        widgets = {
            "theBorrow_datetime":wid.SelectDateWidget(attrs={"type":"date","class":'ml-3'}) #还可以自定义属性
            # "theBorrow_datetime":wid.Input(attrs={"type":"date"})
        }
        
    # 循环找到所有的插件,加入css样式,添加 "class": "form-control"
    bootstrap_exclude_fields = ['theBorrow_datetime',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段,给每个字段的插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            # class属性追加form-control，其他属性保留
            if field.widget.attrs:
                field.widget.attrs["class"] = field.widget.attrs.get('class','') + ' ' + 'form-control'
            else:
                field.widget.attrs = {
                    "class": "form-control",
                }


class theBorrowModalAddForm(ModelForm):
    class Meta:
        model = theBorrow
        fields = '__all__'
        exclude = ['theBorrow_status2','theBorrow_status3',]

        # widgets = {
        # }
        
    # 循环找到所有的插件,加入css样式,添加 "class": "form-control"
    bootstrap_exclude_fields = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段,给每个字段的插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            # class属性追加form-control，其他属性保留
            if field.widget.attrs:
                field.widget.attrs["class"] = field.widget.attrs.get('class','') + ' ' + 'form-control'
            else:
                field.widget.attrs = {
                    "class": "form-control",
                }



class theBorrowModalShowForm(ModelForm):
    boid = forms.CharField(label='boid',widget=wid.Input(attrs={"class":'edit','readonly':True}))
    # theBorrow_add_datetime = forms.CharField(label='theBorrow_add_datetime',widget=wid.Input(attrs={"class":'edit'}))
    class Meta:
        model = theBorrow
        fields = '__all__'
        exclude = ['theBorrow_status2','theBorrow_status3',]
 
        widgets = {
            # "theBorrow_theUser":wid.Select(attrs={"class":'edit',"readonly":'true'}),
            # "theBorrow_theBook":wid.Select(attrs={"class":'edit'}),
            # "theBorrow_duration":wid.NumberInput(attrs={"class":'edit'}),
            # "theBorrow_status1":wid.Select(attrs={"class":'edit'}),
        } 

    # 循环找到所有的插件,加入css样式,添加 "class": "form-control"
    bootstrap_exclude_fields = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段,给每个字段的插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            # class属性追加form-control，其他属性保留
            if field.widget.attrs:
                field.widget.attrs["class"] = field.widget.attrs.get('class','') + ' ' + 'form-control'+ ' ' + 'edit'
            else:
                field.widget.attrs = {
                    "class": "form-control"+ ' ' + 'edit',
                }




class theUserForm(ModelForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username','password','dept','age','mobilenumber','role','theUser_status1',]
        exclude = []

        widgets = {
            "password":wid.PasswordInput(render_value = True) # render_value = True显示值
        }

        labels= {
            "username":"用户名",
            "password":"密码",
        }

        
    # 循环找到所有的插件,加入css样式,添加 "class": "form-control"
    bootstrap_exclude_fields = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段,给每个字段的插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            # class属性追加form-control，其他属性保留
            if field.widget.attrs:
                field.widget.attrs["class"] = field.widget.attrs.get('class','') + ' ' + 'form-control'
            else:
                field.widget.attrs = {
                    "class": "form-control",
                }





#想办法取出多选框的选项
#querylist <QuerySet [{'category_keyname': '人力资源'}, {'category_keyname': '人力资源'}, {'category_keyname': '后端'}, {'category_keyname': '前端'}, {'category_keyname': '前端'}, {'category_keyname': '人力资源'}, {'category_keyname': '后端'}, {'category_keyname': '前端'}, {'category_keyname': '后端'}, {'category_keyname': 'Git'}, {'category_keyname': '后端'}, {'category_keyname': '服务器'}, {'category_keyname': '数据'}]>
querylist = category.objects.all().order_by('category_keyname').distinct().values('category_keyname')
# querylist2 <QuerySet [('Git',), ('人力资源',), ('前端',), ('后端',), ('数据',), ('服务器',)]>
# querylist2 = category.objects.all().order_by('category_keyname').distinct().values_list('category_keyname')
query_set = set()
querybookcategory_choices = [('',''),]
for q in querylist:
    query_set.add(q['category_keyname'])
for qs in query_set:
    querybookcategory_choices.append((qs,qs))
# querybookcategory_choices = [('人力资源', '人力资源'), ('后端', '后端')]
print('querybookcategory_choices',querybookcategory_choices)

# querytheBookcategory_choices = [('', ''),('电子书', '电子书'), ('纸质书', '纸质书')]
querytheBookcategory_list = theBook.objects.all().order_by('theBook_type').distinct().values('theBook_type')
print('querytheBookcategory_list',querytheBookcategory_list)
query_set = set()
querytheBookcategory_choices = [('',''),]
for q in querytheBookcategory_list:
    query_set.add(q['theBook_type'])
for qs in query_set:
    querytheBookcategory_choices.append((qs,qs))


class QueryBookForm(forms.Form):
    querybookname = forms.CharField(label='图书名称')
    querybookcategory = forms.ChoiceField(label='图书分类',choices=querybookcategory_choices)
    querybooktype = forms.ChoiceField(label='图书类型',choices=querytheBookcategory_choices,)


