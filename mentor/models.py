#from django.db import models

# Create your models here.
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# Create your models here.


#メンターの一覧のページ
class MentorIntroductionPage(Page):

    #homeのHomePageが親ページになる
    #parent_page_types = ["home.HomePage"]

    template = "introduction/online_school_page.html"


    #ページのタイトル
    page_title = models.CharField(
        verbose_name="ページのタイトル(メンター紹介)",
        max_length=100,
        blank=True,
        null=True,
    )

    #ページの説明文
    page_explanation = models.CharField(
        verbose_name="ページの説明文",
        max_length=1000,
        blank=True,
        null=True,
    )

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        FieldPanel("page_explanation"),
    ]


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        #メンターのデータを取得しpostsに格納
        posts = MentorDetailPage.objects.live().public()

        #postsを"mentors"という名前で子ページで取り扱うようにする
        context["mentors"] = posts
        
        return context
    

#メンターの詳細のページ
class MentorDetailPage(Page):

    #template = "mentor/mentor_detail_page.html"

    #メンターの名前
    name = models.CharField(
        verbose_name="メンターの名前",
        max_length=100,
        blank=False,
        null=False,
    )

    # 画像
    image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name="画像",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )


    # メンターの紹介文
    explanation = RichTextField(
        verbose_name="メンターの紹介文",
        blank=True,
        null=True,
    )


    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("image"),
        FieldPanel("explanation"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

