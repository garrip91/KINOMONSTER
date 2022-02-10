from django.contrib import admin

from KinomonsterApp.models import Film, Series, FilmComments, SeriesComments, SendMessage


class FilmCommentsAdmin(admin.ModelAdmin):
    # class Meta:
        # model = FilmComments
        
    # list_display = ('author', 'comment', 'film')
    # list_editable = ('travel_time',)
    
    def get_short_comment(self, obj):
        return F'{obj.comment[:100]}...'
    get_short_comment.short_description = 'comment'
    
    list_display = ('author', 'title', 'get_short_comment', 'film')
    # list_display = ('author', 'film')
    
    
class SeriesCommentsAdmin(admin.ModelAdmin):
    # class Meta:
        # model = FilmComments
        
    # list_display = ('author', 'comment', 'film')
    # list_editable = ('travel_time',)
    
    def get_short_comment(self, obj):
        return F'{obj.comment[:100]}...'
    get_short_comment.short_description = 'comment'
    
    list_display = ('author', 'title', 'get_short_comment', 'series')


# Register your models here:
admin.site.register(Film)
admin.site.register(Series)
admin.site.register(FilmComments, FilmCommentsAdmin)
admin.site.register(SeriesComments, SeriesCommentsAdmin)
admin.site.register(SendMessage)