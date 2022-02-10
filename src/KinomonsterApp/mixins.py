from django.views.generic import View
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseRedirect


class MyFormMixin(View):

    def dispatch(self, request, *args, **kwargs):
        #################### РЕАЛИЗУЕМ АВТОРИЗАЦИЮ: ####################
        if request.method == 'POST' and 'login' in request.POST:
            login_form = UserLoginForm(request.POST or None)
            if login_form.is_valid():
                cleaned_data = login_form.cleaned_data
                user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(self.request.path)
                    else:
                        messages.error(request, 'Данная учетная запись отключена! Обратитесь к администратору.')
                        return HttpResponseRedirect(self.request.path)
                else:
                    messages.error(request, 'Неверный логин или пароль! Повторите попытку.')
                    return HttpResponseRedirect(self.request.path)
        elif request.method == 'POST' and 'logout' in request.POST:
            auth.logout(request)
            return HttpResponseRedirect(self.request.path)
        else:
            self.login_form = UserLoginForm()
        ################################################################
        
        #################### РЕАЛИЗУЕМ РЕГИСТРАЦИЮ: ####################
        if request.method == 'POST' and 'register' in request.POST:
            register_form = UserRegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                username = register_form.cleaned_data.get('username')
                print(username)
                email = register_form.cleaned_data.get('email') ### Я ДОБАВИЛ
                print(email)    ### Я ДОБАВИЛ
                raw_password = register_form.cleaned_data.get('password1')
                print(raw_password)
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                print("АККАУНТ УСПЕШНО СОЗДАН!")
                return HttpResponseRedirect(self.request.path)
            else:
                print("ЧТО-ТО ПОШЛО НЕ ТАК!")
                messages.error(request, 'Ваши пароли не совпадают или Вы используете слишком простой пароль!')  # добавил ошибку несовпадения паролей при регистрации
                return HttpResponseRedirect(self.request.path)
        else:
            self.register_form = UserRegisterForm()
        ################################################################
        # print(F'request.path == {request.path}')
        return super().dispatch(request, *args, **kwargs)