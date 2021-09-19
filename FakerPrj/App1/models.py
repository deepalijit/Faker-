from django.db import models

# Create your models here.
class PersonModel(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name},{self.email}'