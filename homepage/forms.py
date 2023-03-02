from .models import Member
from django import forms


class NameForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone_number', 'email']

        def __init__(self, *args, **kwargs):
            super(NameForm, self).__init__(*args, **kwargs)
            self.fields['name'].label = ""
            self.fields['phone_number'].label = ""
            self.fields['email'].label = ""
