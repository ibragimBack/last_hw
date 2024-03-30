from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class CustomUserCreationForm(UserCreationForm):
    date_of_births = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    place_of_births = forms.ChoiceField(choices=models.CustomUser.PLACES_OF_KG)
    height = forms.IntegerField()
    weight = forms.IntegerField()
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', widget=forms.TextInput(attrs={'placeholder': 'Напишите ваш номер телефона'}))
    favourite_color = forms.ChoiceField(choices=models.CustomUser.COLORS)
    hobby = forms.CharField()
    profession = forms.CharField()

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'date_of_births',
            'place_of_births',
            'height',
            'weight',
            'favourite_color',
            'hobby',
            'profession'
        )

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.date_of_births = self.cleaned_data['date_of_births']
        user.place_of_births = self.cleaned_data['place_of_births']
        user.height = self.cleaned_data['height']
        user.weight = self.cleaned_data['weight']
        user.favourite_color = self.cleaned_data['favourite_color']
        user.hobby = self.cleaned_data['hobby']
        user.profession = self.cleaned_data['profession']
        if commit:
            user.save()
        return user
