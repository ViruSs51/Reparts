from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User

#class SignUpForm(UserCreationForm):
#    first_name = forms.CharField(
#        max_length=30, 
#        required=False, 
#        widget=forms.TextInput(attrs={'placeholder': 'Имя'}),
#        help_text='Optional.'
#    )
#    last_name = forms.CharField(
#        max_length=30, 
#        required=False, 
#        widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}),
#        help_text='Optional.'
#    )
#    email = forms.EmailField(
#        max_length=254, 
#        widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта'}),
#        help_text='Required. Enter a valid email address.'
#    )
#    password1 = forms.CharField(
#        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
#        label='Password'
#    )
#    password2 = forms.CharField(
#        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
#        label='Password confirmation'
#    )
#
#    class Meta:
#        model = User
#        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Емейл'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Юзернайм'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Емайл'}))
    agree_privacy_policy = forms.BooleanField(
        required=True,
        error_messages={'required': 'Вы должны принять условиями использования и политикой конфиденциальности'},
        widget=forms.CheckboxInput(attrs={'class': 'auth-form__column_checkbox'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'agree_privacy_policy')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        
        return cd['password2']