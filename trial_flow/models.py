from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class TrialFlow(Page):

    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "trial_flow.TrialFlowBlock",
    ]


    page_title = models.CharField( max_length=255, verbose_name="ページのタイトル")

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
    ]


#体験の流れのブロック
class TrialFlowBlock(Page):

    #体験の流れのタイトル
    flow_title = models.CharField( max_length=255, verbose_name="体験の流れのタイトルのタイトル(例:体験授業60分)")

    #サブタイトル
    sub_title = RichTextField(
        verbose_name="サブタイトル(例:STEP1)",
        blank=True,
        null=True,
    )

    #サブタイトルの背景色
    sub_title_color = models.CharField( 
        max_length=255, 
        verbose_name="サブタイトルの背景カラー",
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

    #カバー画像
    cover_image = models.ForeignKey( 
        "wagtailimages.Image", 
        verbose_name="カバー画像", 
        blank=True,
        null=True,
        related_name="+", 
        on_delete=models.SET_NULL,
    )

    #体験の流れの詳細文
    description = RichTextField(
        blank=True,
        null=True,
        verbose_name="体験の流れの詳細文",
    )

    #最後のブロックかの判定
    order_check = models.BooleanField(verbose_name="最後のブロックかどうかの確認",default=True )
        

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("flow_title"),
        FieldPanel("sub_title"),
        FieldPanel("sub_title_color"),
        FieldPanel("cover_image"),
        FieldPanel("description"),
        FieldPanel("order_check"),
    ]

