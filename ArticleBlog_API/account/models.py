from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .model_managers import UserManager
from django.template.defaultfilters import slugify


class User(AbstractBaseUser):
    username = models.CharField(verbose_name="username", max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True, editable=False)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/Users", null=True)
    is_author = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "date_of_birth"]

    def __str__(self):
        return f"{self.username} - {self.email}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin