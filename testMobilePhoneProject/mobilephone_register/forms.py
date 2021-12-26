from django import forms
from django.core.exceptions import ValidationError

from .models import Mobile


class MobileForm(forms.ModelForm):

    class Meta:
        model = Mobile
        # fields = '__all__'
        fields = ('brand_name', 'model', 'color', 'jan_code')
        labels = {
            'brand_name': 'Brand Name',
            'jan_code': 'JAN Code'
        }
