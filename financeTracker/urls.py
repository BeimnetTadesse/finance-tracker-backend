from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # 👈 your new app
    path('api/core/', include('core.urls')),          # 👈 only if core.urls has valid patterns
    path('', include('core.urls')), 
]
