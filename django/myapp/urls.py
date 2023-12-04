from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name = 'home'),
    path('api/get_recommendation/', views.get_recommendation, name='get_recommendation')
]