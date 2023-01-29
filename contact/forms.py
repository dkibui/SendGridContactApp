from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    fullname = forms.CharField(label='Full Name',
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'}))
    email = forms.EmailField(label='Email Address',
                             widget=forms.TextInput(attrs={'placeholder': 'Enter your email address'}))
    message = forms.CharField(label='Message',
                              widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}))

    class Meta:
        model = Contact
        fields = ['fullname', 'email', 'message']
