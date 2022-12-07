""" STANDARD DJANGO IMPORTS """

from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
    """If user is inactive for 1 hour(s) then on next request, user will be logged out."""
    SECONDS = 60
    MINUTES = 60
    HOURS = 1
    duration = SECONDS * MINUTES * HOURS
    request.session.set_expiry(duration)

    current_user = request.user
    params = request.GET

    current_page = params.get("page") or 1
    search = params.get("search")

    query = Q()

    if not current_user.is_superuser:
        query &= Q(user=current_user)

    if search:
        query &= (
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(email__icontains=search)
            | Q(organization__icontains=search)
            | Q(phone_number__icontains=search)
        )

    contacts = Contact.objects.filter(query).order_by("pk")
    paginator = Paginator(contacts, settings.RECORDS_PER_PAGE)
    page_obj = paginator.get_page(current_page)

    context = {
        "page_obj": page_obj,
        "no_of_pages_range": range(1, page_obj.paginator.num_pages + 1),
    }

    return render(request, "home.html", context)


@never_cache
@login_required
def logout_view(request):
    logout(request)
    return redirect("signin")


def credits_view(request):
    links = (
        {
            "category": "Web Framework",
            "caption": "Django",
            "url": "https://djangoproject.com",
        },
        {
            "category": "Styling",
            "caption": "Tailwind CSS",
            "url": "https://tailwindcss.com",
        },
        {
            "category": "Fonts",
            "caption": "IBM Plex Sans",
            "url": "https://fonts.google.com/specimen/IBM+Plex+Sans",
        },
        {"category": "Icons", "caption": "Hero Icons", "url": "https://heroicons.com"},
        {
            "category": "Table, Search box & Pagination designs",
            "caption": "Flowbite",
            "url": "https://flowbite.com",
        },
        {
            "category": "Alerts",
            "caption": "SweetAlert2",
            "url": "https://sweetalert2.github.io",
        },
    )

    context = {
        "links": links,
    }

    return render(request, "credits.html", context)
