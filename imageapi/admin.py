from django.contrib import admin

# Register your models here.
from .models import Hero, UploadImageTest
admin.site.register(Hero)
admin.site.register(UploadImageTest)