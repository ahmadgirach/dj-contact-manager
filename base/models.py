from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    avatar = models.ImageField(upload_to="media/")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
