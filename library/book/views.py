from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import *
from .forms import *
from django.shortcuts import render, redirect


# Create your views here.
# 登出页面
def categorylist(request):
    form = categoryForm()

    context = {
        "form": form,
    }

    return render(request,'categorylist.html',context)


def categorylist_show(request):    
    categorylist = category.objects.all()
    
    context = {
        'categorylist':categorylist,
    }

    return render(request,'categorylist_show.html',context)



def categorylist_new(request):

    if request.method == "GET":
        form = categoryForm()
        return render(request,'categorylist_new.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = categoryForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/categorylist_show/")

    return render(request,'categorylist_new.html',{'form':form})



def categorylist_edit(request,cid):
    row_obj = category.objects.filter(cid=cid).first()

    if request.method == "GET":
        form = categoryForm(instance=row_obj)
        return render(request,'categorylist_edit.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = categoryForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/categorylist_show/")

    return render(request,'categorylist_edit.html',{'form':form})

