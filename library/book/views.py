from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from book.models import *


# Create your views here.
# 登出页面
def categorylist(request):
    form = categoryForm()

    context = {
        "form": form,
    }

    return render(request,'categorylist.html',context)
