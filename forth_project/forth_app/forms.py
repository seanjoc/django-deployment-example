from django.forms import ModelForm
from forth_app.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        labels = {'ufirst_name':'First Name','ulast_name':'Last Name','uemail':'Email'}
        fields = ['ufirst_name','ulast_name','uemail']
