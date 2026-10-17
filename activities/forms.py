from django import forms
from activities.models import Activity


class ActivityBaseForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityCreateForm(ActivityBaseForm):
    ...

class ActivityEditForm(ActivityBaseForm):
    ...

class ActivityDeleteForm(ActivityBaseForm):
    ...