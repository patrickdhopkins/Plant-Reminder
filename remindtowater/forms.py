from django import forms

from remindtowater.models import Plant


class AddPlantForm(forms.Form):
    name = forms.CharField(label='Plant Name:',
                           max_length=200,
                           error_messages={'required': 'Please enter plant name'},
                           required=True)
    instructions = forms.CharField(label='Instructions:',
                                   required=False)
    image = forms.ImageField(label='Picture of Plant:',
                             required=False)
    period = forms.DurationField(label='Frequency of Water:',
                                 error_messages={'required': 'Please frequency of watering'},
                                 required=True)

    class Meta:
        model = Plant
        fields = ('name', 'instructions', 'image', 'period', )
