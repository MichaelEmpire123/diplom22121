


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Citizens, Users

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

        # Проверка на существующий email
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")

        user.username = self.cleaned_data['email']  # Используем email как username
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            # Создаём объект жителя для нового пользователя
            citizen = Citizens.objects.create(
                surname=self.cleaned_data['surname'],
                name=self.cleaned_data['name'],
                patronymic=self.cleaned_data.get('patronymic', ''),
                tel=self.cleaned_data.get('tel', ''),
                email=self.cleaned_data['email'],
            )

            # Создаём запись в модели Users
            Users.objects.create(user=user, id_citizen=citizen)
        return user

