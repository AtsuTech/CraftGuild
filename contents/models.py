from django.db import models
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel

# ---タグ実装---
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag as TaggitTag
# ---タグ実装---

#　管理画面でタグとカテゴリ編集
from wagtail.snippets.models import register_snippet

from wagtailmarkdown.fields import MarkdownField

# from django.shortcuts import redirect  
# from django.shortcuts import render
# from django.http import HttpResponse

from django.contrib.auth.decorators import login_required



#コンテンツの一覧のページ
class ContentsSelectingPage(Page):

    template = "contents/contents_selecting_page.html"

    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "contents.ContentsDetailPage",
    ]


    #ページのタイトル
    page_title = models.CharField(
        verbose_name="ここには”コンテンツ一覧”と入力",
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

        #コンテンツのデータを取得しpostsに格納
        contents = ContentsDetailPage.objects.live().public()

        #"contents"という名前で子ページで取り扱うようにする
        context["contents"] = contents

        return context        
    
# コンテンツのタグ
class ContentsTag(TaggedItemBase):
    content_object = ParentalKey(
        'ContentsDetailPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

@register_snippet
class ContentsTags(TaggitTag):
    class Meta:
        proxy = True
        #管理画面での表示
        verbose_name = "コンテンツのタグ"
        verbose_name_plural = "コンテンツのタグ管理"
    
#コンテンツの詳細のページ
class ContentsDetailPage(Page):

    #表示に使うテンプレート
    template = "contents/text_selecting_page.html"

    #追加できる子ページの種類を制限
    subpage_types = [
        #(アプリ名).(モデル名)
        "contents.TextPage",
    ]

    #　コンテンツのタイトル
    contents_name = models.CharField(
        verbose_name="コンテンツのタイトル(例:Unity など)",
        max_length=100,
        blank=False,
        null=False,
    )

    #　コンテンツの紹介文
    explanation = models.TextField(
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

    #　タグ
    tags = ClusterTaggableManager(
        verbose_name="タグ",
        through=ContentsTag, 
        blank=True
    )

    #　コンテンツの紹介文
    note = models.TextField(
        verbose_name="備考",
        blank=True,
        null=True,
    )


    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("contents_name"),
        FieldPanel("explanation"),
        FieldPanel("cover_image"),
        FieldPanel("tags"),
        FieldPanel("note"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)


        # カテゴリとテキストのクエリ
        categories = TextCategory.objects.all()
        texts = TextPage.objects.live().public()

        # 親(ContentsDetailPage)の子ページ(TextPage)で使用されているカテゴリだけを抽出
        categories_with_related_texts = categories.filter(textpage__in=self.get_children().specific(), textpage__categories__isnull=False).distinct()

        context["categories"] = categories_with_related_texts
        context["texts"] = texts
        
        return context

# テキストのカテゴリ
@register_snippet
class TextCategory(models.Model):
    name = models.CharField(max_length=255)
    panels = [
        FieldPanel('name'),
    ]
    def __str__(self):
        return self.name
    class Meta:
        #管理画面での表示
        verbose_name = "カテゴリ"
        verbose_name_plural = "テキストのカテゴリ管理"

# テキストのタグ
class TextPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'TextPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
        #管理画面での表示
        verbose_name = "タグ"
        verbose_name_plural = "テキストのタグ管理"

# テキスト
class TextPage(Page):

    #　テキストのタイトル
    text_name = models.CharField(
        verbose_name="テキストのタイトル",
        max_length=100,
        blank=False,
        null=False,
    )

    #　テキスト本文
    body = MarkdownField(
        verbose_name="テキストの本文(マークダウン形式でご入力下さい)",
        blank=True,
        null=True,
    )
    

    # カバー画像
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name="カバー画像",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    #　タグ
    tags = ClusterTaggableManager(
        verbose_name="タグ",
        through=TextPageTag, 
        blank=True
    )

    #　カテゴリ
    categories = models.ForeignKey(
        TextCategory,
        on_delete=models.PROTECT,
        verbose_name="コンテンツのカテゴリ選択",
        default=1,
    )

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("text_name"),
        FieldPanel("cover_image"),
        FieldPanel('tags'),
        FieldPanel("categories"),
        FieldPanel("body"),
    ]