from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django import forms
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password, check_password
import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse




def home(request):

    context = {
    }

    return render(request,'home.html',context)




def categorylist_show(request):    
    # categorylist = category.objects.all()
    # 练习原始SQL
    categorylist = category.objects.raw('SELECT * FROM book_category')
    
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





def theBooklist_show(request,page):
    theBooklist_all = theBook.objects.all()
    print('request.POST',request.POST.get('querybookcategory'))
    querybookname = request.POST.get('querybookname')
    # getlist呈现多选值
    querybookcategory = request.POST.get('querybookcategory')
    querybooktype = request.POST.get('querybooktype')
    print('querybookname',querybookname,'querybookcategory',querybookcategory,'querybooktype',querybooktype)

    theBooklist = theBooklist_all
    if querybookname:
        theBooklist = theBooklist_all.filter(theBook_name__icontains=querybookname)
    if querybookcategory:
        theBooklist = theBooklist.filter(theBook_category__category_keyname__icontains=querybookcategory)
    if querybooktype:
        theBooklist = theBooklist.filter(theBook_type__icontains=querybooktype)

    # 添加分页功能
    paginator = Paginator(theBooklist, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # 如果参数page 的数据类型不是整型，就返回第一页数据
        page_obj = paginator.page(1)
    except EmptyPage:
        # 若用户访问的页数大于实际页数，则返回最后一页的数据
        page_obj = paginator.page(paginator.num_pages) 

    # context = {
    #     'theBooklist':theBooklist,
    # }

    return render(request,'theBooklist_show.html',locals())



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
        theBook_fk_theBorrow_status1 = ''
        if row_obj.theBook_type == '纸质书':
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








def theBorrowlist_show(request,page=1):
    theBorrowlist = theBorrow.objects.all()
    
    # 添加分页功能
    paginator = Paginator(theBorrowlist, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # 如果参数page 的数据类型不是整型，就返回第一页数据
        page_obj = paginator.page(1)
    except EmptyPage:
        # 若用户访问的页数大于实际页数，则返回最后一页的数据
        page_obj = paginator.page(paginator.num_pages) 

    # context = {
    #     'theBorrowlist':theBorrowlist,
    # }

    return render(request,'theBorrowlist_show.html',locals())



def theBorrowlist_new(request):
    errorMsg = ''

    if request.method == "GET":
        form = theBorrowForm()
        return render(request,'theBorrowlist_new.html',{'form':form,'errorMsg':errorMsg})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = theBorrowForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        # print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/theBorrowlist_show/")
    else:
        errorMsg = '数据验证失败，请重新检查'
       
    return render(request,'theBorrowlist_new.html',{'form':form,'errorMsg':errorMsg})



def theBorrowlist_edit(request,boid):
    row_obj = theBorrow.objects.filter(boid=boid).first()

    if request.method == "GET":
        form = theBorrowForm(instance=row_obj)
        object_theBorrow_add_datetime = row_obj.theBorrow_add_datetime if row_obj.theBorrow_add_datetime else 'no-data'
        object_theBorrow_update_datetime = row_obj.theBorrow_update_datetime if row_obj.theBorrow_update_datetime else 'no-data'

        return render(request,'theBorrowlist_edit.html',locals())
    
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





def theBorrowlist_new_default(request,bid):
    errorMsg = ''
    id = request.user.id
    obj = theBook.objects.filter(bid=bid).first()
    userobj = User.objects.filter(id = id).first()

    if request.method == "GET":
        # 附带信息提交
        form = theBorrowForm({'theBorrow_theUser':userobj,
                              'theBorrow_theBook':obj,
                              'theBorrow_status1':'借订中'
                              })
        return render(request,'theBorrowlist_new.html',{'form':form,'errorMsg':errorMsg})

    # 用户POST请求提交数据,需要进行数据校验
    form = theBorrowForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        # print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/theBorrowlist_show/")
    else:
        errorMsg = '数据验证失败，请重新检查'
       
    return render(request,'theBorrowlist_new.html',{'form':form,'errorMsg':errorMsg})





def theUserlist_show(request,page=1):
    theUserlist = User.objects.all()
    # 添加分页功能
    paginator = Paginator(theUserlist, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # 如果参数page 的数据类型不是整型，就返回第一页数据
        page_obj = paginator.page(1)
    except EmptyPage:
        # 若用户访问的页数大于实际页数，则返回最后一页的数据
        page_obj = paginator.page(paginator.num_pages) 

    return render(request,'theUserlist_show.html',locals())



def theUserlist_new(request):

    if request.method == "GET":
        form = theUserForm()
        return render(request,'theUserlist_new.html',{'form':form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = theUserForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        
        # 直接保存至数据库
        form.save()
   
        return redirect("/theUserlist_show/")

    return render(request,'theUserlist_new.html',{'form':form})



def theUserlist_edit(request,id):
    row_obj = User.objects.filter(id=id).first()

    if request.method == "GET":
        form = theUserForm(instance=row_obj)
        # 判断是否存在借订记录
        theUser_fk_theBorrow_fk_theBook = []
        for fk in row_obj.theborrow_set.all():
            booklist = fk.theBorrow_theBook.theBook_name if fk else 'no-data'
            theUser_fk_theBorrow_fk_theBook.append(booklist)
            print(theUser_fk_theBorrow_fk_theBook)
        return render(request,'theUserlist_edit.html',{'form':form,'theUser_fk_theBorrow_fk_theBook':theUser_fk_theBorrow_fk_theBook,})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = theUserForm(data=request.POST,files=request.FILES, instance=row_obj)
    if form.is_valid():
        # print(form.cleaned_data)
        
        # 直接保存至数据库
        form.save()

        return redirect("/theUserlist_show/")

    return render(request,'theUserlist_edit.html',{'form':form})


def theUserlist_delete(request,id):
    User.objects.get(id=id).delete()
    return redirect("/theUserlist_show/")





def theBorrowlist_user(request,page=1):

    theBorrowlist = theBorrow.objects.all()
    AddForm = theBorrowModalAddForm()
    ShowForm = theBorrowModalShowForm()
        
    context = {
        'theBorrowlist':theBorrowlist,
        'AddForm':AddForm,
        'ShowForm':ShowForm,
    }

    # 添加分页功能
    paginator = Paginator(theBorrowlist, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # 如果参数page 的数据类型不是整型，就返回第一页数据
        page_obj = paginator.page(1)
    except EmptyPage:
        # 若用户访问的页数大于实际页数，则返回最后一页的数据
        page_obj = paginator.page(paginator.num_pages) 

    return render(request,'theBorrowlist_user.html',locals())





@csrf_exempt
def theBorrowlist_user_modal_new(request):
    """ 新建 """
    form = theBorrowModalAddForm(data=request.POST)
    if form.is_valid():
        print('is_valid',request.POST)
        form.save()
        return JsonResponse({"status": True,"error":'fail',})

    return JsonResponse({"status": False,"error":'fail',})



@csrf_exempt
def theBorrowlist_user_modal_show(request):

    boid = request.GET.get('boid')
    print('show-boid',boid)

    # values方法形成一个对象
    row_obj = theBorrow.objects.filter(boid=boid).values("boid", "theBorrow_add_datetime", "theBorrow_theUser",
                                                         'theBorrow_theBook','theBorrow_duration','theBorrow_status1'
                                                         ).first()

    
    if not row_obj:
        return JsonResponse({"status": False, "error": "数据不存在!","boid":boid})
    else:
        # 从数据库中获取到一个对象 row_object
        result = {
            "status": True,
            "data": row_obj,
            "boid":boid,
        }
        print('result',result)

        return JsonResponse(result)


@csrf_exempt
def theBorrowlist_user_modal_save(request):
    data = request.POST
    print('save-data',data)
    boid = request.POST.get('boid')
    print('save-boid',boid)

    # values方法形成一个对象
    # row_obj = theBorrow.objects.filter(boid=boid).values("boid", "theBorrow_add_datetime", "theBorrow_theUser",'theBorrow_theBook','theBorrow_duration','theBorrow_status1').first()
    row_obj = theBorrow.objects.filter(boid=boid).first()


    if not row_obj:
        return JsonResponse({"status": False, "error": "数据不存在!"})
    print('row_obj',row_obj)

    form = theBorrowModalShowForm(data=data,instance=row_obj)
    if form.is_valid():
        print('is_valid',request.POST)
        form.save()
        return JsonResponse({"status": True,"error":'fail-valid',})
    
    return JsonResponse({"status": False,"error":'fail-invalid',})




@csrf_exempt
def theBorrowlist_user_modal_delete(request):
    data = request.GET
    boid = request.GET.get('boid')
    print('delete-boid',boid)

    row_obj = theBorrow.objects.filter(boid=boid).first()

    if not row_obj:
        return JsonResponse({"status": False, "error": "数据不存在!"})
    else:
        theBorrow.objects.filter(boid=boid).first().delete()
        return JsonResponse({"status": True,"error":'fail-valid',})




def getQueryBookForm(request):
    form_obj = QueryBookForm(auto_id=True)
    return render(request, 'theBooklist_query.html', {'form_obj':form_obj})





# 登录视图
def user_login(request):
    '''ldap验证模式'''
    '''0.设定默认密码Z123qweASD'''
    '''1.django登录成功，login'''
    '''2.django登录不成功，启动ldap登录'''
    '''3.用户不存在时,直接pass,不login'''
    '''不修改默认密码'''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_django_default = 'Z123qweASD'

        access_token = 0

        # django验证
        user = authenticate(request,username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                pass
        else:
            pass
            return render(request,'user_login.html',{'error':'username and passwd error.'})
            ### 登录验证
            # keycloak_openid = KeycloakOpenID(
            #     server_url="https://keycloak-wzs.wistron.com/auth/",
            #     client_id="django-rest",
            #     realm_name="k8sprdtaskpublishingplatform",
            #     client_secret_key="secret",
            #     verify=False, )
            # try:
            #     token = keycloak_openid.token(username, password)
            #     access_token = token['access_token']
                
            # except Exception as e:
            #     # return render(request,'user_login.html',{'error':'username and passwd error.'})
            #     pass

            
            # if access_token:
            #     # print('access_token',access_token)
            #     user = authenticate(request,username=username,password=password_django_default)
            #     if user:
            #         if user.is_active:
            #             login(request,user)
            #             return HttpResponseRedirect('/')
            #         else:
            #             return HttpResponse("Your account is not active.")
            #     else:
            #         print("Invalid login detail:{0},{1}".format(username,password))
            #         return render(request,'user_login.html',{'error':'Invalid login detail'})
            # else:
            #     # ldap验证PS92
            #     status = check_ldap(username,password)
            #     if status == 200 or status == 302:
            #         user = authenticate(request,username=username,password=password_django_default)
            #         if user:
            #             if user.is_active:
            #                 login(request,user)
            #                 return HttpResponseRedirect('/')
            #             else:
            #                 return HttpResponse("Your account is not active.")
            #         else:
            #             print("Invalid login detail:{0},{1}".format(username,password))
            #             return render(request,'user_login.html',{'error':'Invalid login detail'})
            #     return render(request,'user_login.html',{'error':'Invalid login detail'})

    else:
        # get方式就返回空表
        return render(request,'user_login.html',{})




# 登出页面
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user_login/')


# 练习原始SQL
def practice_query_rowsql(request):
    practice_query_rowsql = theBook.objects.raw('SELECT * FROM book_thebook')
    for data in practice_query_rowsql:
        print('practice_query_rowsql:',data,data.theBook_type)
    return HttpResponse('练习原始sql')






# 直接执行自定义 SQL
# (2, '000001', 'Django基础教程(Tango with Django)', 5, 'images/tangowithdjango.png', '', '已借订', None, None, 'D:\\我的U盘-20220812\\ABE-Python\\4.python网页前后端\\Django基础教程', '', '', '', '', 3, '电子书')
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

from django.db import connection
def my_custom_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM book_thebook")
        rows = dictfetchall(cursor)
        print(rows)
        for row in rows:
            print('row.theBook_name',row['theBook_name'])
        
    # return HttpResponse('rows',rows)
    return HttpResponse('rows')





def chart_list(request):
    """ 数据统计 """
    return render(request, 'chart_list.html')




def chart_line(request):
    """ 构造折线图的数据 """
    # 数据可以去数据库中获取
    legend = ['天津分公司', '北京分公司']
    xAxis = ['1月', '2月', '3月', '4月', '5月', '6月', '7月']
    series_list = [
            {
                'name': '天津分公司',
                'type': 'line',
                'data': [520, 132, 101, 134, 90, 230, 210]
            },
            {
                'name': '北京分公司',
                'type': 'line',
                'data': [220, 182, 191, 234, 290, 330, 310]
            },
            ]

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "xAxis": xAxis,
            "series_list": series_list,
        }
    }

    return JsonResponse(result)



def chart_bar(request):
    """ 构造柱状图的数据 """

    # 数据可以去数据库中获取
    legend = ['销量', '价格']
    xAxis = ['1月', '2月', '3月', '4月', '5月', '6月']
    series_list = [
                {
                    "name": '销量',
                    "type": 'bar',
                    "data": [5, 20, 36, 10, 10, 20]
                },
                {
                    "name": '价格',
                    "type": 'bar',
                    "data": [25, 40, 80, 65, 70, 50]
                }
            ]

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "xAxis": xAxis,
            "series_list": series_list,
        }
    }

    return JsonResponse(result)



def chart_pie(request):
    """ 构造饼图的数据 """
    data_list = [
                    { "value": 10, "name": '销售部' },
                    { "value": 735, "name": '运营部' },
                    { "value": 580, "name": '财务部' },
                ]

    result = {
        "status": True,
        "data_list": data_list,
    }

    return JsonResponse(result)
