from django.shortcuts import render, redirect
from .forms import PostReservationForm
from .models import TimeSlot #時間割モデル
from .models import Schedule #スケジュールモデル
from .models import ReservationForm #予約フォームモデルmoderu
import datetime 
import calendar #月の日数取得

# Create your views here.

# 体験授業予約フォーム表示
def reservation_form_page(request):


    # 現在の日付を取得
    current_date = datetime.datetime.today() 

    #現在の年
    year = current_date.year

    #現在の月
    month = current_date.month

    #現在の日
    day = current_date.day

    #現在の曜日を数字(月:0-日:6)で取得
    weekday = current_date.weekday()

    #月曜スタートの1週間の開始の日にちを計算{(今日の日にち)ー(月曜起点の今日の曜日までの日数)}
    start_day = day - weekday

    #今月は全部で何日かを取得
    day_total_now_month = calendar.monthrange(year, month)[1]

    #来月は全部で何日かを取得
    day_total_next_month = calendar.monthrange(year, month+1)[1]

    #今月から来月の2ヶ月間の合計日数
    two_month_day_total = day_total_now_month + day_total_next_month


    #現在の日付を含んだ、月曜スタートの日にちを2ヶ月を配列に格納
    week_day_arry = []
    for i in range(start_day, start_day + two_month_day_total, 1):

        #月と日にちは、zfill()メソッドで0埋めの2桁の表示に変換
        date = str(year) + '-' + str(month).zfill(2) + '-' + str(i).zfill(2)

        if i > day_total_now_month:

            date = str(year) + '-' + str(month + 1).zfill(2) + '-' + str(i - day_total_now_month).zfill(2)


        week_day_arry.append(date)

    #時間割のデータをDBより取得
    timeslots = TimeSlot.objects.all()

    #スケジュールのデータをDBより取得
    schedules = Schedule.objects.all()

    

    

    return render(
        request,
        template_name="trial_class_reservation/reservation_form_page.html",
        context={
            "timeslots": timeslots,
            "schedules": schedules,
            "week_day_arry":week_day_arry,
        }
    )



#フォーム送信処理
def post_reservation_form(request):

    #予約するスケジュールの定員の確認


    if request.method == 'POST':
        form = PostReservationForm(request.POST)

        if form.is_valid():

            #フォームから送信された希望スケジュールのidでScheduleモデルを絞り込む
            target_schedule = Schedule.objects.get(id=form.cleaned_data['schedule'].id)

            #絞り込んだ対象のScheduleの定員数をcapcityに格納
            capacity = target_schedule.capacity

            #絞り込んだ対象のScheduleに外部キーで紐づいている予約を逆リレーション(_setを付ける)で取得し予約数をカウントする
            reservation_total = target_schedule.reservationform_set.all().count()



            if capacity > reservation_total:
                #スケジュールの定員数が予約数より大きい時だけ予約できる
                form.save()

                if (capacity - reservation_total) == 1:
                    #予約時点で定員の残りが1枠の場合、今回の予約で満員になるので対象のスケジュールの予約可否を否(false)にする
                    target_schedule.available = False
                    target_schedule.save()

                return redirect('/')  # 保存後、一覧ページにリダイレクトするように変更
            else:
                #満員の時は予約フォーム画面に戻す
                return redirect('/resavation/')
    else:
        form = PostReservationForm()

    return render(request, 'trial_class_reservation/reservation_form_page.html', {'form': form})