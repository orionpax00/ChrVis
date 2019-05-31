from django.db import models
# Create your models here.

def user_directory_path(instance, filename):
    return ('{0}/{1}'.format(instance.email.split('@')[0], filename))


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
