from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password, name, params=None):
        if not email:
            raise ValueError("Email is required to create an account")

        try:
            query = User.objects.get(email=email)
            if query is not None:
                raise ValueError("This email is already registered")
        except User.DoesNotExist:
            pass

        user = self.model(email=self.normalize_email(email), name=name)

        user.set_password(password)
        user.save(using=self._db)

        if params is not None:
            User.objects.filter(id=user.id).update(**params)

        return user

    def update_user(self, email, password, name, params=None):
        if not email:
            raise ValueError("Email is required to create an account")

        try:
            query = User.objects.get(email=email)
            if query is None:
                raise ValueError("This email is not registered")
        except User.DoesNotExist:
            raise ValueError("This email is not registered")

        print("Updating user with password ")
        print(password)
        if password is not None:
            query.set_password(password)
            print("Updated")
        query.name = name
        query.save(using=self._db)

        if params is not None:
            User.objects.filter(id=query.id).update(**params)

        return query

    def update_user_admin(self, id, email, password, name, params=None):
        if not email:
            raise ValueError("Email is required to create an account")

        try:
            query = User.objects.get(id=id)
            if query is None:
                raise ValueError("This user ID does not exists")
        except User.DoesNotExist:
            raise ValueError("This user ID does not exists")

        if password is not None:
            query.set_password(password)
        query.name = name
        query.save(using=self._db)

        if params is not None:
            User.objects.filter(id=query.id).update(**params)

        return query

    def create_staff(self, email, password):
        if not email:
            raise ValueError("Email is required to create an account")

        user = self.model(email=self.normalize_email(email), )

        user.set_password(password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError("Email is required to create an account")

        user = self.model(email=self.normalize_email(email), )

        user.set_password(password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    # Community member lines
    community = models.ForeignKey("Community", related_name="lead", on_delete=models.CASCADE,
                                  null=True, blank=True)
    photo = models.ImageField(upload_to="lead", null=True, default="lead/avatar.png")
    biography = models.TextField()
    social_instagram = models.CharField(max_length=300, null=True, blank=True)
    social_website = models.CharField(max_length=300, null=True, blank=True)
    social_facebook = models.CharField(max_length=300, null=True, blank=True)
    social_twitter = models.CharField(max_length=300, null=True, blank=True)
    social_linkedin = models.CharField(max_length=300, null=True, blank=True)
    social_email = models.CharField(max_length=300, null=True, blank=True)
    social_youtube = models.CharField(max_length=300, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_lead = models.BooleanField(default=False)
    is_core_team = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default
    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


class Venue(models.Model):
    name = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="community", null=True, default="community/avatar.png")
    city = models.ForeignKey("City", related_name="venue_city", on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        if self is None:
            return "None"
        else:
            return self.name


class City(models.Model):
    id = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(81)], primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        if self is None:
            return "None"
        else:
            return self.name


class Community(models.Model):
    name = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="community", null=True, default="community/avatar.png")
    city = models.ForeignKey(City, related_name="community_city", on_delete=models.CASCADE, null=False, blank=False)
    biography = models.TextField()
    social_instagram = models.CharField(max_length=300, null=True, blank=True)
    social_website = models.CharField(max_length=300, null=True, blank=True)
    social_facebook = models.CharField(max_length=300, null=True, blank=True)
    social_twitter = models.CharField(max_length=300, null=True, blank=True)
    social_linkedin = models.CharField(max_length=300, null=True, blank=True)
    social_email = models.CharField(max_length=300, null=True, blank=True)
    social_youtube = models.CharField(max_length=300, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        if self is None:
            return "None"
        else:
            return self.name


class Event(models.Model):
    name = models.CharField(max_length=400)
    photo = models.ImageField(upload_to="event", null=True, default="event/avatar.png")
    communities = models.ManyToManyField(Community, related_name="events", blank=True)
    description = models.TextField()
    venue = models.ForeignKey(Venue, related_name="event", on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateTimeField(blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        # sort by "the date" in descending order unless
        # overridden in the query with order_by()
        ordering = ['-date']

    def __str__(self):
        if self is None:
            return "None"
        else:
            return self.name
