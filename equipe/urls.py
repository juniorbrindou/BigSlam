from django.urls import path,include
from equipe import views




urlpatterns = [
    path('equipe', views.index, name='equipe'),
]