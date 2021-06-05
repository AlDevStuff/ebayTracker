from django.contrib import admin
from .models import Item

# Register your models here.

class Filter(admin.ModelAdmin):
    list_filter = ['email_sent']


admin.site.register(Item, Filter)