
from django import forms
 
# creating a form
class InputForm(forms.Form):
 
    question = forms.CharField(max_length = 200)
    choice1 = forms.CharField(max_length = 100)
    choice2 = forms.CharField(max_length = 100)
  
    