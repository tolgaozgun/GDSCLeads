from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class City(models.Model):
    id = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], primary_key=True)


class Lead(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=300)
    city = models.ForeignKey(City, related_name="city", on_delete=models.CASCADE, null=False, blank=False)
    photo = models.ImageField(upload_to="profile", null=True, default="profile/avatar.png")
    social_instagram = models.CharField(max_length=300, null=True, blank=True)
    social_website = models.CharField(max_length=300, null=True, blank=True)
    social_facebook = models.CharField(max_length=300, null=True, blank=True)
    social_twitter = models.CharField(max_length=300, null=True, blank=True)
    social_linkedin = models.CharField(max_length=300, null=True, blank=True)
    social_email = models.CharField(max_length=300, null=True, blank=True)
    social_youtube = models.CharField(max_length=300, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self is None:
            return "None"
        else:
            return self.first_name + " " + self.last_name

