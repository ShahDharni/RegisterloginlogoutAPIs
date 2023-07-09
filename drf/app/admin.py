
# # from .models import User

# # admin.site.register(User)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# from .models import Profile

# # class ProfileInline(admin.StackedInline):
# #     model = Profile
# #     can_delete = False
# #     verbose_name_plural = 'Profile'
# #     fk_name = 'name'

# # class CustomUserAdmin(UserAdmin):
# #     inlines = (ProfileInline, )

# #     def get_inline_instances(self, request, obj=None):
# #         if not obj:
# #             return list()
# #         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# # admin.site.unregister(User)
# # admin.site.register(User, CustomUserAdmin)


# # class CustomUserAdmin(UserAdmin):
# #     inlines = (ProfileInline, )
# #     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
# #     list_select_related = ('profile', )

# #     # def get_location(self, instance):
# #     #     return instance.profile.location
# #     # get_location.short_description = 'Location'

# #     def get_inline_instances(self, request, obj=None):
# #         if not obj:
# #             return list()
# #         return super(CustomUserAdmin, self).get_inline_instances(request, obj)



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# # from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']

# admin.site.register(User, CustomUserAdmin)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User
from django.db import models
from .models import Product
from .models import Category
from django.utils.html import format_html
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name','category_desc','created_at','is_active',)
    list_filter=('category_name',)
    search_fields=('category_name__startswith',)

    def is_active(self, obj):
        return obj.is_active == 1
  
    is_active.boolean = True


   
admin.site.register(Category,CategoryAdmin)

admin.site.site_header = "Django_worst"
admin.site.site_title = "Welcome to D's Project"
admin.site.index_title = "Welcome to D's Project"





class ProductAdmin(admin.ModelAdmin):
    list_display=('category_id','product_id','product_name','product_desc','created_at','is_active',)
    list_filter=('product_name',)
    search_fields=('product_name__startswith',)
    


admin.site.register(Product,ProductAdmin)



class CustomUserAdmin(UserAdmin):
    add_form=UserCreationForm
    form=UserChangeForm
    model=User
    list_display=['name','DOB','user_type']
    add_fieldsets=UserAdmin.add_fieldsets+ (
        (None,{'fields':('name','DOB','user_type',)}),
    )
    fieldsets=UserAdmin.fieldsets+ (
        (None,{'fields':('name','DOB','user_type',)}),
    )


admin.site.register(User,CustomUserAdmin)
