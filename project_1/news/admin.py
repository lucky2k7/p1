from django.contrib import admin
from news.models import News

class admin_news(admin.ModelAdmin):
    list_display = ('news_tital','news_desc')

# Register your models here.

admin.site.register(News, admin_news)
