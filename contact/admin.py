from django.contrib import admin

from .models import Contact, Category

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ... 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): 
    ... 
