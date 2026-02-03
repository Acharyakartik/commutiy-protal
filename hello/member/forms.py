from django import forms
from .models import MemberDetail,Member

class MemberDetailForm(forms.ModelForm):
    class Meta:
        model = MemberDetail
        fields = [
            'first_name',
            'middle_name',
            'surname',
            'date_of_birth',
            'age',
            'gender',
            'occupation',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
        }
