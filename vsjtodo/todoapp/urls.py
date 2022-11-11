from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
path('form/', views.form),
path('tasks/', views.alltasks),
path('update/', views.update),

]
