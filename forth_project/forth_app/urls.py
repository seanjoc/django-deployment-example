from django.urls import path
from forth_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('users/',views.users,name='users'),
]
