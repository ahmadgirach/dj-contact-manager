""" STANDARD DJANGO IMPORTS """

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class Contact(models.Model):
    first_name = models.CharField(_("First Name"), max_length=20)
    last_name = models.CharField(_("Last Name"), max_length=20)
    email = models.EmailField(_("Email"), max_length=20, blank=True, null=True)
    phone_number = models.CharField(
        _("Phone Number"), max_length=20, blank=True, null=True, default=""
    )
    organization = models.CharField(
        _("Organization"), max_length=50, blank=True, null=True, default=""
    )
    avatar = models.ImageField(
        _("Avatar"), upload_to="profiles/", blank=True, null=True, default=""
    )
    is_favourite = models.BooleanField(
        _("Favourite?"),
        # help_text=_(
        #     "Designates whether this contact has been marked as Favourite or not."
        # )
    )
    user = models.ForeignKey(
        UserModel,
        related_name="contacts",
        on_delete=models.CASCADE,
    )

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
