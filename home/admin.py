from django.contrib import admin
from .models import UserPassword, Provider


# Register models here to show into admin panel.
admin.site.register(UserPassword)
admin.site.register(Provider)
