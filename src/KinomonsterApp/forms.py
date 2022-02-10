from django import forms

from KinomonsterApp.models import Film, Series, FilmComments, SeriesComments, SendMessage

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django.core.mail import send_mail


class SearchForm(forms.Form):
    
    search = forms.CharField(label='Введите ключевое(-ые) слово(-а) для поиска')
    
    
################################################################


Person = get_user_model()

class UserLoginForm(forms.Form):
    
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Логин'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Пароль'}))


class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Придумайте логин'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Укажите почту'}))  ### Я ДОБАВИЛ
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Придумайте пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Повторите пароль'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class FilmCommentForm(forms.ModelForm):  # добавил форму коммента
    
    class Meta:
        model = FilmComments  # добавил модель FilmComments
        fields = ['title', 'comment']  # значение, которое будет отображаться в форме
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Заголовок отзыва'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв'}),
        }        
        
class SeriesCommentForm(forms.ModelForm):  # добавил форму коммента
    
    class Meta:
        model = SeriesComments  # добавил модель FilmComments
        fields = ['title', 'comment']  # значение, которое будет отображаться в форме
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Заголовок отзыва'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв'}),
        }
        
        
class SendMessageForm(forms.ModelForm):
    
    class Meta:
        model = SendMessage
        fields = ['email', 'title', 'text'] # удалил поле автора, потому что мы его подтягиваем от зарегистрированного пользователя
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Почтовый адрес автора текста'}),
            'title': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Заголовок текста'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '9', 'placeholder': 'Текст'}),
        }