from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

# Create your models here.

class CreationFlow(Page):


    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "creation_flow.CreationFlowBlock",
    ]


    page_title = models.CharField( max_length=255, verbose_name="ページのタイトル")

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
    ]


class CreationFlowBlock(Page):

    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "creation_flow.CreationFlowItem",
    ]

    flow_title = models.CharField( max_length=255, verbose_name="作成フローのタイトル(例:ミニミッションに挑戦!)")
    sub_title = models.CharField( max_length=255, verbose_name="サブタイトル(例:導入の20分)")
    order_check = models.BooleanField(verbose_name="最後のブロックかどうかの確認",default=True )
        

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("flow_title"),
        FieldPanel("sub_title"),
        FieldPanel("order_check"),
    ]


class CreationFlowItem(Page):

    flow_item = models.CharField( max_length=255, verbose_name="作成フロー項目名")

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
        verbose_name="作成フローの詳細文",
    )

        
    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("flow_item"),
        FieldPanel("cover_image"),
        FieldPanel("description"),
    ]
