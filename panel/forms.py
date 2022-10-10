from datetime import datetime

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from map.models import User, Community, City, Event, Venue


class DateInput(forms.DateInput):
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'


class AddLeadForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'photo', 'community', 'biography',
                  'social_instagram', 'social_email', 'social_facebook',
                  'social_twitter', 'social_website', 'social_linkedin',
                  'social_youtube', 'is_lead', 'is_core_team']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        users = User.objects.filter(email=email)
        if users.exists():
            raise forms.ValidationError("This email is already taken")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_again = cleaned_data.get("password_again")
        community = cleaned_data.get("community")
        if password and password_again and password != password_again:
            self.add_error("password_again", "Your passwords must match")
        if community is not None:
            cleaned_data["latitude"] = community.latitude
            cleaned_data["longitude"] = community.longitude
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '',
            'email': 'example@email.com',
            'password': '',
            'password_again': '',
            'photo': '',
            'community': '',
            'biography': '',
            'social_instagram': '',
            'social_email': '',
            'social_facebook': '',
            'social_twitter': '',
            'social_website': '',
            'social_linkedin': '',
            'social_youtube': '',
        }
        for key, value in placeholders.items():
            self.fields[key].widget.attrs['class'] = 'form-control'


class AddEventForm(forms.ModelForm):
    picked_date = forms.DateField(widget=DateInput())
    picked_time = forms.TimeField(widget=TimePickerInput())

    class Meta:
        model = Event
        fields = ['name', 'photo', 'communities', 'description',
                  'venue']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '',
            'photo': '',
            'communities': '',
            'description': '',
            'venue': '',
            'picked_date': '',
            'picked_time': '',
        }
        for key, value in placeholders.items():
            self.fields[key].widget.attrs['class'] = 'form-control'


class AddVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'photo', 'city', 'latitude', 'longitude']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '',
            'photo': '',
            'city': '',
            'latitude': '',
            'longitude': '',
        }
        for key, value in placeholders.items():
            self.fields[key].widget.attrs['class'] = 'form-control'


class EditLeadForm(AddLeadForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    password_again = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, required=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_again = cleaned_data.get("password_again")
        if password != password_again:
            self.add_error("password_again", "Your passwords must match")
        return cleaned_data


class AddCommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'photo', 'biography',
                  'social_instagram', 'social_email', 'social_facebook',
                  'social_twitter', 'social_website', 'social_linkedin',
                  'social_youtube', 'latitude', 'longitude', 'city']

    def clean(self):
        cleaned_data = super().clean()
        communities = Community.objects.filter(latitude=self.cleaned_data.get("latitude"),
                                               longitude=self.cleaned_data.get("longitude"))
        if communities.exists():
            raise forms.ValidationError("This address already exists")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '',
            'photo': '',
            'biography': '',
            'social_instagram': '',
            'social_email': '',
            'social_facebook': '',
            'social_twitter': '',
            'social_website': '',
            'social_linkedin': '',
            'social_youtube': '',
            'latitude': '',
            'longitude': '',
            'city': '',
        }
        for key, value in placeholders.items():
            self.fields[key].widget.attrs['class'] = 'form-control'


class AddCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'id']

    def clean(self):
        cleaned_data = super().clean()
        cities = City.objects.filter(id=cleaned_data.get("id"))
        if cities.exists():
            raise forms.ValidationError("This city ID already exists")
        cities = City.objects.filter(name=cleaned_data.get("id"))
        if cities.exists():
            raise forms.ValidationError("This city name already exists")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '',
            'id': '',
        }
        for key, value in placeholders.items():
            self.fields[key].widget.attrs['class'] = 'form-control'


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = User
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get("email")
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                print("Invalid email and password")
                raise forms.ValidationError("Invalid email and password combination")
            else:
                print("Valid email and password")
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'example@email.com',
            'password': '',
        }
        for key, value in placeholders.items():
            self.fields[key].widget.attrs['placeholder'] = value
            self.fields[key].widget.attrs['class'] = 'form-control'
