from django import forms


class EmailPredictForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}), label='')
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}), label='')
    domain = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Domain'}), label='')


class CSVFileForm(forms.Form):
    csv_file = forms.FileField(label='')
