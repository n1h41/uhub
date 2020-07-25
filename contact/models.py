from django.db import models

# Create your models here.

class contact_us(models.Model):
    name = models.CharField(max_length=250, blank=False)
    phone = models.CharField(max_length=250, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.name