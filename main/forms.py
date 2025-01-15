from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import Citizens, Users

# Регистрация
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Электронная почта", required=True)
    surname = forms.CharField(max_length=255, label="Фамилия", required=True)
    name = forms.CharField(max_length=255, label="Имя", required=True)
    patronymic = forms.CharField(max_length=255, label="Отчество", required=False)
    tel = forms.CharField(max_length=255, label="Телефон", required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'surname', 'name', 'patronymic', 'tel']

    def save(self, commit=True):
        try:
            email = self.cleaned_data.get('email')
            user, created = User.objects.get_or_create(username=email, email=email)
            if not created:
                raise ValidationError("Пользователь с таким email уже существует.")
            if commit:
                user.set_password(self.cleaned_data.get('password2'))
                user.save()
                citizen = Citizens.objects.create(
                    surname=self.cleaned_data.get('surname'),
                    name=self.cleaned_data.get('name'),
                    patronymic=self.cleaned_data.get('patronymic', ''),
                    tel=self.cleaned_data.get('tel', ''),
                    email=self.cleaned_data.get('email'),
                )
                Users.objects.create(user=user, id_citizen=citizen)
            return user
        except IntegrityError as e:
            raise ValidationError(f"Ошибка при сохранении данных: {e}")


# Авторизация
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Email")

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            from django.contrib.auth import authenticate
            user = authenticate(username=username, password=password)
            if user is None:
               raise forms.ValidationError('Неверный email или пароль')
            self.user_cache = user
        return self.cleaned_data



class LogoutForm(forms.Form):
    pass  # Эта форма не содержит полей