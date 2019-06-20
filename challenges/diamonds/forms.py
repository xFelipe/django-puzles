from django import forms
from django.core.validators import RegexValidator


class DiamondsForm(forms.Form):
    _my_validator = RegexValidator(r'[a-zA-Z]', 'O caractere deve ser uma letra')
    letter = forms.CharField(label='Letra',
                             max_length=1,
                             required=True,
                             validators=[_my_validator])
