from django.contrib import admin
from core import models

@admin.register(models.Book)
class Book(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Genre)
class Genre(admin.ModelAdmin):
    list_display = ('name',)



@admin.register(models.Author)
class Author(admin.ModelAdmin):
    list_display = ('name',)
