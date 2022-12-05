""" STANDARD DJANGO IMPORTS """

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields):
        user = self.model(email=self.normalize_email(email), **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **other_fields):
        extra = {
            "is_superuser": True,
            "is_staff": True,
            **other_fields,
        }

        user = self.create_user(email=email, password=password, **extra)

        return user


class CustomUser(AbstractUser):
    """
    By default, ``username`` field is required and unique; but we want to use
    email as login field. Thus, need to mark this field as optional, otherwise
    it'll raise integrity constraint errors.
    """

    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_("150 characters or fewer. Letters, digits and @/./+/-/_ only."),
    )

    """
    By default, ``email`` field is optional; but we want to use
    it as login field. Thus, need to mark this field as unique.
    """

    email = models.EmailField(_("email address"), unique=True)

    """ Map the ``username`` field to ``email`` """

    USERNAME_FIELD = "email"

    """
    If you have any other required fields other than ``email``, those should
    be listed here.
    """

    REQUIRED_FIELDS = []

    objects = CustomUserManager()
