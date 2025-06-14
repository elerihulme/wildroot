from django import forms
from .models import UserPlant

class UserPlantForm(forms.ModelForm):
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