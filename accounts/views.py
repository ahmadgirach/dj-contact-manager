""" STANDARD DJANGO IMPORTS """

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

""" LOCAL APP IMPORTS """

from .forms import SigninForm, SignupForm

from contacts.models import Contact


def signup_view(request):
    form = SignupForm()
    success = False

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            messages.success(request, "User created successfully!")
        else:
            messages.error(request, "Please fix the errors!")

    context = {
        "form": form,
        "success": success,
    }

    return render(request, "registration/signup.html", context)


def signin_view(request):
    form = SigninForm()

    if request.method == "POST":
        form = SigninForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid credentials!")
        else:
            messages.error(request, "Invalid form!")

    context = {"form": form}

    return render(request, "registration/signin.html", context)


@never_cache
@login_required
def homepage_view(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts,
    }
    return render(request, "home.html", context)


@never_cache
@login_required
def logout_view(request):
    logout(request)
    return redirect("signin")


@never_cache
@login_required
def credits_view(request):
    return render(request, "credits.html")
