from django.db import models


class ContactInfo(models.Model):
    mobile_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email_id = models.EmailField(max_length=50)


class Customer(ContactInfo):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
