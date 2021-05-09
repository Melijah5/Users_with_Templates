from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-user', views.add_user),
    path('result/<int:id>', views.result),
    path('reset/<int:id>', views.reset)
    
]