from django.contrib import admin
from .models import Income, Category
# Register your models here.


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'owner', 'category', 'date',)
    search_fields = ('description', 'category', 'date', 'owner')

    list_per_page = 20


admin.site.register(Income, IncomeAdmin)
admin.site.register(Category)