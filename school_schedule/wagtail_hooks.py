from django.urls import path, reverse

from wagtail.admin.menu import MenuItem
from wagtail import hooks
from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from .views import index,timeslot_admin,edit_timeslot_view



#from .models import SchoolSchedule



@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('timeslot/',timeslot_admin, name='timeslot'),
        path('timeslot/edit/view/',edit_timeslot_view,name='timeslot_edit_view'),
        path('calendar/', index, name='calendar'),
    ]


@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    #return MenuItem('カレンダー', reverse('calendar'), icon_name='date')


    submenu = Menu(items=[
        MenuItem('時間割', reverse('timeslot'), icon_name='date'),
        MenuItem('カレンダー', reverse('calendar'), icon_name='date'),
        
    ])

    return SubmenuMenuItem('スケジュール', submenu, icon_name='date')


