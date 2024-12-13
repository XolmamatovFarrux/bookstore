from django.db import models

class Authers(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    IN_STOCK = 'In Stock'
    OUT_OF_STOCK = 'Out of Stock'
    ON_SALE = 'On Sale'
    NEW = 'New'

    AVAILABILITY_CHOICES =[
        (IN_STOCK, 'In Stock'),
        (OUT_OF_STOCK, 'Out of Stock'),
        (ON_SALE, 'On Sale'),
        (NEW, 'New'),
    ]

    STANDARD = 'Standard'
    DOWNLOADABLE = 'Downloadable'
    EXTERNAL = 'External'


    FORMAT_CHOICES = [
        (STANDARD, 'Standard'),
        (DOWNLOADABLE, 'Downloadable'),
        (EXTERNAL, 'External'),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authers, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(blank=True, null=True)
    categories = models.ManyToManyField(Categories)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    published = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.text


