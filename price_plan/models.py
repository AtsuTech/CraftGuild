from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

# Create your models here.

class PricePlan(Page):

    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "price_plan.PricePlanBlock",
    ]


    page_title = models.CharField( max_length=255, verbose_name="ページのタイトル")

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
    ]


#料金ブロック
class PricePlanBlock(Page):

    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "price_plan.PricePlanItem",
    ]

    plan_title = models.CharField( max_length=255, verbose_name="作成フローのタイトル(例:ミニミッションに挑戦!)")        

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("plan_title"),
    ]


#料金アイテム
class PricePlanItem(Page):

    plan_item = models.CharField( max_length=255, verbose_name="作成フロー項目名")

    cover_image = models.ForeignKey( 
        "wagtailimages.Image", 
        verbose_name="カバー画像", 
        blank=True,
        null=True,
        related_name="+", 
        on_delete=models.SET_NULL,
    )

    price1 = models.CharField( max_length=255, verbose_name="料金(税込)")

    price2 = models.CharField( max_length=255, verbose_name="料金(税込)/(時間)")

        
    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("plan_item"),
        FieldPanel("cover_image"),
        FieldPanel("price1"),
        FieldPanel("price2"),
    ]

#料金の説明文(枠外)
class PriceDescription(Page):

    description = models.TextField(
        blank=True,
        verbose_name="作成フローの詳細文",
    )

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]