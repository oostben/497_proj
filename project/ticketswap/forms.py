from django import forms
from django.forms import widgets  

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import University, User, Listing


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "university")

    def clean(self):
        response = super().clean()

        uni = self.cleaned_data["university"]
        email = self.cleaned_data["email"]
        email_domain_name = email.split("@")[-1]

        print(uni.domain_name, " " , email_domain_name)
        if uni.domain_name != email_domain_name:
            raise forms.ValidationError(
                f"Email is not a valid {uni.name} email. Must have {uni.domain_name} domain name."
            )

        return response


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")

# class ListingForm(forms.ModelForm):
#     class Meta:
#         model = Listing
#         fields = ("user", "event", "pub_date", "price", "quantity", "description")
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

