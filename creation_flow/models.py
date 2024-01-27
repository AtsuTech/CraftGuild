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

    #ページのタイトル"
    page_title = models.CharField( max_length=255, verbose_name="ページのタイトル(作成の流れ)")

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

    #タイトル
    flow_title = models.CharField( max_length=255, verbose_name="作成フローのタイトル(例:ミニミッションに挑戦!)")

    #サブタイトル1行目
    sub_title1 = models.CharField( max_length=255,default="", verbose_name="サブタイトル1行目(例:導入の)")

    #サブタイトル2行目
    sub_title2 = models.CharField( max_length=255,default="", verbose_name="サブタイトル2行目(例:導入の20分)")

    #サブタイトルの背景色
    sub_title_color = models.CharField( 
        max_length=255, 
        verbose_name="サブタイトルの背景カラー",
        default="#BDE3FF",
        choices=[
            ('#BDE3FF', 'スカイブルー'),
            ('#FCD19C', 'オレンジ'),
            ('#FCC7C2', 'ピンク'),
            ('#99FF99', 'グリーン'),
            ('#C299FF', 'パープル'),
            ('#FFFF99', 'イエロー'),
            ('#FFFFFF', 'ホワイト'),
            ('#CCCCCC', 'グレー'),
        ]
    )

    #最後のブロックかの判定
    order_check = models.BooleanField(verbose_name="最後のブロックかどうかの確認",default=True )
        

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("flow_title"),
        FieldPanel("sub_title1"),
        FieldPanel("sub_title2"),
        FieldPanel("sub_title_color"),
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
