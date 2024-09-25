from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books_created"
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn_number = models.CharField(max_length=13, null=True, blank=True)
    cover_image = models.URLField(null=True, blank=True)
    categories = models.ManyToManyField(
        "Category", through="BookCategory", related_name="books"
    )

    def __str__(self):
        return self.title


# for categories
# The first argument is the name of the table that is the other side of the many-to-many relationship - Category. Django will just find this model by name.

# The second argument tells Django which model will store those relationships - BookCategory.

# The third argument is what property will be added to instances of the Category model to contain a list of related books - books.
