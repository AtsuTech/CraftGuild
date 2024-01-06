from django.db import models

# Create your models here.
from wagtail.admin.panels import FieldPanel

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from contents.models import TextCategory

 

#時間割モデル
class TimeSlot(models.Model):
    start_time = models.TimeField(
        # "Time",
        verbose_name="開始時刻"
    )
    end_time = models.TimeField(
        # "Time",
        verbose_name="終了時刻"
    )

    #管理画面で操作可能
    panels = [
        FieldPanel('start_time'),
        FieldPanel('end_time'),
    ]

    def __str__(self):
        #管理画面で、他モデルのドロップダウンで表示の設定
        return f"{self.start_time} - {self.end_time}"  


#体験授業スケジュールモデル
class Schedule(models.Model):
    date = models.DateField(
        # "Date",
        verbose_name="日付"
    )

    timeslot = models.ForeignKey(
        TimeSlot,
        on_delete=models.CASCADE,
        verbose_name="時間割を選択",
    )

    capacity = models.IntegerField(
        # "Number",
        verbose_name="定員(予約の上限数)"
    )

    available = models.BooleanField(
        verbose_name="予約可否",
        default=True
    )

    #管理画面で操作可能
    panels = [
        FieldPanel('date'),
        FieldPanel('timeslot'),
        FieldPanel('capacity'),
    ]

    def __str__(self):
        #管理画面で、他モデルのドロップダウンで表示の設定
        return f"{self.date}|{self.timeslot}"  

 



#体験予約フォームモデル
class ReservationForm(models.Model):
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
        # "Email Address",
        verbose_name="メールアドレス"
    )

    phone_number = models.CharField(
        max_length=255,
        verbose_name="電話番号",
    )

    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name="希望日時",
    )

    content = ParentalManyToManyField(
        TextCategory,
        verbose_name="コンテンツのカテゴリ選択",
        blank=True
    )

    comment = models.TextField(
        # "Content",
        verbose_name="自由記入欄"
    )