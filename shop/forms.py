from django import forms

from .models import Callback

class CallbackForm(forms.ModelForm):

    class Meta:
        model = Callback
        fields = ('name', 'phone', 'description')