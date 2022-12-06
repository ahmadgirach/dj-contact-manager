""" STANDARD DJANGO IMPORTS """

from django.urls import path

""" LOCAL APP IMPORTS """

from .views import homepage_view, logout_view, signin_view, signup_view, credits_view


urlpatterns = [
    path("", homepage_view, name="home"),
    path("signup/", signup_view, name="signup"),
    path("signin/", signin_view, name="signin"),
    path("logout/", logout_view, name="logout"),
    path("credits/", credits_view, name="credits"),
]
