from django import forms


class EmailPredictForm(forms.Form):
    first_name = forms.CharField(
        label='First Name', max_length=100, required=True)
    last_name = forms.CharField(
        label='Last Name', max_length=100, required=True)
    domain = forms.CharField(label='Domain', max_length=100, required=True)
