from django.contrib import admin

from shops.models import Book
from users.models import Address


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    pass