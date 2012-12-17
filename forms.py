from django import forms
from django.contrib.auth.models import User

from . models import Account

class AccountAvatarForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset = User.objects.all(),
        widget = forms.HiddenInput(),
    )

    class Meta:
        model = Account
