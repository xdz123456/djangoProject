# Generated by Django 3.2.5 on 2022-07-14 19:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatbot', '0012_alter_property_property_interested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property_belong',
        ),
        migrations.AddField(
            model_name='property',
            name='property_belong',
            field=models.ManyToManyField(related_name='user_belong', to=settings.AUTH_USER_MODEL),
        ),
    ]
