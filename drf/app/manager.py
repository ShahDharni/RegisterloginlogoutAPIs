# # Manager.py is used to manage the user models

# from django.contrib.auth.base_user import BaseUserManager


# class UserManager(BaseUserManager):
#     # Here we have to modify the two methods create_user and createsuper_user so that it will add up these extra or additional fields.
#     def create_user(self,username,password=None,**extra_fields):
#         if not username:
#             raise ValueError("Name is required")
        
#         user=self.model(username=username,**extra_fields)
#         user.username=username

#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     # extra_fields=['DOB']==extra_fields['DOB']
    
#     def create_superuser(self,username,password=None,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)

#         return self.create_user(username,password,**extra_fields)