from django.contrib import admin
from inventory.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'slug', 'is_active', 'level')
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
