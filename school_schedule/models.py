from django.db import models
from wagtail.admin.panels import FieldPanel

#休講日
class SchoolSchedule(models.Model):

    day_off = models.DateField(
        # "Date",
        verbose_name="日付"
    )

    #管理画面で操作可能
    panels = [
        FieldPanel('day_off'),
    ]

    def __str__(self):
        #管理画面で、他モデルのドロップダウンで表示の設定
        return f"{self.day_off}"  