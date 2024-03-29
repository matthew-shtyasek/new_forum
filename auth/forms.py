from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import Field


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'username-class'})

        # self.fields -> {'username': <object Field>, 'password1': <object Field>, ...}
        for field in list(self.fields.values()):
            field.widget.attrs.update({'class': 'form-control'})


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in list(self.fields.values()):
            field.widget.attrs.update({'class': 'form-control'})
