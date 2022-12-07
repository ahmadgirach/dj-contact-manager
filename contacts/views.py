""" STANDARD DJANGO IMPORTS """

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache

""" LOCAL APP IMPORTS """

from .forms import ContactForm
from .models import Contact


@never_cache
@login_required
def create_view(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect("home")
        else:
            messages.error(request, "Please fix the errors!")

    context = {"form": form}

    return render(request, "contacts/create.html", context)


@never_cache
@login_required
def edit_view(request, pk):
    """
    If user tries to manually alter the ID of the contact, make sure
    current user belongs to it or such contact exists.
    Otherwise don't allow to view that page.
    """
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return redirect("contacts:not-found")

    if contact and contact.user != request.user:
        return redirect("contacts:unauthorized")

    form = ContactForm(instance=contact)

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect("home")
        else:
            messages.error(request, "Please fix the errors!")

    context = {
        "form": form,
        "is_editing": True,
    }

    return render(request, "contacts/create.html", context)


@login_required
def delete_view(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == "POST":
        contact.delete()
        return redirect("home")


@login_required
def toggle_favourite(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == "POST":
        contact.is_favourite = not contact.is_favourite
        contact.save()
        return redirect("home")


@never_cache
@login_required
def unauthorized_view(request):
    return render(request, "401.html")


@never_cache
@login_required
def not_found_view(request):
    return render(request, "404.html")
