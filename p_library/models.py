from django.db import models

class Author(models.Model):
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Authors of book"

    def __str__(self):
        return self.full_name

class Redaction(models.Model):
    name=models.TextField()

    def __str__(self):
        return self.name


class Friend(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="one_author")
    copy_count = models.SmallIntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE)
    authors = models.ManyToManyField(
        Author,
        through='Inspiration',
        through_fields=('book', 'author'),
    )
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="inspired_works",
        null=True,
    )
