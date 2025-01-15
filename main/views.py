
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Импортируем messages framework
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Users, Citizens, Employees
def home(req):
    return render(req, 'main/index.html')


# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно! Теперь вы можете войти в систему.') # сообщение об успехе
            return redirect('login')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.') # сообщение об ошибке

    else:
        form = UserRegistrationForm()

    return render(request, 'auth/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на главную после входа
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


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