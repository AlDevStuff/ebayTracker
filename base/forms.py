from django import forms
from .models import Item


class MainForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('url', 'target_price', 'receiver_email',)

        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control my-input mb-4'}),
            'target_price': forms.TextInput(attrs={'class': 'form-control my-input mb-4'}),
            'receiver_email': forms.TextInput(attrs={'class': 'form-control my-input mb-4'}),

        }
