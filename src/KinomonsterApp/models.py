from django.db import models

# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from django.utils import timezone
'''
(<ManyToOneRel: admin.logentry>, <OneToOneRel: KinomonsterApp.user>,
 1. <django.db.models.fields.AutoField: id>,
 2. <django.db.models.fields.CharField: password>,
 3. <django.db.models.fields.DateTimeField: last_login>,
 4. <django.db.models.fields.BooleanField: is_superuser>,
 5. <django.db.models.fields.CharField: username>,
 6. <django.db.models.fields.CharField: first_name>,
 7. <django.db.models.fields.CharField: last_name>,
 8. <django.db.models.fields.EmailField: email>,
 9. <django.db.models.fields.BooleanField: is_staff>,
10. <django.db.models.fields.BooleanField: is_active>,
11. <django.db.models.fields.DateTimeField: date_joined>,
12. <django.db.models.fields.related.ManyToManyField: groups>,
13. <django.db.models.fields.related.ManyToManyField: user_permissions>)
'''


# Create your models here:
class Film(models.Model):
    
    title = models.CharField(max_length=50, unique=True, verbose_name='Название фильма')
    logo = models.ImageField(upload_to='images', verbose_name='Логотип фильма')
    youtube_trailer_url = models.URLField(max_length=200, unique=True, verbose_name='Ссылка на трейлер фильма в YouTube')
    year = models.PositiveIntegerField(verbose_name='Год выхода фильма')
    rating = models.FloatField(verbose_name='Рейтинг фильма')
    producer = models.CharField(max_length=5000, verbose_name='Режиссёр(-ы) фильма')
    description = models.TextField(verbose_name='Описание фильма')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['title']
                      

class Series(models.Model):
    
    title = models.CharField(max_length=50, unique=True, verbose_name='Название сериала')
    logo = models.ImageField(upload_to='images', verbose_name='Логотип сериала')
    youtube_trailer_url = models.URLField(max_length=200, unique=True, verbose_name='Ссылка на трейлер сериала в YouTube')
    year = models.PositiveIntegerField(verbose_name='Год выхода сериала')
    rating = models.FloatField(verbose_name='Рейтинг сериала')
    producer = models.CharField(max_length=5000, verbose_name='Режиссёр(-ы) сериала')
    description = models.TextField(verbose_name='Описание сериала')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"
        ordering = ['title']
        
        
class FilmComments(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True) # добавил null=True, чтобы значение даже если пустое, записывалось в бд
    title = models.CharField(max_length=5000, verbose_name='Заголовок комментария')
    comment = models.TextField(verbose_name='Комментарий')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Фильм', null=True) # добавил null=True, чтобы значение даже если пустое, записывалось в бд
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now) # добавил поле времени регистрации поста
    
    def __str__(self):
        return str(self.author)
    
    class Meta:
        verbose_name = "Комментарий к фильму"
        verbose_name_plural = "Комментарии к фильмам"
        ordering = ['author']
        
        
class SeriesComments(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True) # добавил null=True, чтобы значение даже если пустое, записывалось в бд
    title = models.CharField(max_length=5000, verbose_name='Заголовок комментария')
    comment = models.TextField(verbose_name='Комментарий')
    series = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name='Сериал', null=True) # добавил null=True, чтобы значение даже если пустое, записывалось в бд
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now) # добавил поле времени регистрации поста
    
    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name = "Комментарий к сериалу"
        verbose_name_plural = "Комментарии к сериалам"
        ordering = ['author']
        
        
class SendMessage(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор текста', null=True)
    email = models.EmailField(blank=True, null=True, verbose_name='Почтовый адрес автора текста')
    title = models.CharField(max_length=5000, verbose_name='Заголовок текста', null=True)
    text = models.TextField(verbose_name='Текст')
    
    def __str__(self):
        return str(self.title)
        
    class Meta:
        verbose_name = "Отправленное сообщение"
        verbose_name_plural = "Отправленные сообщения"
        ordering = ['title']