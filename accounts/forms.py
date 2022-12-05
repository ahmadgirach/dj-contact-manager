from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, EmailField, Form, PasswordInput, TextInput

UserModel = get_user_model()


class SignupForm(UserCreationForm):
    first_name = CharField(max_length=150, widget=TextInput(attrs={"autofocus": True}))
    last_name = CharField(max_length=150)
    email = EmailField(max_length=50)

    class Meta:
        model = UserModel
        fields = ("first_name", "last_name", "email", "password1", "password2")


class SigninForm(Form):
    email = EmailField(max_length=50)
    password = CharField(widget=PasswordInput())
