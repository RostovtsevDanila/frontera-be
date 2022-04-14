from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name="email", unique=True)

    class Meta:
        verbose_name = "user"


class Language(models.Model):
    language = models.CharField(verbose_name="language", max_length=32)

    class Meta:
        verbose_name = "language"


class Category(models.Model):
    name = models.CharField(verbose_name="name", max_length=256, blank=False, null=False)
    description = models.TextField(verbose_name="description")

    class Meta:
        verbose_name = "category"


class Course(models.Model):
    title = models.CharField(verbose_name="title", max_length=256, blank=False, null=False)
    authors = models.CharField(verbose_name="authors", max_length=256)
    category = models.ManyToManyField(Category)
    language = models.ManyToManyField(Language)
    updated_at = models.DateField(verbose_name="updated_at")
    duration = models.IntegerField(verbose_name="duration")
    description = models.TextField(verbose_name="description")

    class Meta:
        verbose_name = "course"
