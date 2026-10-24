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

class ActivityFilterBaseForm(forms.Form):
    max_budget=forms.DecimalField(max_digits=10,
                              decimal_places=2,
                              required=False,
                              min_value=0,
                              label="Maximum budget (€)",
                              widget=forms.NumberInput(attrs={'placeholder':'Any budget','step':'0.01'}))
    distance=forms.DecimalField(max_digits=10,
                                decimal_places=2,
                                required=False,
                                min_value=0,
                                max_value=40075.02,
                                label="Maximum distance (km)",
                                widget=forms.NumberInput(attrs={'placeholder':'Any distance','step':'0.01'}))
    environment=forms.ChoiceField(choices=(("",'Any environment'),
                                           ('Outdoors','Outdoors'),
                                           ('Indoors','Indoors')),
                                  required=False,
                                  widget=forms.Select,
                                  label="Environment (Outdoor, Indoors or Any)")
    pet_friendly=forms.ChoiceField(choices=(("",'Any'),('yes','Yes'),('no','No')),
                                  required=False,
                                  widget=forms.Select,
                                  label="Pet-friendly")

class ActivityFilterForm(ActivityFilterBaseForm):
    min_budget = forms.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    required=False,
                                    min_value=0,
                                    label="Minimum budget (€)",
                                    widget=forms.NumberInput(attrs={'placeholder': 'Any budget', 'step': '0.01'}))

    sort=forms.ChoiceField(choices=(("","Default order"),
                                    ('name','Name A-Z'),
                                    ('-name','Name Z-A'),
                                    ("budget","Budget Low to High"),
                                    ('-budget','Budget High to Low'),
                                    ('distance','Distance to Nearest First'),
                                    ('-distance','Distance to Farthest First'),
                                    ),
                           required=False,
                           widget=forms.Select,
                           label='Sort by')

    def clean(self):
        cleaned_data=super().clean()
        min_budget=cleaned_data.get('min_budget')
        max_budget=cleaned_data.get('max_budget')

        if min_budget is not None and max_budget is not None:
            if max_budget < min_budget:
                raise forms.ValidationError("Minimum budget cannot be more than maximum budget")
        return cleaned_data
