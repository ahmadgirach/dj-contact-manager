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

    context = {
        "form": form
    }

    return render(request, "contacts/create.html", context)


@never_cache
@login_required
def edit_view(request, pk):
    contact = Contact.objects.get(pk=pk)
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
