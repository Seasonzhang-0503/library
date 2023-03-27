from django.db import models
from django import forms
from django.forms import ModelForm
from .models import *

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

