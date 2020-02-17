from django.urls import path

from pyladies import views

urlpatterns = [
    path('', views.home_page, name='home')
]
