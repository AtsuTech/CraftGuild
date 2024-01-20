from django.urls import path, reverse

from wagtail.admin.menu import MenuItem
from wagtail import hooks

from .views import index



#from .models import SchoolSchedule



@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('calendar/', index, name='calendar'),
    ]


@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    return MenuItem('カレンダー', reverse('calendar'), icon_name='date')





