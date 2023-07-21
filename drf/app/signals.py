# from django.db.models.signals import pre_save,post_save
# from django.contrib.auth import get_user_model
# from django.dispatch import receiver
# from .models import User
# from django.core.exceptions import ValidationError

# # user=get_user_model

# # # @receiver(post_save,sender=user)
# # # def create_user_profile(sender, instance, created,**kwargs):
# # #     print(sender)
# # #     print("{{}}")
# # #     print(instance)
# # #     print("^^^")
# # #     print(created)
# # #     print("++++")
# # #     print(**kwargs)

# # #     if created:
# # #         User.objects.create(user=instance)


# @receiver(pre_save, sender=User)
# def limit_user_registration(sender, instance, created, **kwargs):
#     print("inside function...")
#     print(sender)
#     print("***********")
#     print(instance)
#     print("IIIIII")
#     print(created)
#     print("{{{{{}}}}}")
#     if created:
#         user_count = User.objects.count()
#         max_users = 5

#         if user_count == max_users:
#             raise ValidationError("You can't register more than 5 users.")

# # # @receiver(pre_save, sender=user)
# # # def save_profile(sender, instance, **kwargs):
# # #     instance.user.save()  

# # # @receiver(pre_save, sender=user)

# # # def user_pre_save(sender, instance, created, **kwargs):
# # #     if created and sender.objects.count() > 6:
# # #         instance.is_active = False
# # #         instance.save()