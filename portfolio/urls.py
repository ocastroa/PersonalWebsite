from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='portfolio'),
    path('<slug>', views.project, name='project'),
]