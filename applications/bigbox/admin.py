from django.contrib import admin
from .models import (
    Box,
    Activity,
    Category,
    Reason
)
# Register your models here.

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    raw_id_fields = ('category',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    ordering = ('id',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')