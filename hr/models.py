from django.db import models

# Create your models here.

class Reg_email(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email
