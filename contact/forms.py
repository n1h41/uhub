from django import forms
from .models import contact_us

class contact_us_form(forms.ModelForm):
    class Meta :
        model = contact_us
        fields = ['name', 'phone', 'email', 'message']