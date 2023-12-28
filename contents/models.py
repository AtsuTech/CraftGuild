from django.db import models
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


#コンテンツの一覧のページ
class ContentsSelectingPage(Page):

    template = "contents/contents_selecting_page.html"


    #ページのタイトル
    page_title = models.CharField(
        verbose_name="ページのタイトル(ここにはコンテンツの選択画面のページの名前を入力します)",
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
        posts = ContentsDetailPage.objects.live().public()

        #postsを"contents"という名前で子ページで取り扱うようにする
        context["contents"] = posts
        
        return context
    

#コンテンツの詳細のページ
class ContentsDetailPage(Page):

    #template = "mentor/mentor_detail_page.html"

    #　コンテンツのタイトル
    contents_name = models.CharField(
        verbose_name="コンテンツのタイトル",
        max_length=100,
        blank=False,
        null=False,
    )

    #　コンテンツの紹介文
    explanation = RichTextField(
        verbose_name="コンテンツの説明",
        blank=True,
        null=True,
    )

    # カバー画像
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name="カバー写真",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )


    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("contents_name"),
        FieldPanel("explanation"),
        FieldPanel("cover_image"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

