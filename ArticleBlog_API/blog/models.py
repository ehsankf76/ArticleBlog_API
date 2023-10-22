from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(Category, self).save(*args, **kwargs)