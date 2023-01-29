from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.email
