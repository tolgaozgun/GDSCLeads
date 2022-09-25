from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    city = models.ForeignKey(City, related_name="city", on_delete=models.CASCADE, null=False, blank=False)
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



class Lead(models.Model):
    name = models.CharField(max_length=300)
    community = models.ForeignKey(Community, related_name="community", on_delete=models.CASCADE, null=False, blank=False)
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

    def __str__(self):
        if self is None:
            return "None"
        else:
            return self.name

