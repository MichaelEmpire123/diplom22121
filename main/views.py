
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
# Create your views here.

def home(req):
    return render(req, 'main/index.html')


# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после регистрации
    else:
        form = UserRegistrationForm()

    return render(request, 'auth/register.html', {'form': form})