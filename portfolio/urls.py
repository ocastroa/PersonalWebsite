from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:project_id>', views.project, name='project'),
]