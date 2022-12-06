""" STANDARD DJANGO IMPORTS """

from django.forms import ModelForm

""" LOCAL APP IMPORTS """

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ("user", "is_favourite")
