from django.shortcuts import render, redirect

from .models import SchoolSchedule
from .forms import SchoolScheduleForm

from datetime import datetime ,timedelta#年月日の処理に使用
# Create your views here.
import calendar
from calendar import monthcalendar,setfirstweekday

from django.http import HttpResponse
from django.utils import timezone

from django.shortcuts import get_object_or_404


def index(request):
    current_year = timezone.now().year
    calendar_html = calendar.HTMLCalendar().formatyear(current_year)

    # 現在の日付を取得
    current_date = datetime.today() 
    year = 2024

    
    #パラメータを取得する
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)

    # month パラメータが存在しないか場合、デフォルトで現在の年月を使用
    if month is not None:
        month = int(month)
    else:
        month = current_date.month

    if year is not None:
        year = int(year)
    else:
        year = current_date.year



    # 月曜日をスタートに設定
    #setfirstweekday(1)

    cal = monthcalendar(year, month)

    # カレンダー内の各日に対応するイベントを取得
    day_offs = SchoolSchedule.objects.filter(day_off__year=year, day_off__month=month)

    # カレンダーのデータを作成
    calendar_data = []
    for week in cal:
        week_data = []
        for day in week:
            if day == 0:
                week_data.append({'day': '', 'check': []})
            else:
                date = datetime(year, month, day)
                day_off = day_offs.filter(day_off=date)
                week_data.append({'day': day, 'check': day_off})
                #week_data.append({'day': day})
        calendar_data.append(week_data)

    return render(request, 'school_schedule/index.html', {
        "year":year,
        "month":month,
        "calendar_data":calendar_data,
        "day_offs":day_offs,
    })




#スケジュール新規登録処理
def add_schedule(request):

    if request.method == 'POST':
        #form = SchoolScheduleForm(request.POST)

        selected_record_ids = request.POST.getlist('day_off')
        for record_id in selected_record_ids:
            SchoolSchedule.objects.create(day_off=record_id) 


        # if form.is_valid():
        #     #form.save()
        #     fields = form.cleaned_data["day_off"]
        #     for day_off in fields:
        #         SchoolSchedule.objects.create(
        #             day_off=day_off,
        #             #day_off=fields,
        #         )
    
    return redirect('/admin/calendar/')



def delete_schedule(request, id):
    schedule = get_object_or_404(SchoolSchedule, pk=id)
    schedule.delete()
    return redirect('/admin/calendar/')