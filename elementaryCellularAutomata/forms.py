from django import forms


class WolframForm(forms.Form):
    nmb = forms.IntegerField(min_value=0, max_value=256)