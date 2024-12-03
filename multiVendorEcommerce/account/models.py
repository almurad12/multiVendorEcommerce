from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
from account.manager import MyUserManager
# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =["first_name","last_name"]
    objects = MyUserManager()

    def __str__(self):
        return self.email
    
# class MyUserManager(BaseUserManager):
#     def create_user(self,email,password=None):
#         if not email:
#             raise ValueError("user must be email")
#         user = self.model(
#             email = self.normalize_email(email),
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#     def create_superuser(self,email,password=None):
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.is_admin =True
#         user.is_superuser =True
#         user.is_active =True
#         user.save(using=self._db)
#         return user


