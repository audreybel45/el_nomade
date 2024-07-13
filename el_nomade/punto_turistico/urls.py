
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_punto_turistico, name='create_punto_turistico'),
    path('', views.list_puntos_turisticos, name='list_puntos_turisticos'),
    path('update/<int:pk>/', views.update_punto_turistico, name='update_punto_turistico'),
    path('delete/<int:pk>/', views.delete_punto_turistico, name='delete_punto_turistico'),
    path('upload/', views.upload_image, name='upload_image'),  # Agregar esta línea

]

