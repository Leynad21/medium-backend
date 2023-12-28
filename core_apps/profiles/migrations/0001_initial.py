# Generated by Django 4.1.7 on 2023-12-27 17:22

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        default="+250784123456",
                        max_length=30,
                        region=None,
                        verbose_name="phone number",
                    ),
                ),
                (
                    "about_me",
                    models.TextField(
                        default="say something about yourself", verbose_name="about me"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        default="O",
                        max_length=20,
                        verbose_name="gender",
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        default="PT", max_length=2, verbose_name="country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default="Lisbon", max_length=180, verbose_name="city"
                    ),
                ),
                (
                    "profile_photo",
                    models.ImageField(
                        default="/profile_default.png",
                        upload_to="",
                        verbose_name="profile photo",
                    ),
                ),
                (
                    "twitter_handle",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="twitter handle"
                    ),
                ),
                (
                    "followers",
                    models.ManyToManyField(
                        blank=True, related_name="following", to="profiles.profile"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
    ]
