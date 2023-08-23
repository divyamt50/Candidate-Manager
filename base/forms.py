from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'password1':'Enter Password',
            'password2':'Confirm Password', 
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    


class CandidateDirectoryForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    login_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    logout_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    created_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    modified_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    experience_level = forms.ModelChoiceField(
        queryset=Experiencelevel.objects.all(),
        widget=forms.Select,  
    )

    class Meta:
        model = CandidateDirectory
        fields = [
            'event',
            'job_position',
            'recruiter_alert',
            'first_name',
            'last_name',
            'email',
            'persona',
            'role',
            'screening_mode',
            'dob',
            'gender',
            'marital_status',
            'contact_no_primary',
            'contact_no_alternate',
            'referred_by',
            'referred_by_other',
            'address_line',
            'city',
            'pincode',
            'experience_level',
            'education_level',
            'education_qualification',
            'education_specialization',
            'education_specialization_other',
            'education_institution',
            'years_of_experience',
            'current_employer',
            'current_designation',
            'current_monthly_salary',
            'expected_monthly_salary',
            'reason_for_change',
            'notice_period',
            'photo',
            'resume',
            'login_time',
            'logout_time',
            'ip_address',
            'geo_location',
            'created_date',
            'created_by',
            'modified_date',
            'modified_by',
            'status',
        ]
        