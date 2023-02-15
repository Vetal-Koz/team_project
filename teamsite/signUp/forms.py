from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, PasswordInput, EmailInput


User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
                                                                           'class': 'input-btn',
                                                                            'placeholder': 'example@test.com',
                                                                            'name': 'emauil_us'
                                                                           }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input-btn'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].widget.attrs['class'] = 'input-btn'
        self.fields['password2'].widget.attrs['placeholder'] = 'Min 8 charaters long'
        self.fields['password2'].widget.attrs['class'] = 'input-btn'



# class UserLoginForm(AuthenticationForm):
#
#
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#
#         self.fields['password'].widget.attrs['placeholder'] = 'Min 8 charaters long'
#
#     email = forms.EmailField(widget=forms.EmailInput(attrs={
#         'class': 'input-btn',
#         'placeholder': 'example@test.com'
#     }))
#
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'input-btn',
#         'placeholder': 'Min 8 charaters long'
#     }))