from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('get-content', views.get_content, name="index_content")
]
