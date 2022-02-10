# from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import Film, Series, FilmComments, SeriesComments

from django.views.generic import View

from django.views.generic import View, TemplateView, DetailView, ListView

from django.db.models import Q

################################################################
from django.views.generic import CreateView

from .forms import SearchForm, UserLoginForm, UserRegisterForm, FilmCommentForm, SeriesCommentForm, SendMessageForm

from django.views.generic.edit import FormView
from django.contrib import auth
from django.contrib import messages  # импортировал новый модуль messages
from django.contrib.auth.models import User
#
#
from django.contrib.auth import authenticate, login, logout
#
#
from django.shortcuts import redirect
#
#
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
#
#
from django import forms
#
#
from django.core.exceptions import ValidationError
#
#
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
#
#
from django.urls import reverse
#
#
from .mixins import MyFormMixin
#
#
from django.views.generic.edit import FormView
#
#
from django.core.mail import send_mail
#
#
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here:
class HomePageView(MyFormMixin, View):

    def get(self, request, *args, **kwargs):
        films = Film.objects.all()
        series = Series.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'KinomonsterApp/home.html',
            {
                'films': films,
                'series': series,
                'login_form': self.login_form,
                'register_form': self.register_form,
            }
        )
        
        
class SearchResultsView(MyFormMixin, ListView):

    model = Film
    context_object_name = 'object_list'
    template_name = 'KinomonsterApp/search_results.html'
    
    def get_queryset(self):
        search_query = self.request.GET.get('q')
        print(F'1. {search_query}')
        object_list = Film.objects.filter(
            Q(title__icontains=search_query) | Q(year__icontains=search_query) | Q(rating__icontains=search_query) | Q(producer__icontains=search_query) | Q(description__icontains=search_query)
        )
        if Film.objects.filter(title__icontains=search_query).exists():
            print(F'1.1. {object_list}')
        else:
            print("Фильма(-ов) с таким ***[ НАЗВАНИЕМ ]*** нет!")
        if Film.objects.filter(year__icontains=search_query).exists():
            print(F'1.2. {object_list}')
        else:
            print("Фильма(-ов) с таким ***[ ГОДОМ ]*** нет!")
        if Film.objects.filter(rating__icontains=search_query).exists():
            print(F'1.3. {object_list}')
        else:
            print("Фильма(-ов) с таким ***[ РЕЙТИНГОМ ]*** нет!")
        if Film.objects.filter(producer__icontains=search_query).exists():
            print(F'1.4. {object_list}')
        else:
            print("Фильма(-ов) с таким ***[ РЕЖИССЁРОМ ]*** нет!")
        if Film.objects.filter(description__icontains=search_query).exists():
            print(F'1.5. {object_list}')
        else:
            print("Фильма(-ов) с таким ***[ ОПИСАНИЕМ ]*** нет!")
        print(F'request.path == {self.request.path}')
        return object_list
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q')
        print(F'2. {search_query}')
        context['series'] = Series.objects.filter(
            Q(title__icontains=search_query) | Q(year__icontains=search_query) | Q(rating__icontains=search_query) | Q(producer__icontains=search_query) | Q(description__icontains=search_query)
        )
        context['search_query'] = search_query
        if Series.objects.filter(title__icontains=search_query).exists():
            print(F"2.1. {context['series']}")
        else:
            print("Сериала(-ов) с таким ***[ НАЗВАНИЕМ ]*** нет!")
        if Series.objects.filter(year__icontains=search_query).exists():
            print(F"2.2. {context['series']}")
        else:
            print("Сериала(-ов) с таким ***[ ГОДОМ ]*** нет!")
        if Series.objects.filter(rating__icontains=search_query).exists():
            print(F"2.3. {context['series']}")
        else:
            print("Сериала(-ов) с таким ***[ РЕЙТИНГОМ ]*** нет!")
        if Series.objects.filter(producer__icontains=search_query).exists():
            print(F"2.4. {context['series']}")
        else:
            print("Сериала(-ов) с таким ***[ РЕЖИССЁРОМ ]*** нет!")
        if Series.objects.filter(description__icontains=search_query).exists():
            print(F"2.5. {context['series']}")
        else:
            print("Сериала(-ов) с таким ***[ ОПИСАНИЕМ ]*** нет!")
        print(F'request.path == {self.request.path}')
        context['login_form'] = self.login_form
        context['register_form'] = self.register_form
        return context
    
        
class FilmsTemplateView(MyFormMixin, TemplateView):

    template_name = 'KinomonsterApp/films.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        context['series'] = Series.objects.all()
        context['login_form'] = self.login_form
        context['register_form'] = self.register_form
        print(F'request.path == {self.request.path}')
        return context
    
        
class FilmDetailView(MyFormMixin, FormMixin, DetailView): # Добавил FormMixin, это представление формы https://docs.djangoproject.com/en/3.2/ref/class-based-views/mixins-editing/

    model = Film
    template_name = 'KinomonsterApp/film_detail.html'
    form_class = FilmCommentForm  # определил форму
    
    def get_success_url(self):  # если коммент успешно отправился на сервер, перенаправляем на эту же страницу
        return reverse('film_detail_url', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        context['series'] = Series.objects.all()
        context['comments'] = FilmComments.objects.all()
        context['form'] = FilmCommentForm()  # добавил форму в контекст
        context['login_form'] = self.login_form
        context['register_form'] = self.register_form
        print(F'request.path == {self.request.path}')
        return context
        
    def post(self, request, *args, **kwargs): # функция поста коммента
        self.object = self.get_object()  # определили объект
        form = self.get_form()  # забираем форму
        if form.is_valid():  # выполняем проверку формы
            print(form)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
            
    def form_valid(self, form):  # здесь мы задаем нашу форму
        instance = form.save(commit=False)  # определяем объект модели, чтобы сохранить наши параметры
        instance.author = self.request.user  # сохраняем автора, для передачи в шаблон
        instance.film = Film.objects.get(pk=self.object.pk)  # получаем id нашего фильма
        instance.save()  # сохраняем форму
        return super(FilmDetailView, self).form_valid(form)
        
        
class SeriesTemplateView(MyFormMixin, TemplateView):

    template_name = 'KinomonsterApp/series.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        context['series'] = Series.objects.all()
        context['login_form'] = self.login_form
        context['register_form'] = self.register_form
        print(F'request.path == {self.request.path}')
        return context
    
        
class SeriesDetailView(MyFormMixin, FormMixin, DetailView): # Добавил FormMixin, это представление формы https://docs.djangoproject.com/en/3.2/ref/class-based-views/mixins-editing/

    model = Series
    template_name = 'KinomonsterApp/series_detail.html'
    form_class = SeriesCommentForm  # определил форму
    
    def get_success_url(self):  # если коммент успешно отправился на сервер, перенаправляем на эту же страницу
        return reverse('series_detail_url', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(SeriesDetailView, self).get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        context['series'] = Series.objects.all()
        context['comments'] = SeriesComments.objects.all()
        context['form'] = SeriesCommentForm()  # добавил форму в контекст
        context['login_form'] = self.login_form
        context['register_form'] = self.register_form
        print(F'request.path == {self.request.path}')
        return context
        
    def post(self, request, *args, **kwargs): # функция поста коммента
        self.object = self.get_object()  # определили объект
        form = self.get_form()  # забираем форму
        if form.is_valid():  # выполняем проверку формы
            print(form)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
            
    def form_valid(self, form):  # здесь мы задаем нашу форму
        instance = form.save(commit=False)  # определяем объект модели, чтобы сохранить наши параметры
        instance.author = self.request.user  # сохраняем автора, для передачи в шаблон
        instance.series = Series.objects.get(pk=self.object.pk)  # получаем id нашего сериала
        instance.save()  # сохраняем форму
        return super(SeriesDetailView, self).form_valid(form)
        
        
class FilmsRatingTemplateView(MyFormMixin, TemplateView):

    template_name = 'KinomonsterApp/films_rating.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        context['series'] = Series.objects.all()
        context['login_form'] = self.login_form
        context['register_form'] = self.register_form
        print(F'request.path == {self.request.path}')
        return context
        
        
class SeriesRatingTemplateView(MyFormMixin, TemplateView):

    template_name = 'KinomonsterApp/series_rating.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        context['series'] = Series.objects.all()
        context['login_form'] = self.login_form
        context['register_form'] = self.register_form
        print(F'request.path == {self.request.path}')
        return context
    
    
class ContactsTemplateView(MyFormMixin, TemplateView):

    template_name = 'KinomonsterApp/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        context['series'] = Series.objects.all()
        context['login_form'] = self.login_form
        context['register_form'] = self.register_form
        print(F'request.path == {self.request.path}')
        return context


################################################################
class SendMessageView(MyFormMixin, SuccessMessageMixin, FormView):
    
    template_name = 'KinomonsterApp/contacts.html'
    form_class = SendMessageForm
    success_url = '/contacts/' # При успешной отправке формы, перенаправляет на contacts_test
    success_message = "Ваше письмо успешно отправлено!"
        
    def form_valid(self, form): # проверяем форму на валидность
        instance = form.save(commit=False) # определяем объект модели, чтобы сохранить наши параметры
        instance.author = self.request.user # сохраняем автора, для передачи в шаблон
        # Для того, чтобы добавить какое-то из полей формы в бд автоматически
        # тут нужно прописать к примеру instance.email = email юзера из бд и убрать это поле из templates и из формы
        #instance.email = self.request.user.email
        instance.email = form.cleaned_data['email']
        instance.title = form.cleaned_data['title']
        instance.text = form.cleaned_data['text']
        print(instance.email, instance.title, instance.text)
        instance.save() # сохраняем форму...
        try:
            send_mail(F'{instance.title} от ***[[ {instance.email} ]]*** из учебного проекта', instance.text, 'garrip91@yandex.ru', ['garrip91@yandex.ru'], fail_silently=False)
            return super(SendMessageView, self).form_valid(form)
        except:
            return HttpResponseNotFound('<h1>Письмо не отправлено</h1>')
        
    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['email'] = self.request.user.email
            print(initial['email'])
        return initial
        
    def get_context_data(self, **kwargs):
        context = super(SendMessageView, self).get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        context['series'] = Series.objects.all()
        context['login_form'] = self.login_form
        context['register_form'] = self.register_form
        print(F'request.path == {self.request.path}')
        return context
################################################################