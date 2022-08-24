# from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator


class CaseInsensitiveUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD + "__iexact": username})


class CustomUser(AbstractUser):
    username_validator = ASCIIUsernameValidator()
    objects = CaseInsensitiveUserManager()


# class CustomUser(AbstractBaseUser):
#     username_validator = ASCIIUsernameValidator()
#     objects = CaseInsensitiveUserManager()

#     EMAIL_FIELD = "email"
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]

#     username = models.CharField(
#         _("username"),
#         max_length=150,
#         unique=True,
#         help_text=_("Required. 150 characters or fewer. ASCII letters and digits only."),
#         validators=[username_validator],
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#     )
#     first_name = models.CharField(_("first name"), max_length=150, blank=True)
#     last_name = models.CharField(_("last name"), max_length=150, blank=True)
#     age = models.PositiveIntegerField(_("age"), blank=True, null=True)
#     email = models.CharField(
#         _("email address"),
#         max_length=256,
#         unique=True,
#         error_messages={
#             "unique": _("A user with that email address already exists."),
#         },
#     )
#     is_superuser = models.BooleanField(
#         _("superuser status"),
#         default=False,
#         help_text=_("Designates whether the user have all permissions on site."),
#     )
#     is_staff = models.BooleanField(
#         _("staff status"),
#         default=False,
#         help_text=_("Designates whether the user can log into this admin site."),
#     )
#     is_active = models.BooleanField(
#         _("active"),
#         default=True,
#         help_text=_(
#             "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
#         ),
#     )
#     date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

#     def clean(self):
#         super().clean()
#         self.email = self.__class__.objects.normalize_email(self.email)

#     def get_full_name(self):
#         """Returns the first_name plus the last_name, with a space in between."""
#         full_name = "%s %s" % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         """Returns the short name for the user."""
#         return self.first_name

#     def has_perm(self, perm, obj=None):
#        return self.is_superuser

#     def has_module_perms(self, app_label):
#        return self.is_superuser

#     class Meta:
#         verbose_name = _("user")
#         verbose_name_plural = _("users")
