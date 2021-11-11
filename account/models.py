from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, user_id, user_name, department, email, password=None):
        if (not user_id):
            raise ValueError("User must have user_id")
        
        user = self.model(
            user_id = user_id,
            email = self.normalize_email(email),
            user_name = user_name,
            department = department,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_id, user_name, department, email, password):
        user = self.create_user(
            user_id = user_id,
            user_name = user_name,
            department = department,
            email = email,
            password = password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    objects = UserManager()
    user_id = models.CharField(
        verbose_name = 'user_id',
        max_length=16,
        unique = True
    )
    email = models.EmailField(
        verbose_name = 'Email',
        max_length = 255,
        unique = True
    )
    user_name  = models.CharField(
        verbose_name = 'user_name',
        max_length=10
    )
    department = models.CharField(
        verbose_name = "Department",
        max_length=30
    )
    is_admin = models.BooleanField(
        verbose_name = 'is_admin',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name = 'is_active',
        default=False
    )

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_name', 'department', 'email']

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    #get 역할만 할 수 있는 함수
    @property
    def is_staff(self):
        return self.is_admin