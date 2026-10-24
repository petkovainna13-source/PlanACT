from django import forms

class ActivityPickerForm(forms.Form):
    budget=forms.DecimalField(max_digits=10,
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
