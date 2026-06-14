from django import apps
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Повторіть пароль")

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username': 'Логін', 'email': 'Email'}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Паролі не співпадають!")
        return cleaned_data