from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import Profile

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width: 100%; margin-bottom: 20px; padding: 10px; padding-left:20px; border-radius: 30px;',
            'placeholder': 'Логин'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'width: 100%; margin-bottom: 20px; padding: 10px; padding-left:20px; border-radius: 30px;',
            'placeholder': 'Пароль'
        })
    )

class LoginUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width:60%; margin-left:185px; margin-bottom:20px; margin-top:-70px padding-left:20px; border-radius: 30px;',
            'placeholder': 'Логин'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'width:60%; margin-left:185px; margin-bottom:20px padding-left:20px; border-radius: 30px;',
            'placeholder': 'Пароль'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width: 100%; margin-bottom: 20px; padding: 10px; padding-left:20px; border-radius: 30px;',
            'placeholder': 'Логин'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'width: 100%; margin-bottom: 20px; padding: 10px; padding-left:20px; border-radius: 30px;',
            'placeholder': 'Пароль'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'width: 100%; margin-bottom: 20px; padding: 10px; padding-left:20px; border-radius: 30px;',
            'placeholder': 'Повторите пароль'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; margin-bottom: 20px; padding: 10px; padding-left:20px; border-radius: 30px;',
                'placeholder': 'E-mail'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; margin-bottom: 20px; padding: 10px; padding-left:20px; border-radius: 30px;',
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; margin-bottom: 20px; padding: 10px; padding-left:20px; border-radius: 30px;',
                'placeholder': 'Фамилия'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class ProfileUserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width:60%; margin-left:185px; margin-bottom:-20px; margin-top:-70px',
            'placeholder': 'Имя'
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width:60%; margin-left:185px; margin-bottom:-20px',
            'placeholder': 'Фамилия'
        })
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'style': 'width:60%; margin-left:185px; margin-bottom:-20px; height: 150px;',
            'placeholder': 'Информация о себе'
        }),
        required=False
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'style': 'width:60%; margin-left:185px; margin-bottom:-20px',
            'type': 'date',
            'placeholder': 'Дата рождения'
        }),
        required=False
    )
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'style': 'width:60%; margin-left:185px; margin-bottom:-20px',
            'placeholder': 'Загрузите аватар'
        }),
        required=False
    )
    background_color = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width:60%; margin-left:185px; margin-bottom:-20px',
            'type': 'color',
            'placeholder': 'Цвет фона'
        })
    )

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar', 'bio', 'birth_date', 'background_color']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
