from django import forms
from jobportal_app.models import Employer,Jobs,Candidate

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = "__all__"

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"

class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = "__all__"