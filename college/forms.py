from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'Application_Status', 'message',)
        widgets = {
            'aadhar_card_number': forms.TextInput(attrs={'placeholder': 'Enter Aadhar Card Number'}),
            'aadhar_card': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
