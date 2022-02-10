def get_login_and_register_data():
    
    if request.method == 'POST' and 'login' in request.POST:  # Здесь отлавливаем post запрос,
        # если нажали кнопу с name=login, понимаем,
        # что авторизация, авторизуем пользователя
        login_form = UserLoginForm(request.POST or None)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data # бывш. cd1
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return messages.error(request, 'Отключенная учетная запись! Обратитесь к администратору')  # добавил ошибку отключенной УЗ # ДОБАВЛЕН return
            else:
                return messages.error(request, 'Неверный логин или пароль. Повторите попытку')  # добавил ошибку неверного пароля # ДОБАВЛЕН return
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
            print(username)
            raw_password = register_form.cleaned_data.get('password1')  # забираем наш пароль пользователя из формы
            print(raw_password)
            user = authenticate(username=username, password=raw_password)  # производим аутентификацию
            login(request, user)
            print("АККАУНТ УСПЕШНО СОЗДАН!")
            return HttpResponseRedirect('/') # так же перенаправляем его на главную страницу, но уже залогиненным
        else:
            print("ЧТО-ТО ПОШЛО НЕ ТАК!")
            return messages.error(request, 'Ваши пароли не совпадают или Вы используете слишком простой пароль!')  # добавил ошибку несовпадения паролей при регистрации # ДОБАВЛЕН return
    else:
        register_form = UserRegisterForm()