from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('submit_job', views.submitjob, name='submitjob'),
    path('get_results', views.get_results, name='get_results'),
]
