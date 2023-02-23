from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('artworks/', views.getArtworks),
    path('artworks/<str:pk>/', views.getArtwork),
]
