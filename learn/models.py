from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

# Create your models here.


class LaenItemList(Page):

    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "learn.LeanItem",
    ]


    page_title = models.CharField( max_length=255, verbose_name="ページのタイトル")

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
    ]



class LeanItem(Page):

    item = models.CharField( max_length=255, verbose_name="学べるスキル(例:観察する力)")

    cover_image = models.ForeignKey( 
        "wagtailimages.Image", 
        verbose_name="カバー画像", 
        blank=True,
        null=True,
        related_name="+", 
        on_delete=models.SET_NULL,
    )

    description = models.TextField(
        blank=True,
        verbose_name="学べるスキルの詳細文",
    )

        
    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("item"),
        FieldPanel("cover_image"),
        FieldPanel("description"),
    ]