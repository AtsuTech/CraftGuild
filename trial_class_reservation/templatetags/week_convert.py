from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime #年月日の処理に使用
import locale #曜日を日本語にするのに使用

register = template.Library()


@register.filter
@stringfilter
def ja_week(date): 

    # localeモジュールで時間のロケールを'ja_JP.UTF-8'に変更する
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

    # 20XX-0X-0Xの形式の年月日から日本語表記の曜日の文字列に変換する
    converted = datetime.strptime(date, "%Y-%m-%d").strftime("%a")

    return (converted)