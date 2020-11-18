from django import forms
from .models import Goals, ToDo
class GoalForm(forms.ModelForm):
    goal = forms.CharField()
    

    class Meta:
        model = Goals
        fields = ['goal']

class TodoForm(forms.ModelForm):
	title = forms.CharField()
	desc = forms.CharField()
	

	class Meta:
		model = ToDo
		fields = ['title','desc'] 