from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import *

class AlumniForm(ModelForm):
	# EMPLOYED = (
	# 	        ('Yes','Yes'),('No','No'),
	# 		   )
	# employed = forms.ChoiceField(choices=EMPLOYED, widget=forms.RadioSelect)

	class Meta:
		model = Alumni
		fields = '__all__'
		exclude = ['user']
		widgets={
		 	'incaseofemergency': forms.TextInput(attrs={'class':'form-control','placeholder':'Incase of Emergency'}),
		# 	'firstname' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'lastname' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'Gender' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'email' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'phone' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'address' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'zipcode' : forms.TextInput(attrs={'class':'form-control'}),
		# 	'Course' : forms.TextInput(attrs={'class':'form-control'}),
		 }

class JobsForm(ModelForm):
	class Meta:
		model = Jobs
		fields = '__all__'

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = '__all__'

#class UserEmployedForm(ModelForm):
		#models = UserEmployed
		#fields = '__all__'
class EmployedModal(ModelForm):
	class Meta:
		model = Employed
		fields = '__all__'
		exclude = ['alumni']


		

class CreateUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required = False)
	last_name = forms.CharField(max_length=30, required = False)



	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

		#model = UserEmployed
		#fields = '__all__'
