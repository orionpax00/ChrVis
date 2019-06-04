from django.db import models
# Create your models here.

def user_directory_path_matrix(instance, filename):
    return ('{0}/{1}.matrix'.format(instance.email.split('@')[0], filename))

def user_directory_path_annot(instance, filename):
    return ('{0}/{1}.annot'.format(instance.email.split('@')[0], filename))


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    matrix_file = models.FileField(upload_to=user_directory_path_matrix)
    annotation_file = models.FileField(upload_to=user_directory_path_annot)
    uploaded_at = models.DateTimeField(auto_now_add=True)
