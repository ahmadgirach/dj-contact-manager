from django.urls import path

from .views import create_view, delete_view, edit_view


app_name = "contacts"

urlpatterns = [
    path("create/", create_view, name="create"),
    path("<int:pk>/edit", edit_view, name="edit"),
    path("<int:pk>/delete", delete_view, name="delete"),
]
