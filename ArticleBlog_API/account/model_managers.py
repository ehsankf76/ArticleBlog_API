from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, first_name, last_name, image=None, password=None):
        """
        Creates and saves a User with the given username, email, date of
        birth, first_name, last_name, created_time, image and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            image=image
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, first_name, last_name, image=None, password=None):
        """
        Creates and saves a superuser with the given username, email, date of
        birth, first_name, last_name, created_time, image and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            image=image,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user