from django import forms

class AssayInputForm(forms.Form):
    target = forms.CharField(label='Target (gene/protein)', max_length=200)
    goal = forms.CharField(label='Experimental Goal', widget=forms.Textarea)