from django.contrib import admin
from django.urls import path
from edlearn.views import front, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", front, name="front"),
    path('home/', home, name="home")
]