from django.urls import path
from responsive__CV import views

urlpatterns = [
    path('', views.show_CV, name='responsive__CV'),
]