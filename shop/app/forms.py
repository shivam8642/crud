
from .models import Person,Student
from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    stream=forms.CharField(max_length=100)
    email=forms.EmailField()

class StudentCreateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model=Student
        fields="__all__"

    def clean_email(self):
      email=self.cleaned_data['email']
      if Student.objects.filter(email= email).exists():
        raise forms.ValidationError("Email already exists")
      return email

class StudentUpdateForm(forms.ModelForm):
    roll_no=forms.IntegerField()
    email = forms.EmailField()
    class Meta:
        model=Student
        fields="__all__"

    def clean_email(self):
      email=self.cleaned_data['email']
      roll_no=self.cleaned_data['roll_no']
    
      if Student.objects.filter(email__iexact=email).exclude(pk=roll_no).exists():
        raise forms.ValidationError("Email already exists")
      return email


class Personform(forms.ModelForm):
    class Meta:
        model=Person 
        fields="__all__"
