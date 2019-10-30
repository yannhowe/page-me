from . import views
from django.urls import path

urlpatterns = [
    path('helloworld/', views.helloworld, name='helloworld'),
    path('netpage/', views.netpage, name='netpage'),
]