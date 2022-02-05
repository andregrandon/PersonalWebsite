from django.core.mail import send_mail, get_connection

from django.forms.widgets import TextInput

from django import forms

class ContactForm(forms.Form):
   name = forms.CharField(label='sr-only', widget=forms.TextInput(
   attrs={'placeholder': 'Name', 'class': 'form-control', 'id':'c_name'}))

   email = forms.CharField(label='sr-only', widget=forms.TextInput(
     attrs={'placeholder': 'Subject', 'class': 'form-control', 'id':'c_email'}),
     required=False)

   message = forms.CharField(label='sr-only', widget=forms.TextInput(
   attrs={'placeholder': 'Message/Email', 'class': 'form-control', 'id':'c_message'}))
