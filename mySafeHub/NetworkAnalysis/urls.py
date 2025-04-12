from django.urls import path
from . import views

urlpatterns = [
    path('', views.Net_Analysis, name='network_like_a_web'),
    path('process/', views.process_data, name='process'),
]
