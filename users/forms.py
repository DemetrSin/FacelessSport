from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'username', 'country', 'age', 'number', 'sport', 'telegram', 'viber',
            'whatsapp', 'signal', 'linkedin', 'youtube', 'tiktok',
            'instagram', 'facebook', 'twitter'
        ]
