# Generated by Django 2.2.1 on 2019-06-04 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='password',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
