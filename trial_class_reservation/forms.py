from django import forms
from .models import ReservationForm


class PostReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationForm
        fields = [
            'child_name1',
            'child_name2',
            'parent_name1',
            'parent_name2',
            'email',
            'phone_number',
            'schedule',
            'content',
            'comment'
        ]
    