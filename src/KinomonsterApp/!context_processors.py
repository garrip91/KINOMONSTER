from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages


def get_login_and_register_data(request):
    
    if request.method == 'POST' and 'login' in request.POST:  # Здесь отлавливаем post запрос,
        # если нажали кнопу с name=login, понимаем,
        # что авторизация, авторизуем пользователя
        login_form = UserLoginForm(request.POST or None)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data # бывш. cd1
            # un1 = cleaned_data.get('username') # бывш. un
            # qs = User.objects.filter(username=un1)
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, 'Отключенная учетная запись! Обратитесь к администратору')  # добавил ошибку отключенной УЗ
            else:
                messages.error(request, 'Неверный логин или пароль. Повторите попытку')  # добавил ошибку неверного пароля
    elif request.method == 'POST' and 'logout' in request.POST:  # если в нажали кнопку с name=logout,
        # разлогиниваем пользователя
        auth.logout(request)
        return HttpResponseRedirect('/')
    else:
        login_form = UserLoginForm()
    #################### РЕАЛИЗУЕМ РЕГИСТРАЦИЮ: ####################
    if request.method == 'POST' and 'register' in request.POST:
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            # После того, как мы сохранили пользователя, создаем две переменных.
            username = register_form.cleaned_data.get('username')  # забираем наше имя пользователя из формы
            #print(username)
            raw_password = register_form.cleaned_data.get('password1')  # забираем наш пароль пользователя из формы
            #print(raw_password)
            user = authenticate(username=username, password=raw_password)  # производим аутентификацию
            login(request, user)
            #print("АККАУНТ УСПЕШНО СОЗДАН!")
            return HttpResponseRedirect('/') # так же перенаправляем его на главную страницу, но уже залогиненным
        else:
            #print("ЧТО-ТО ПОШЛО НЕ ТАК!")
            messages.error(request, 'Ваши пароли не совпадают или Вы используете слишком простой пароль!')  # добавил ошибку несовпадения паролей при регистрации
    else:
        register_form = UserRegisterForm()
    return {
        'login_form': login_form,
        'register_form': register_form,
    }