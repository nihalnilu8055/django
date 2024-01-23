from django import forms

class Mobile_Forms(forms.Form):
    Mobile_name=forms.CharField()
    price=forms.IntegerField()
    images=forms.CharField()