from django.db import models
from wagtail.admin.panels import FieldPanel

#お問合せ内容のカテゴリ
class ContactCategory(models.Model):

    option = models.CharField(
        max_length=255,
        verbose_name="カテゴリ名を設定",
    )

    #管理画面で操作可能
    panels = [
        FieldPanel('option'),
    ]

    def __str__(self):
        #管理画面で、他モデルのドロップダウンで表示の設定
        return f"{self.option}"  

# お問合せフォーム
class ContactForm(models.Model):
    child_name1 = models.CharField(
        max_length=255,
        verbose_name="お子様の氏名(漢字)",
    )

    child_name2 = models.CharField(
        max_length=255,
        verbose_name="お子様の氏名(ふりがな)",
    )

    parent_name1 = models.CharField(
        max_length=255,
        verbose_name="保護者の氏名(漢字)",
    )

    parent_name2 = models.CharField(
        max_length=255,
        verbose_name="保護者の氏名(ふりがな)",
    )

    email = models.EmailField(
        verbose_name="メールアドレス"
    )

    phone_number = models.CharField(
        max_length=255,
        verbose_name="電話番号",
    )

    contact_category = models.ForeignKey(
        ContactCategory,
        on_delete=models.CASCADE,
        default=1,
        verbose_name="お問い合わせ内容選択",
    )

    comment = models.TextField(
        verbose_name="自由記入欄",
    )

    def __str__(self):
        #管理画面で、他モデルのドロップダウンで表示の設定
        return f"【{self.contact_category}】{self.parent_name1}:{self.comment}"  