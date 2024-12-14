from django.urls import path  
from . import views

urlpatterns = [
    path('', views.q_list, name='q_list'),  
    path('result', views.result, name='result'),  
]
