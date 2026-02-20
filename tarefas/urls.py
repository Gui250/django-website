from . import views
from django.urls import path

urlpatterns = [ 
    path('', views.home, name='home'),
    path('adicionar', views.adicionar, name='adicionar'),
    path('tarefa/<int:id>', views.editar, name='editar'),
]