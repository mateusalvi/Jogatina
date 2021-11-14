from django.contrib import admin
from .models import saleAnnounce,transactions

# Register your models here.
@admin.register(saleAnnounce)

class VendasAdmin (admin.ModelAdmin):
    list_display = ("title", "vendor", "date_announced", "price")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(transactions)
class transactionsAdmin(admin.ModelAdmin):
    list_display = ('vendor','customer','price','status','date')