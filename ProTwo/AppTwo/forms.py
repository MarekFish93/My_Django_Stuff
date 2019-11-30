from django import forms
from AppTwo.models import User

class MyNewForm(forms.ModelForm):
    # first_name = User.first_name
    # last_name = User.last_name
    # email = User.email
    class Meta:
        model = User
        fields = "__all__"
