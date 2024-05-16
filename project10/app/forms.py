from django import forms
from app.models import *

def validator_for_b(data):
    fdata = data.lower()
    if fdata.startswith('b'):
        raise forms.ValidationError('The School Name is startting with "B"')

def validator_for_len(data):
    if len(data)>5:
        raise forms.ValidationError('Has More than 5 characters')
    
def validator_for_duplicate(data):
    SO = School.objects.get(sname=data)
    if SO:
        raise forms.ValidationError('Invalid data')




class SchoolForm(forms.Form):
    sname = forms.CharField(max_length=50, required=False, validators=[validator_for_b,validator_for_len,validator_for_duplicate])
    sprincipal = forms.CharField( max_length=50, required=False)
    saddress = forms.CharField( max_length=50, required=False)
