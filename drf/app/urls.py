from .views import RegisterAPI
from django.urls import path
from .views import LoginAPI
# from . views import CategoryListCreateView
from .views import *
# from . views import ProductListCreateView

# from.views import CustomModelAPI

from django.urls import path
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', LogoutAPI.as_view(), name='logout'), 
    # path('api/Categoryapi/', CategoryListCreateView.as_view()),
    # path('api/Categoryapi/<int:pk>/',CategoryRetrieveUpdateDestroyView.as_view()),
    # path('api/Productsapi/',ProductListCreateView.as_view()),
    # # path('api/Productsapi/<int:pk>/',ProductRetrieveUpdateDestroyView.as_view()),
    
    
    # path('api/registercustom/', CustomModelAPI.as_view(), name='logout'),   
  

]

