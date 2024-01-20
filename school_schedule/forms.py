from django import forms
from .models import SchoolSchedule


class SchoolScheduleForm(forms.ModelForm):
        
    class Meta:
        model = SchoolSchedule
        fields = [
            'day_off',
        ]
        widgets = {
            'day_off': forms.CheckboxSelectMultiple,
        }