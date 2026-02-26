from django.contrib import admin
from .models import book


# Register your models here.


# class bookadmin(admin.ModelAdmin):
#     # list_display=['id','name','author','price','description']
#     list_filter=['author']
#     list_editable=['name']
#     list_per_page=2



class book_admin(admin.ModelAdmin):
    list_display=['id','name','author','price','description']

    actions=['update_book']


    def update_book(self,request,queryset):
        queryset.update(price=0)
        self.message_user(request,'are you sure')



admin.site.register(book,book_admin)    
