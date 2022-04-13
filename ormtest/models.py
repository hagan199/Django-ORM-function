from django.db import models
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def number_books(self):
        number_books = Book.objects.filter(author=self).count()
        return number_books

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
     return f'{self.title}.{self.author.name}'


