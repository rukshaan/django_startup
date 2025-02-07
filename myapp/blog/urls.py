
from django.urls import path
from . import views  # Ensure views is properly imported


app_name='blog'
urlpatterns = [
    path("", views.index, name="index"),  # Ensure this exists
    path("post/<int:post_id>", views.detail, name="detail"), 
    path("new_url", views.new_url_view, name="new_url_page"),
    path("old_url", views.old_url_view, name="old_url"),
]