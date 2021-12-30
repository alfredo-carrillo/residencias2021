# Generated by Django 3.2.9 on 2021-11-25 16:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0002_remove_business_business_reason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='contact',
        ),
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
