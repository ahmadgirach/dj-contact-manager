from django.urls import path

from .views import homepage_view, logout_view, signin_view, signup_view


urlpatterns = [
    path("", homepage_view, name="home"),
    path("signup/", signup_view, name="signup"),
    path("signin/", signin_view, name="signin"),
    path("logout/", logout_view, name="logout"),
]
