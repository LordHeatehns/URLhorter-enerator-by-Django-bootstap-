
from django import forms

from .models import Shorter

class ShorterForm(forms.ModelForm):
    long_url =  forms.URLField(widget=forms.URLInput(
        attrs={"class":"form-control form-control-lg","placeholder":"Your url ro shorten"}
    ))

    class Meta :
        model = Shorter
        fields = ('long_url',)