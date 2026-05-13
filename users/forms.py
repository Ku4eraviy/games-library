from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
import re

from .models import CustomUser


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        label='Полное имя',
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Иванов Иван Иванович',
            'class': 'w-full bg-neutral-800 border border-neutral-700 rounded-lg px-4 py-2.5 text-white placeholder-neutral-500 focus:outline-none focus:border-violet-500 transition'
        })
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=16,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '8(999)123-45-67',
            'class': 'w-full bg-neutral-800 border border-neutral-700 rounded-lg px-4 py-2.5 text-white placeholder-neutral-500 focus:outline-none focus:border-violet-500 transition'
        })
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@mail.ru',
            'class': 'w-full bg-neutral-800 border border-neutral-700 rounded-lg px-4 py-2.5 text-white placeholder-neutral-500 focus:outline-none focus:border-violet-500 transition'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'phone', 'email', 'password1', 'password2']
        labels = {'username': 'Логин'}
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Введите логин',
                'class': 'w-full bg-neutral-800 border border-neutral-700 rounded-lg px-4 py-2.5 text-white placeholder-neutral-500 focus:outline-none focus:border-violet-500 transition'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pw_class = 'w-full bg-neutral-800 border border-neutral-700 rounded-lg px-4 py-2.5 text-white placeholder-neutral-500 focus:outline-none focus:border-violet-500 transition'
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].widget.attrs.update({'class': pw_class, 'placeholder': 'Минимум 8 символов'})
        self.fields['password2'].label = 'Повтор пароля'
        self.fields['password2'].widget.attrs.update({'class': pw_class, 'placeholder': 'Повторите пароль'})

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.fullmatch(r'[A-Za-z0-9]+', username):
            raise ValidationError('Логин должен содержать только латинские буквы и цифры')
        if len(username) < 4:
            raise ValidationError('Логин должен быть не короче 4 символов')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким логином уже существует')
        return username

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not re.fullmatch(r'8\(\d{3}\)\d{3}-\d{2}-\d{2}', phone):
            raise ValidationError('Телефон должен быть в формате 8(XXX)XXX-XX-XX')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким email уже существует')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data.get('full_name', '')
        user.email = self.cleaned_data.get('email', '')
        user.phone = self.cleaned_data.get('phone', '')
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ваш логин',
            'class': 'w-full bg-neutral-800 border border-neutral-700 rounded-lg px-4 py-2.5 text-white placeholder-neutral-500 focus:outline-none focus:border-violet-500 transition'
        })
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Ваш пароль',
            'class': 'w-full bg-neutral-800 border border-neutral-700 rounded-lg px-4 py-2.5 text-white placeholder-neutral-500 focus:outline-none focus:border-violet-500 transition'
        })
    )

    error_messages = {
        'invalid_login': 'Неверный логин или пароль',
        'inactive': 'Учётная запись отключена',
    }
