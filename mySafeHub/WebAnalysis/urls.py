from django.urls import path
from . import views

urlpatterns = [
    path('', views.Web_Analysis, name='danger_site'),
]
