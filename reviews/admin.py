from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'created_at')
    list_filter = ('product', 'user', 'created_at')
    search_fields = ('user__username', 'product__name', 'text')
