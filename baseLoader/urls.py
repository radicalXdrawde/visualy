from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_database, name='upload_database'),
]
