from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__' #all the fields in the model 
        # fields=['name','age','gender','email'] # specifed fields 
        # exclude=['age'] # to exclude specific fields 
    
    widgets={'name':forms.TextInput(attrs={'placeholder':'enter the name'})}
    
