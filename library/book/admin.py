from django.contrib import admin
from book.models import *
# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('username',)

    ordering = ('username',)
admin.site.register(User, UserAdmin)

class categoryAdmin(admin.ModelAdmin):

    list_display = ('cid','category_id','category_keyname','category_subname')

    ordering = ('category_id',)

admin.site.register(category,categoryAdmin)



class theBookAdmin(admin.ModelAdmin):

    list_display = ('bid','theBook_name','theBook_type','theBook_logo')

admin.site.register(theBook,theBookAdmin)




class locationAdmin(admin.ModelAdmin):

    list_display = ('lid','location_city','location_name')

admin.site.register(location,locationAdmin)



class theBorrowAdmin(admin.ModelAdmin):

    list_display = ('boid','theBorrow_add_datetime')

admin.site.register(theBorrow,theBorrowAdmin)



# class theUserAdmin(admin.ModelAdmin):

#     list_display = ('uid','theUser_name')

# admin.site.register(theUser,theUserAdmin)