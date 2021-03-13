from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'


class ProductFoundForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['name' , 'description','date','time']
		widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }