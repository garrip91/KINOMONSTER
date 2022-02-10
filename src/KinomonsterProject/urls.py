"""KinomonsterProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from KinomonsterApp.views import HomePageView, FilmsTemplateView, FilmDetailView, SeriesTemplateView, SeriesDetailView, FilmsRatingTemplateView, SeriesRatingTemplateView, ContactsTemplateView, SearchResultsView, SendMessageView


from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('films/', FilmsTemplateView.as_view(), name='films'),
    path('film/<int:pk>/', FilmDetailView.as_view(), name='film_detail_url'),
    path('series/', SeriesTemplateView.as_view(), name='series'),
    path('series/<int:pk>/', SeriesDetailView.as_view(), name='series_detail_url'),
    path('films_rating/', FilmsRatingTemplateView.as_view(), name='films_rating'),
    path('series_rating/', SeriesRatingTemplateView.as_view(), name='series_rating'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('contacts/', SendMessageView.as_view(), name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
