from django import forms
from activities.models import Activity
from planact.mixins import DisabledFieldsMixin


class ActivityBaseForm(forms.ModelForm):
    PET_CHOICES=('True','Yes'),('False','No')
    pet_friendly=forms.TypedChoiceField(choices=PET_CHOICES,
                                        widget=forms.RadioSelect(),
                                        initial='False',
                                        coerce=lambda value: value == 'True')

    class Meta:
        model=Activity
        fields='__all__'
        labels={
            'name':'Activity Title',
            'description':'Brief Description',
            'budget':'Estimated Budget (EUR) ',
            'environment':'Environment',
            'distance':'Distance from Starting Point: (km)',
            'location':'Location',
            'pet_friendly':'Pet-Friendly',
            'category':'Category',
            'vibes':'Vibes',
        }
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'e.g. Go snowboarding'}),
            'description':forms.Textarea(attrs={'placeholder':'Describe the activity in more detail.'}),
            'budget':forms.NumberInput(attrs={'placeholder':'Enter a number'}),
            'environment':forms.Select,
            'distance':forms.NumberInput(attrs={'placeholder':'Enter a number'}),
            'location':forms.TextInput(attrs={'placeholder':'Enter a location of the activity'}),
            'category':forms.Select,
            'vibes':forms.CheckboxSelectMultiple(attrs={}),
        }

class ActivityCreateForm(ActivityBaseForm):
    ...

class ActivityEditForm(ActivityBaseForm):
    ...

class ActivityDeleteForm(DisabledFieldsMixin,ActivityBaseForm):
    ...