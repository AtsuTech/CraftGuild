from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import (
    TimeSlot, Schedule, Content, ReservationForm)


class TimeSlotAdmin(ModelAdmin):
    model = TimeSlot
    menu_label = '時間割の設定'  # ditch this to use verbose_name_plural from model
    menu_icon = 'time'  # change as required
    list_display = ('start_time', 'end_time')
    # list_filter = ('genre', 'author')
    # search_fields = ('title', 'author')


class ScheduleAdmin(ModelAdmin):
    model = Schedule
    menu_label = 'スケジュール設定'  # ditch this to use verbose_name_plural from model
    menu_icon = 'calendar'  # change as required
    # list_display = ('capacity')
    # list_filter = ('date')
    list_display = ('date', 'timeslot', 'capacity', 'available')  # Provide field names in a tuple or list
    list_filter = ('date', 'available')  #
    # search_fields = ('first_name', 'last_name')

class ContentAdmin(ModelAdmin):
    model = Content
    menu_label = 'コンテンツ設定'  # ditch this to use verbose_name_plural from model
    menu_icon = 'thumbtack'
    list_display = ('name', 'image')


class ReservationFormAdmin(ModelAdmin):
    model = ReservationForm
    menu_label = '予約フォーム'  # ditch this to use verbose_name_plural from model
    menu_icon = 'form'  # change as required
    list_display = ('child_name1','child_name2','parent_name1','parent_name2','email','phone_number','schedule','content','comment')
    list_filter = ('schedule','content')
    # search_fields = ('name',)


class TrialClassGroup(ModelAdminGroup):
    menu_label = '体験授業の管理'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (TimeSlotAdmin, ScheduleAdmin, ContentAdmin, ReservationFormAdmin)

# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(TrialClassGroup)