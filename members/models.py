"""
This is to default email as the username instead of letting the user to pick an username
"""

from django.db import models, transaction
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils.translation import ugettext as _
from django.core.mail import send_mail


class AccountQuerySet(models.QuerySet):

    def superadmins(self):
        return self.filter(is_superadmin=True)

    def pending(self):
        return self.exclude(is_active=True)

    def active(self):
        return self.filter(is_active=True)


class AccountManager(UserManager.from_queryset(AccountQuerySet)):

    use_in_migrations = False

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        kwargs.setdefault('is_superadmin', False)
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    @transaction.atomic
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superadmin', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_superadmin') is not True:
            raise ValueError('Superuser must have is_superadmin=True.')

        user = self.create_user(email, password=password, **kwargs)

        return user


class Account(PermissionsMixin, AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = None
    email = models.EmailField(unique=True, verbose_name=_('E-mail Address'))
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Active'))
    is_superadmin = models.BooleanField(default=False, verbose_name=_('Superadmin'))

    objects = AccountManager()

    @property
    def get_full_name(self):
        return ' '.join((x for x in [self.first_name, self.last_name] if x))

    @property
    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.is_superadmin

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        full_name = self.get_full_name
        if full_name.strip() != '':
            return full_name

        if self.email:
            return self.email

        return self.pk

    class Meta:
        ordering = ('first_name', 'last_name', 'email',)

