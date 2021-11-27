from django.contrib import admin

from .models import Figure, Cleaning, Comic

# Register your models here
admin.site.register(Figure)

admin.site.register(Cleaning)

admin.site.register(Comic)