from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'country',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set country to UK only
        self.fields['country'].choices = [
            ('United Kingdom', 'United Kingdom')
        ]
        self.fields['country'].initial = 'United Kingdom'

        # Add Bootstrap classes for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.label = field.label.title().replace('_', ' ')