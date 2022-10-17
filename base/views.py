from rest_framework.viewsets import ModelViewSet

from base.models import Contact
from base.serializers import ContactSerializer


class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
