from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel



class Question(Page):

    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "question.QuestionItem",
    ]

    page_title = models.CharField( max_length=255, verbose_name="ページのタイトル(Q&A)")

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
    ]


class QuestionItem(Page):

    #質問
    inquiry = models.CharField( max_length=255, verbose_name="質問)")

    #回答
    answer = RichTextField(
        blank=True,
        null=True,
        verbose_name="回答",
    )

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("inquiry"),
        FieldPanel("answer"),
    ]