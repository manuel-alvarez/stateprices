__author__ = 'mnu'

from django import forms


class SourceForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, help_text='Try something original')
    api_key_name = forms.CharField(label='API key name', max_length=100, help_text='It has to be properly configured in settings')
    api_source = forms.CharField(label='API source', max_length=300, help_text='URL to be requested')
