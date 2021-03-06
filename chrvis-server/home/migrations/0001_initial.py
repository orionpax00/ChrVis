# Generated by Django 2.2.1 on 2019-06-03 22:51

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('matrix_file', models.FileField(upload_to=home.models.user_directory_path_matrix)),
                ('annotation_file', models.FileField(upload_to=home.models.user_directory_path_annot)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
