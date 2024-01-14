from django import forms
from .models import ContactForm


class PostContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = [
            'child_name1',
            'child_name2',
            'parent_name1',
            'parent_name2',
            'email',
            'phone_number',
            'contact_category',
            'comment',
        ]
    