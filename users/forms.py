from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import NewUser


class RegisterForm(UserCreationForm):
    # declare the fields you will show
    username = forms.CharField(label="Your Username")
    # first password field
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Your Password")
    # confirm password field
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Repeat Your Password")
    email = forms.EmailField(label = "Email Address")
    first_name = forms.CharField(label = "Name")
 
    # this sets the order of the fields
    class Meta:
        model = NewUser
        fields = ("first_name", "email", "username", "password1", "password2")
 
    # this redefines the save function to include the fields you added
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.user_name = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            user.save()

        return user