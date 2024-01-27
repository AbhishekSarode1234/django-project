from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns =[
    path('new/', views.new, name='new'),
    path('update/', views.update, name='update'),
    path('contact/', views.update, name='update'),
    path('members/', views.members, name='members'),
    path('members/detail/update/<int:id>/',views.update,name='update'),
    path('members/detail/delete/<int:id>/',views.delete,name='delete'),
    path('members/detail/<int:id>',views.detail,name='detail'),
]
    
