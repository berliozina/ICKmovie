from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all),
    path('<str:film>', views.show_one, name='show_one'),
]
