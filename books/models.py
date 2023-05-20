from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=255)
    ratings = models.FloatField()
    published_year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name