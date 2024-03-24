from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_('Email'), unique=True)
    phone_number = models.CharField(_('Phone Number'), max_length=20)
    address = models.TextField(_('Address'))
    username = models.CharField(
        _("username"),
        max_length=150,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        null=True,
        blank=True
    )
  
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    def __str__(self):
        return self.email
 
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class VerificationOtp(models.Model):
    class VerificationType(models.TextChoices):
        REGISTER = 'register', _('Register')
        RESET_PASSWORD = 'reset_password', _('Reset Password')

    code = models.IntegerField(_('Code'))
    type = models.CharField(_('Type'), choices=VerificationType.choices)
    expires_in = models.DateTimeField(_('Expires in'))

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='verification_otp')

    def __str__(self):
        return f"{self.user.email} | code: {self.code}"

    class Meta:
        verbose_name = _('Verification Otp')
        verbose_name_plural = _('Verification Otps')


class UserAddress(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    phone_number = models.CharField(_('Phone Number'), max_length=20)
    apartment = models.CharField(_('Apartment'), max_length=120)
    street = models.TextField(_('Street'))

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_adresses')
    # city = models.ForeignKey()

    def __str__(self):
        return f"{self.user.id} {self.name}"

    class Meta:
        verbose_name = _('User Address')
        verbose_name_plural = _('User Addresses')

