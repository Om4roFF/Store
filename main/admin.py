from django.contrib import admin
from main.models import Car, Photo


class PhotoImageInline(admin.TabularInline):
    model = Photo
    extra = 3


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PhotoImageInline, ]


admin.site.register(Car,PropertyAdmin)