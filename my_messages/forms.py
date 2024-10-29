from django import forms
from .models import Message, Profile

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name']
