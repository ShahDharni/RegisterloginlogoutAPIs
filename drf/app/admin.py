from typing import Optional
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.http.request import HttpRequest
from .models import User
from django.db import models
from .models import Product
from .models import Category
from django.utils.html import format_html
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
# from rest_framework.views import
# from django.contrib.messages import constants as messages
 

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name','category_desc','created_at','is_active',)
    list_filter=('category_name',)
    search_fields=('category_name__startswith',)

    def is_active(self, obj):
        return obj.is_active == 1
  
    is_active.boolean = True




from .models import ProductImage
 
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    
   
admin.site.register(Category,CategoryAdmin)
admin.site.site_header = "Django_worst"
admin.site.site_title = "Welcome to D's Project"
admin.site.index_title = "Welcome to D's Project"





class ProductAdmin(admin.ModelAdmin):
    list_display=('category_id','product_id','product_name','product_desc','created_at','is_active',)
    list_filter=('product_name',)
    search_fields=('product_name__startswith',)
    


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)


class CustomUserAdmin(UserAdmin):
    add_form=UserCreationForm
    form=UserChangeForm
    model=User
    list_display=["id","username",'name','DOB','user_type']
    # add_fieldsets=UserAdmin.add_fieldsets+ (
    #     (None,{'fields':('name','DOB','user_type',)}),
    # )
    # fieldsets=UserAdmin.fieldsets+ (
    #     (None,{'fields':('name','DOB','user_type',)}),
    # )

    def add_view(self, request,form_url='' ,extra_context=None):
        if request.method == "POST":
            if User.objects.all().count() >= 5:
                messages.error(
                        request, f"Update you subscription plan to add more users."
                    )
                return HttpResponseRedirect("/admin/app/user/")
            

        return super().add_view(request,form_url=form_url,extra_context=extra_context)

admin.site.register(User,CustomUserAdmin)

# class UserAdminPermissions(admin.ModelAdmin):
    