from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('viewer', views.viewer, name='viewer'),
    path('get_results', views.get_results, name='get_results'),
]
