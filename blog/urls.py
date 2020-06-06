from django.urls import path,include
from blog import views




urlpatterns = [
    path('blog', views.index, name='blog'),
    path('single', views.index, name='single'),
]