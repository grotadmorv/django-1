from django import forms


class HashidForm(forms.Form):
    hash_value = forms.CharField(required=True)