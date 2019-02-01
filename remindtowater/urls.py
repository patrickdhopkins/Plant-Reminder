from django.urls import path, re_path

from . import views

app_name = 'remindtowater'
# urlpatterns = [
#     re_path('(?P<user>\w+)/(?P<pk>\d+)/', views.DetailView.as_view(), name='detail'),
#     re_path('(?P<user>\w+)/', views.IndexView.as_view(), name='index'),
#     re_path('(?P<user>\w+)/add_plant/', views.AddPlantView.as_view(), name='add_plant'),
# ]

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    re_path('(?P<username>\w+)/(?P<pk>\d+)/', views.DetailView.as_view(), name='detail'),
    re_path('(?P<username>\w+)', views.IndexView.as_view(), name='index'),
    path('add_plant/', views.AddPlantView.as_view(), name='add_plant'),
]

# url(r'^(?P<user>\w+)/(?P<slug>\w+)/$', views.PageView.as_view(), name='page')

# currently trying to use user from plants, however this won't work as no plant exist!! need to use current user!!
