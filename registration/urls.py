from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.Registration.as_view(), name='registration'),
]