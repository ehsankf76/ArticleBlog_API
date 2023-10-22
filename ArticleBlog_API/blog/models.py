from django.db import models
from django.template.defaultfilters import slugify
from account.models import User


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True, editable=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True, editable=False)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/Articles", null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="articles")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)