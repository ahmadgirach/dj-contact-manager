from rest_framework.serializers import ModelSerializer

from base.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "first_name", "last_name", "email", "phone_number", "avatar")
