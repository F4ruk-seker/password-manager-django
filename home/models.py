from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField

User = get_user_model()


class UserPassword(models.Model):
    username: models.CharField = models.CharField(max_length=100, default=None, blank=True, null=True)
    email: models.CharField = models.CharField(max_length=100, default=None, blank=True, null=True)
    password: models.CharField = models.CharField(max_length=500)

    # bool
    favorite: models.BooleanField = models.BooleanField(default=False)
    delete: models.BooleanField = models.BooleanField(default=False)

    provider: models.ForeignKey = models.ForeignKey('Provider', on_delete=models.CASCADE)
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)

    date_created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    date_last_updated: models.DateTimeField = models.DateTimeField(auto_now=True)


class Provider(models.Model):
    class ProviderType(models.TextChoices):
        social = "1", "Social"
        media = "2", "Media"
        game = "3", "Game"
        bank = "4", "Bank"
        development = "5", "Development"
        mail = "6", "Mail"
        other = "7", "Other"

    provider_type: models.CharField = models.CharField(
        max_length=2,
        choices=ProviderType.choices,
        default=ProviderType.social
    )

    name: models.CharField = models.CharField(max_length=100)

    cloudinary_icon_settings = {
        'overwrite': True,
        'folder': 'password/icon',
        'resource_type': "image",
        'transformation': {"quality": "auto:low"},
        'format': "webp",
    }

    if settings.DEBUG:
        icon: models.ImageField = models.ImageField(default=None, blank=True, null=True)
    else:
        icon: CloudinaryField = CloudinaryField(**cloudinary_icon_settings)

    def __str__(self) -> str:
        return f"@{self.name}:{self.ProviderType(self.provider_type).label}"
