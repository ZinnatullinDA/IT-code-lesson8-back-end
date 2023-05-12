from django.db import models


class Author(models.Model):
    name = models.CharField('ФИО', max_length=255)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Название', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, blank=True)
    description = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title



