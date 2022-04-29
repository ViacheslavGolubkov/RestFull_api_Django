from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, is_subscriber=True, is_author=False,
                    is_active=True):
        if not email:
            raise ValueError("Это поле должно быть заполнено")
        if not password:
            raise ValueError("Это поле должно быть заполнено")

        user = self.model(
            email=self.normalize_email(email),
            is_staff=False,
            is_superuser=False
        )
        user.set_password(password)
        user.is_active = is_active
        user.subscriber = is_subscriber
        user.author = is_author
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Это поле должно быть заполнено")
        if not password:
            raise ValueError("Это поле должно быть заполнено")

        user = self.model(
            email=self.normalize_email(email),
            is_staff=True,
            is_superuser=True
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):

    username = None
    email = models.EmailField(verbose_name='E-mail', unique=True)
    password = models.CharField(max_length=100, blank=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    is_subscriber = models.BooleanField(verbose_name='Подписчик', default=True)
    is_author = models.BooleanField(verbose_name='Автор', default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email