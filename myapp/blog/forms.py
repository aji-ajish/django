from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    # name = forms.CharField(label="Name", max_length=100, required=True)
    # email = forms.EmailField(label="Email", required=True)
    # message = forms.CharField(label="Message", max_length=500, required=True,)
    # picture = forms.FileInput()
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'picture']
