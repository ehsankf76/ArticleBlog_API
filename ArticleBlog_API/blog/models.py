from django.db import models
from django.template.defaultfilters import slugify
from account.models import User


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True, editable=False, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    content = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/Articles", null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="articles")

    def get_average_rating(self):
        comments = self.comment_set.all()
        if comments:
            all_ratings = [comment.rating for comment in comments]
            total_rating = sum(all_ratings)
            count_rating = len(all_ratings)-all_ratings.count(0)
            average_rating = total_rating/count_rating
            return average_rating
        return 0
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField()
    create_time = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(1, 6)])

    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.writer} - {self.text[:20]}"