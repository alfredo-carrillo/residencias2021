# Generated by Django 3.2.9 on 2021-11-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20211125_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
