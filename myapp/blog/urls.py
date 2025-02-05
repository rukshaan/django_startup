
from django.urls import path
from . import views  # Ensure views is properly imported

urlpatterns = [
    path("", views.index, name="index"),  # Ensure this exists
    path("/detail", views.detail, name="detail"), 
]