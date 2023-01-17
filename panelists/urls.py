from django.urls import path
from . import views

urlpatterns = [

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.panelistProfile, name="panelist-profile"),
    # path('account/', views.panelistAccount, name="account"),
]
