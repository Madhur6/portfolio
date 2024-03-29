from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"