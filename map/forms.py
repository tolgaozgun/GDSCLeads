from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name']

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
        if password and password_again and password != password_again:
            self.add_error("password_again", "Your passwords must match")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': '',
            'email': 'example@email.com',
            'password': '',
            'password_again': '',
        }
        for key, value in placeholders.items():
            # self.fields[key].widget.attrs['placeholder'] = value
            self.fields[key].widget.attrs['class'] = 'form-control'
