from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

# Create your models here.


class Particular(Page):

    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "particular.ParticularBlock",
    ]


    page_title = models.CharField( max_length=255, verbose_name="ページのタイトル")

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
    ]


#こだわりのブロック
class ParticularBlock(Page):

    #こだわりのタイトル
    particular_title = models.CharField( max_length=255, verbose_name="作成フローのタイトル(例:ミニミッションに挑戦!)")

    #カバー画像
    cover_image = models.ForeignKey( 
        "wagtailimages.Image", 
        verbose_name="カバー画像", 
        blank=True,
        null=True,
        related_name="+", 
        on_delete=models.SET_NULL,
    )

    #こだわりの詳細文
    description = models.TextField(
        blank=True,
        verbose_name="作成フローの詳細文",
    )

    #最後のブロックかの判定
    order_check = models.BooleanField(verbose_name="最後のブロックかどうかの確認",default=True )
        

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("particular_title"),
        FieldPanel("cover_image"),
        FieldPanel("description"),
        FieldPanel("order_check"),
    ]

