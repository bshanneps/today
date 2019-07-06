from django.urls import path
from question import views
from django.contrib import admin

urlpatterns = [
    path('create', views.create),
    path('show/', views.show),
    path('edit/<int:id>/', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>/', views.delete),

]