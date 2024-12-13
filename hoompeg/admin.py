from django.contrib import admin
from .models import Authers,Categories,Books,Reviews

@admin.register(Authers)
class AuthersAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title','author','price','availability', 'format')
    search_fields = ('title','author_name')
    list_filter = ('availability','format')
    filter_horizontal = ('categories',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user','book','rating')
    search_fields = ('user','book','title')