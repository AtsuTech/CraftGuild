from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel

# Create your models here.


#Q&Aの一覧のページ
class QuestionListingPage(Page):

    #template = "introduction/contact_page.html"
    #template = "contact_page.html"
    template = "introduction/feature_page.html"


    #ページのタイトル
    page_title = models.CharField(
        verbose_name="ページのタイトル(例: Q&Aページ)",
        max_length=100,
        blank=True,
        null=True,
    )


    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
    ]


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        #メンターのデータを取得しpostsに格納
        questions = QuestionPage.objects.live().public()

        #postsを"questions"という名前で子ページで取り扱うようにする
        context["questions"] = questions
        

class QuestionPage(Page):

    #(Q)質問文
    question = RichTextField(
        verbose_name="(Q)質問文",
        blank=True,
        null=True,
    )

    #(A)回答文
    answer = RichTextField(
        verbose_name="(A)回答文",
        blank=True,
        null=True,
    )

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("question"),
        FieldPanel("answer"),
    ]