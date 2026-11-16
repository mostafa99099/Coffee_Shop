from django.urls import path
from . import views

urlpatterns = [
    path("", views.Base_Home, name="Base_Home"), 
    
]