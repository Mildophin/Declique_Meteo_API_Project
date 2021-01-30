from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Ville ?'}),
        }  # Met a jour la class input pour avoir la bonne class et le placeholder correspondant.
