from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
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
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Используем email как username
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            # Создаем объект гражданина
            citizen = Citizens.objects.create(
                surname=self.cleaned_data['surname'],
                name=self.cleaned_data['name'],
                patronymic=self.cleaned_data.get('patronymic', ''),
                tel=self.cleaned_data.get('tel', ''),
                email=self.cleaned_data['email'],
            )
            # Создаем объект пользователя
            Users.objects.create(user=user, id_citizen=citizen)

        return user


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