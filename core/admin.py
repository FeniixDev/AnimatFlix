from django.contrib import admin

# Register your models here.
from project.core.models import AuthUser

admin.site.register(AuthUser, )
