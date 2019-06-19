from django import forms


class DiamondsForm(forms.Form):
    letter = forms.CharField(label='letter', max_length=1)
