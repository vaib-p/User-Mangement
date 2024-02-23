from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    billing_group = models.CharField(max_length=50, choices=[("free", "Free"), ("pro", "Pro"), ("premium", "Premium")])
    
    def __str__(self):
        return self.name
class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    organizations = models.ManyToManyField(Organization, related_name='members')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin





class Role(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="roles")

    def __str__(self):
        return self.name


class MembershipRequest(models.Model):
    STATUS_CHOICES = [("pending", "Pending"), ("accepted", "Accepted"), ("rejected", "Rejected")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.user} - {self.organization} - {self.status}"
