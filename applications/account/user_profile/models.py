from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

User = get_user_model()


class Gender(models.TextChoices):
    No = 'no'
    Man = 'man'
    Woman = 'woman'


class ProfileModel(models.Model):
    slug = models.SlugField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=24, blank=True)
    last_name = models.CharField(max_length=24, blank=True)
    birth_date = models.DateField(auto_now_add=True)
    gender = models.CharField(
        max_length=6, blank=True,
        choices=Gender.choices, default=Gender.No)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)
