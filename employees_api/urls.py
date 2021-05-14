from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.EmployeeAPIView.as_view(), name="employees_api"),
]
