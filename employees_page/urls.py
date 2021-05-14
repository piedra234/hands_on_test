from django.urls import path
from . import views

urlpatterns = [
    path('', views.Employees_view, name="employees_id"),
]