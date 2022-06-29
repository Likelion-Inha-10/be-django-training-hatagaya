from dataclasses import dataclass
from unicodedata import name
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, id, name, MBTI, password):
        user = self.model(
            id = id,
            name = name,
            MBTI = MBTI,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, name, password):
        user = self.create_user(
            id = id,
            name = name,
            MBTI = "",
            password= password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        


class User(AbstractBaseUser, PermissionsMixin):
    
    id = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    MBTI = models.CharField(default="", max_length=4)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.id

    def is_staff(self):
        return self.is_admin
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
