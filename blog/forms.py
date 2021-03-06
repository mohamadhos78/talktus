from django import  forms
from .models import Contact

class contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]