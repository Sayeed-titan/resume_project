from django import forms
from .models import ResumeModel

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        # '__all__' tells Django to create an input field for every single item in our model!
        fields = '__all__'