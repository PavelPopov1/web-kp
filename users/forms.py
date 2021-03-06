from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4',
               'placeholder': 'Введите имя пользователя',
               'title': 'username должен содержать только латиницу и не повторять уже существующие'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4',
               'placeholder': 'Введите пароль',
               'title': 'Пароль должен быть длинее 8 символов и не должен быть слишком простым'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4',
               'placeholder': 'Введите имя пользователя',
               'title': 'username должен содержать только латиницу и не повторять уже существующие'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-4',
               'placeholder': 'Введите адрес эл. почты',
               'title': 'email должен иметь корректный формат'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4',
               'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4',
               'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4',
               'placeholder': 'Введите пароль',
               'title': 'Пароль должен быть длинее 8 символов и не должен быть слишком простым'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control py-4',
               'placeholder': 'Подтвердите пароль',
               'title': 'Пароль должен быть длинее 8 символов и не должен быть слишком простым'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-4',
               'readonly': True}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'image')
