from django.urls import path  # Use 'path' instead of 'url'
from . import views

urlpatterns = [
    path('', views.q_list, name='q_list'),  # Root URL for the app
    path('result', views.result, name='result'),  # /result URL
]
