from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    # Custom validation added here

    class Meta():
        model = User
        fields = '__all__'
