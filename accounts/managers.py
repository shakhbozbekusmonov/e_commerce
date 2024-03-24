from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
  
  def create_user(self, email, password, **extra_fields):
    
    if not email: 
      raise ValueError('Email must be provided')
    email = self.normalize_email(email)
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    user = self.model(email=email, **extra_fields)
    user.password = make_password(password)
    user.save(using=self._db)
    return user
  
  def crete_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)

    if extra_fields.get("is_staff") is not True:
        raise ValueError("Superuser must have is_staff=True.")
    if extra_fields.get("is_superuser") is not True:
        raise ValueError("Superuser must have is_superuser=True.")
      
    user = self.model(email=email, **extra_fields)
    user.password = make_password(password)
    user.save(using=self._db)
    return user
  