from django.core.exceptions import ValidationError

from .forms import UserRegistrationForm, EmailAuthenticationForm, LogoutForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Импортируем messages framework
from django.contrib.auth import login, logout
from .models import Users, Citizens, Employees
def home(req):
    return render(req, 'main/index.html')


# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Регистрация прошла успешно! Теперь вы можете войти в систему.')
                return redirect('login')
        except ValidationError as e:
             form.add_error(None, e)

    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


# Авторизация
def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


# Профиль пользователя
@login_required
def profile(request):
    user_profile = get_object_or_404(Users, user=request.user)
    citizen = None
    employee = None

    if user_profile.id_citizen:
        citizen = get_object_or_404(Citizens, id_citizen=user_profile.id_citizen.id_citizen)
    elif user_profile.id_sotrudnik:
        employee = get_object_or_404(Employees, id_sotrudnik=user_profile.id_sotrudnik.id_sotrudnik)

    context = {
        'user_profile': user_profile,
        'citizen': citizen,
        'employee': employee,
    }
    return render(request, 'auth/profile.html', context)

@login_required
def change_profile(request):
    return render(request, 'auth/change_data_profile.html')


# Выход
def logout_view(request):
    if request.method == 'POST':
        form = LogoutForm(request.POST)
        if form.is_valid():
            logout(request)
            return redirect('/') # Перенаправление на главную страницу после выхода
    else:
        form = LogoutForm()
    return render(request, 'auth/logout.html', {'form': form})