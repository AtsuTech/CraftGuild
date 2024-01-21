from django.shortcuts import render, redirect

from .models import SchoolTimeSlot #時間割モデル
from .models import AvailableTime #利用可能な時間割モデル
from .models import SchoolSchedule #スケジュール(休校日)モデル

#from .forms import SchoolScheduleForm

from datetime import datetime ,timedelta#年月日の処理に使用
# Create your views here.
import calendar
from calendar import monthcalendar,setfirstweekday

from django.http import HttpResponse
from django.utils import timezone

from django.shortcuts import get_object_or_404

#時間割の管理画面
def timeslot_admin(request):

    times = SchoolTimeSlot.objects.all()
    day_code = [0,1,2,3,4,5,6]
    
    week_array = []
    for time in times:
        day_data = []
        for d in day_code:
            available = AvailableTime.objects.filter(day=d, time=time)
            day_data.append({'day': d, 'available': available})
        week_array.append({'time': time, 'days': day_data})

    return render(
        request, 
        'school_schedule/timeslot_admin.html', 
        {
            "times":times,
            "day_code":day_code,
            "week_array":week_array,
        }
    )

#時間割の登録
def add_timeslot(request):
    if request.method == 'POST':
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        SchoolTimeSlot.objects.create(
            start_time = start_time,
            end_time = end_time,
        ) 
    
    return redirect('/admin/timeslot/')

#時間割の編集画面
def edit_timeslot_view(request):
        
        id = request.GET.get('id')

        edit_timeslot = SchoolTimeSlot.objects.get(id=id)
        return render(
        request, 
        'school_schedule/edit_timeslot.html', 
        {
            "edit_timeslot":edit_timeslot,
        }
    )

#時間割の編集処理
def edit_timeslot(request,id):

    edit_timeslot = get_object_or_404(SchoolTimeSlot, pk=id)
    edit_timeslot.start_time = request.POST.get('start_time')
    edit_timeslot.end_time = request.POST.get('end_time')
    edit_timeslot.save() 
    return redirect('/admin/timeslot/')


#時間割の削除処理
def delete_timeslot(request,id):
    delete_timeslot = get_object_or_404(SchoolTimeSlot, pk=id)
    delete_timeslot.delete()
    return redirect('/admin/timeslot/')


#利用可能な時間割の登録
def add_available(request):
    if request.method == 'POST':
        #time = request.POST['time']
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        day = request.POST['day']
        AvailableTime.objects.create(
            time=SchoolTimeSlot.objects.get(start_time=start_time, end_time=end_time), 
            day = day,
        )     
    return redirect('/admin/timeslot/')


#利用可能な時間割の削除
def delete_available(request,id):
    delete_available = get_object_or_404(AvailableTime, pk=id)
    delete_available.delete()
    return redirect('/admin/timeslot/')

#休講日の管理画面
def index(request):
    current_year = timezone.now().year
    #calendar_html = calendar.HTMLCalendar().formatyear(current_year)

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


#休校の削除
def delete_schedule(request, id):
    schedule = get_object_or_404(SchoolSchedule, pk=id)
    schedule.delete()
    return redirect('/admin/calendar/')