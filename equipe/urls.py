from django.urls import path,include
from equipe import views




urlpatterns = [
    path('', views.index, name='equipe'),
]