from django.contrib import admin
from book.models import *
# Register your models here.



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

    list_display = ('boid','theBorrow_datetime')

admin.site.register(theBorrow,theBorrowAdmin)