from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django import forms
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt



def home(request):

    context = {
    }

    return render(request,'home.html',context)




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


def categorylist_delete(request,cid):
    category.objects.get(cid=cid).delete()
    return redirect("/categorylist_show/")




def locationlist_show(request):    
    locationlist = location.objects.all()
    
    context = {
        'locationlist':locationlist,
    }

    return render(request,'locationlist_show.html',context)



def locationlist_new(request):

    if request.method == "GET":
        form = locationForm()
        return render(request,'locationlist_new.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = locationForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/locationlist_show/")

    return render(request,'locationlist_new.html',{'form':form})



def locationlist_edit(request,lid):
    row_obj = location.objects.filter(lid=lid).first()

    if request.method == "GET":
        form = locationForm(instance=row_obj)
        return render(request,'locationlist_edit.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = locationForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/locationlist_show/")

    return render(request,'locationlist_edit.html',{'form':form})



def locationlist_delete(request,lid):
    location.objects.get(lid=lid).delete()
    return redirect("/locationlist_show/")





def theBooklist_show(request):
    theBooklist = theBook.objects.all()

    context = {
        'theBooklist':theBooklist,
    }

    return render(request,'theBooklist_show.html',context)



def theBooklist_new(request):

    if request.method == "GET":
        form = theBookForm()
        return render(request,'theBooklist_new.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = theBookForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        # print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/theBooklist_show/")

    return render(request,'theBooklist_new.html',{'form':form})



def theBooklist_edit(request,bid):
    row_obj = theBook.objects.filter(bid=bid).first()

    if request.method == "GET":
        form = theBookForm(instance=row_obj)

        # 三元表达式：判断是否存在借订记录
        theBook_fk_theBorrow_status1 = row_obj.theborrow_set.first().theBorrow_status1 if row_obj.theborrow_set.first() else 'no-data'
        print(theBook_fk_theBorrow_status1)
        return render(request,'theBooklist_edit.html',{'form':form,'theBook_fk_theBorrow_status1':theBook_fk_theBorrow_status1,})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = theBookForm(data=request.POST,files=request.FILES, instance=row_obj)
    if form.is_valid():
        print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/theBooklist_show/")

    return render(request,'theBooklist_edit.html',{'form':form})


def theBooklist_delete(request,bid):
    theBook.objects.get(bid=bid).delete()
    return redirect("/theBooklist_show/")








def theBorrowlist_show(request):
    theBorrowlist = theBorrow.objects.all()
    
    context = {
        'theBorrowlist':theBorrowlist,
    }

    return render(request,'theBorrowlist_show.html',context)



def theBorrowlist_new(request):

    if request.method == "GET":
        form = theBorrowForm()
        return render(request,'theBorrowlist_new.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = theBorrowForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        # print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/theBorrowlist_show/")

    return render(request,'theBorrowlist_new.html',{'form':form})



def theBorrowlist_edit(request,boid):
    row_obj = theBorrow.objects.filter(boid=boid).first()

    if request.method == "GET":
        form = theBorrowForm(instance=row_obj)
        return render(request,'theBorrowlist_edit.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = theBorrowForm(data=request.POST,files=request.FILES, instance=row_obj)
    if form.is_valid():
        # print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/theBorrowlist_show/")

    return render(request,'theBorrowlist_edit.html',{'form':form})


def theBorrowlist_delete(request,boid):
    theBorrow.objects.get(boid=boid).delete()
    return redirect("/theBorrowlist_show/")









def theUserlist_show(request):
    theUserlist = theUser.objects.all()
    
    context = {
        'theUserlist':theUserlist,
    }

    return render(request,'theUserlist_show.html',context)



def theUserlist_new(request):

    if request.method == "GET":
        form = theUserForm()
        return render(request,'theUserlist_new.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = theUserForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        # print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/theUserlist_show/")

    return render(request,'theUserlist_new.html',{'form':form})



def theUserlist_edit(request,uid):
    row_obj = theUser.objects.filter(uid=uid).first()

    if request.method == "GET":
        form = theUserForm(instance=row_obj)
        return render(request,'theUserlist_edit.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = theUserForm(data=request.POST,files=request.FILES, instance=row_obj)
    if form.is_valid():
        # print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/theUserlist_show/")

    return render(request,'theUserlist_edit.html',{'form':form})


def theUserlist_delete(request,uid):
    theUser.objects.get(uid=uid).delete()
    return redirect("/theUserlist_show/")





def theBorrowlist_user(request):

    theBorrowlist = theBorrow.objects.all()
    AddForm = theBorrowModalAddForm()
    ShowForm = theBorrowModalShowForm()
    # EditForm = theBorrowModalEditForm()
        
    context = {
        'theBorrowlist':theBorrowlist,
        'AddForm':AddForm,
        'ShowForm':ShowForm,
        # 'EditForm':EditForm,
    }

    return render(request,'theBorrowlist_user.html',context)



@csrf_exempt
def theBorrowlist_user_modal_show(request):

    boid = request.GET.get('boid')
    print('得到boid',boid)
    # values方法形成一个对象
    row_obj = theBorrow.objects.filter(boid=boid).values("boid", "theBorrow_datetime", "theBorrow_theUser",
                                                         'theBorrow_theBook','theBorrow_duration','theBorrow_status1'
                                                         ).first()

    if not row_obj:
        return JsonResponse({"status": False, "error": "数据不存在!"})
    
    # 从数据库中获取到一个对象 row_object
    result = {
        "status": True,
        "data": row_obj,
    }
    print('result',result)

    return JsonResponse(result)



@csrf_exempt
def theBorrowlist_user_modal_new(request):
    result = {
        "status": True,
        "error":'fail',
    }
    return JsonResponse(result)