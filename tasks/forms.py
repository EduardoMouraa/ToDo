from django import forms

from .models import Task
from django import forms

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'schedule_date')
        widgets = {
            'schedule_date': DateInput()
        }