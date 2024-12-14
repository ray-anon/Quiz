from django.contrib import admin
from django.urls import path, include  # Import 'path' correctly

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL pattern
    path('', include('app.urls')),  # Root URL, include URLs from 'app' app
]
