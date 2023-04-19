from django import forms
from django.forms.widgets import DateInput
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'date_of_birth', 'physics_marks', 'chemistry_marks', 'maths_marks', 'computer_science_marks']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'})
        }
        labels = {
            'name': 'Student Name',
            'date_of_birth': 'Date of Birth',
            'physics_marks': 'Physics Marks (out of 100)',
            'chemistry_marks': 'Chemistry Marks (out of 100)',
            'maths_marks': 'Maths Marks (out of 100)',
            'computer_science_marks': 'Computer Science Marks (out of 100)',
        }


        def __init__(self, *args, **kwargs):
            super().__init__( *args, **kwargs )
            self.fields['date_of_birth'].input_formats = ['%Y-%m-%d']
