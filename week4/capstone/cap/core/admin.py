from django.contrib import admin
from core.models import UploadImage
# Register your models here.

@admin.register(UploadImage)
class UploadImageAdmin(admin.ModelAdmin):
    pass