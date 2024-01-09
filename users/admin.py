from django import forms
from django.utils.translation import gettext_lazy as _
from wagtail.users.forms import UserEditForm, UserCreationForm


# Register your models here.

class CustomUserEditForm(UserEditForm):
    user_id = forms.CharField(max_length=30, required=False, label=_("UserID"))
    user_type = forms.ChoiceField(
        required=True, 
        choices= [
            (0, '通塾生'),
            (1, '体験'),
        ],
        label=_("ユーザータイプ")
    )


class CustomUserCreationForm(UserCreationForm):
    user_id = forms.CharField(max_length=30, required=False, label=_("UserID"))
    user_type = forms.ChoiceField(
        required=True, 
        choices= [
            (0, '通塾生'),
            (1, '体験'),
        ],
        label=_("ユーザータイプ")
    )

#forms.IntegerField(required=True, label=_("UserType"))
    