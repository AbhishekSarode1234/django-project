from django import forms
from .models import Member

class Memberform(forms.ModelForm):
    class Meta:
        model=Member
        fields=['firstname','lastname','rollno']