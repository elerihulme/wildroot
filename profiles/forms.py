from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """ Form for updating the user's default delivery information stored in their profile. """
    class Meta:
        model = UserProfile
        exclude = ('user', 'default_country')
    
    def __init__(self, *args, **kwargs):
        """
        Customize form initialization:
        - Add Bootstrap 'form-control' class for styling.
        - Format field labels to title case with spaces.
        """
        super().__init__(*args, **kwargs)

        # Add Bootstrap classes for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.label = field.label.title().replace('_', ' ')