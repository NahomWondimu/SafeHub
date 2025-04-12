from django.urls import path
from . import views

urlpatterns = [
    path('', views.Web_Analysis, name='danger_site'),
    path('process/', views.process_data, name='process'),
]
