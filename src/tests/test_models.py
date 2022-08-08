from django.test import TestCase

from KinomonsterApp.models import Film


class FilmModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Настраиваем немодифицированные объекты, используемые всеми методами тестирования:
        Film.objects.create(title='ЗАГОЛОВОК ДЛЯ ТЕСТА', logo='images/ДЛЯ_ТЕСТА.png', youtube_trailer_url='https://www.youtube.com/watch?v=FquXN0t_KbU', year='2022', rating='666666', producer='РЕЖИССЁР ДЛЯ ТЕСТА', description='ОПИСАНИЕ ДЛЯ ТЕСТА')

    def test_title_label(self):
        film = Film.objects.get(id=1)
        field_label = film._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название фильма')

    def test_logo_label(self):
        film = Film.objects.get(id=1)
        field_label = film._meta.get_field('logo').verbose_name
        self.assertEquals(field_label, 'Логотип фильма')

    def test_youtube_trailer_url_max_length(self):
        film = Film.objects.get(id=1)
        max_length = film._meta.get_field('youtube_trailer_url').max_length
        self.assertEquals(max_length, 200)

    def test_ABC_DEF_1(self):
        pass

    def test_ABC_DEF_2(self):
        pass

    def test_ABC_DEF_3(self):
        pass

    def test_get_absolute_url(self):
        film = Film.objects.get(id=1)
        self.assertEquals(film.get_absolute_url(), '/catalog/author/1')