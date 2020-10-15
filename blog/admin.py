from django.contrib import admin
from .models import post
# Register your models here.



class postAdmin(admin.ModelAdmin):
    list_display=['Title','create_at']
    list_filter=['create_at']

admin.site.register(post,postAdmin)    