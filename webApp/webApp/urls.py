from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # allauth routes start
    path('accounts/', include('allauth.urls')),
    # path to our users app
    path('', include('users.urls')),
]
