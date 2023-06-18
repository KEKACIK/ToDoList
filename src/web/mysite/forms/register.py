from django import forms
from django.contrib.auth.forms import UserCreationForm

from admin_web.models import Telegram


class RegisterForm(UserCreationForm):
    telegram = forms.IntegerField()

    def save_and_telegram(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        Telegram(user=user, telegram_id=self.cleaned_data["telegram"]).save()
        return user
