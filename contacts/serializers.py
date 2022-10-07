from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('owner', 'id','country_code', "first_name","last_name", "phone_number", "contact_picture", "is_favourited")

    