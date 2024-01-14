from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import (ContactCategory,ContactForm)

class ContactCategoryAdmin(ModelAdmin):
    model = ContactCategory
    menu_label = '内容のカテゴリ設定' 
    menu_icon = 'mail'
    # list_display = ('option')
    # list_filter = ('option')
    # search_fields = ('option')

class ContactFormAdmin(ModelAdmin):
    model = ContactForm
    menu_label = 'フォーム'  # ditch this to use verbose_name_plural from model
    menu_icon = 'mail'  # change as required
    # menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    # add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    # exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    # add_to_admin_menu = True  # or False to exclude your model from the menu


class LibraryGroup(ModelAdminGroup):
    menu_label = 'お問い合わせ'
    menu_icon = 'mail'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ContactCategoryAdmin,ContactFormAdmin)

modeladmin_register(LibraryGroup)