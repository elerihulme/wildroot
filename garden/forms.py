from django import forms
from .models import UserPlant, UserPlantPhoto
from django.utils import timezone

class UserPlantForm(forms.ModelForm):
    """ Form to collect or update user plant details. """

    class Meta:
        model = UserPlant
        fields = ['plant_species', 'nickname', 'last_watered', 'notes']
        widgets = {
            'last_watered': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_last_watered(self):
        last_watered = self.cleaned_data.get('last_watered')
        if last_watered and last_watered > timezone.now():
            raise forms.ValidationError(
                "Last watered date cannot be in the future."
            )
        return last_watered

class UserPlantPhotoForm(forms.ModelForm):
    """ Form to upload user plant photo. """
    class Meta:
        model = UserPlantPhoto
        fields = ['image', 'image_alt', 'caption']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set optional by default
        self.fields['caption'].required = False
        self.fields['image_alt'].required = False

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['image_alt'].label = "Description"


    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        caption = cleaned_data.get('caption')
        image_alt = cleaned_data.get('image_alt')

        # If image is provided, caption and alt are required
        if image:
            if not caption:
                self.add_error('caption', 'Please add a caption for the photo.')
            if not image_alt:
                self.add_error('image_alt', 'Please add alt text for the photo.')

        return cleaned_data