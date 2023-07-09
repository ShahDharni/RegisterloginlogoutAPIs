# # # from django.db import models
# # # from django.contrib.auth.models import AbstractUser
# # # from django.contrib.auth.models import User
# # # from django.db import models
# # # from django.db.models.signals import post_save
# # # from django.dispatch import receiver

# # # class User(AbstractUser):
    

  
# # # class UserProfile(models.Model):
# # #     Vendor = 1
# # #     Employee = 2
 
# # #     user_type = (
# # #         (Vendor, 'Vendor'),
# # #         (Employee, 'Employee'),
       
# # #     )
# # #     name = models.OneToOneField(User, on_delete=models.CASCADE)
# # #     DOB = models.DateField(null=True, blank=True)
# # #     user_data = models.PositiveSmallIntegerField(choices=user_type, null=True, blank=True)


    


# # # @receiver(post_save, sender=User)
# # # def create_or_update_user_profile(sender, instance, created, **kwargs):
# # #     if created:
# # #         UserProfile.objects.create(user=instance)
# # #     instance.profile.save()



# # from django.db import models
# # from django.contrib.auth.models import User
# # from django.db.models.signals import post_save
# # from django.dispatch import receiver

# # class Profile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     bio = models.CharField(null=True, max_length=200)
# #     birth_date = models.DateField(null=True, blank=True)    
# #     profile_pic = models.ImageField(default='default.jpg', upload_to='profiles_pics')
# #     hobby = models.CharField(null=True, max_length=200)
    


# #     USERNAME_FIELD = 'user'
# #     REQUIRED_FIELDS = []

    


# # @receiver(post_save, sender=User)
# # def create_profile(sender, instance, created, **kwargs):
# #     if created:
# #         Profile.objects.create(user=instance)

# # @receiver(post_save, sender=User)
# # def save_profile(sender, instance, **kwargs):
# #     instance.profile.save()


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Category(models.Model):

    category_name = models.CharField(max_length=500)
    category_desc = models.CharField(max_length=5000, default="")
    category_img= models.ImageField(upload_to='images/',default="")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True)
    is_active = models.IntegerField(default = 1,blank = True,  null = True, help_text ='1->Active, 0->Inactive',  choices =((1, 'Active'), (0, 'Inactive')))
                                   
                                   
                                  
                                   

    def __str__(self) -> str:
         return str(self.category_name) 
    

class Product(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Product')
    product_id = models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=500)
    product_img= models.ImageField(upload_to='images/',default="")
    product_desc=models.CharField(max_length=5000)
    created_at=models.DateField(auto_now_add=True,blank=True,null=True)
    is_active = models.IntegerField(default = 1,blank = True,null = True,help_text ='1->Active, 0->Inactive', choices =((1, 'Active'), (0, 'Inactive')                          ))

    


    def __str__(self):
          return str(self.product_name)

user_type_data = (
        ("1", "vendor"), 
        ("2", "employee"),
        ("3", "Customer"),
        )

class User(AbstractUser):
    # Username=None
    name = models.CharField(max_length=100)
    DOB = models.CharField(max_length=80)
    user_type = models.CharField( choices=user_type_data, max_length=10)
    

    def __str__(self):
        return self.name
