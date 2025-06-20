from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    """ Form to collect and validate delivery and contact details for an order. """
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
            ('GB', 'United Kingdom')
        ]
        self.fields['country'].initial = 'GB'
        self.fields['country'].widget.attrs['readonly'] = True

        # Add Bootstrap classes for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.label = field.label.title().replace('_', ' ')

        # Add HTML5 regex pattern to match server-side postcode validator
        self.fields['postcode'].widget.attrs['pattern'] = (
            r"(GIR ?0AA|[A-PR-UWYZ][0-9][0-9]? ?[0-9][ABD-HJLNP-UW-Z]{2}|"
            r"[A-PR-UWYZ][A-HK-Y][0-9][0-9]? ?[0-9][ABD-HJLNP-UW-Z]{2}|"
            r"[A-PR-UWYZ][0-9][A-HJKSTUW]? ?[0-9][ABD-HJLNP-UW-Z]{2}|"
            r"[A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]? ?[0-9][ABD-HJLNP-UW-Z]{2})"
        )
        self.fields['postcode'].widget.attrs['title'] = "Enter a valid UK postcode"