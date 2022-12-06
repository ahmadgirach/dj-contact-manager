""" STANDARD DJANGO IMPORTS """

from django.urls import path

""" LOCAL APP IMPORTS """

from .views import create_view, delete_view, edit_view, toggle_favourite


app_name = "contacts"

urlpatterns = [
    path("create/", create_view, name="create"),
    path("<int:pk>/edit", edit_view, name="edit"),
    path("<int:pk>/delete", delete_view, name="delete"),
    path("<int:pk>/toggle-favourite", toggle_favourite, name="toggle-favourite"),
]
