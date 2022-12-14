from django.contrib import admin
from django.urls import path
from djangoCRUD_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('news', views.news),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete),
]