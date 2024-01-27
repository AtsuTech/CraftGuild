from django.shortcuts import render, redirect
from .forms import PostReservationForm
from .models import TimeSlot #時間割モデル
from .models import Schedule #スケジュールモデル
from .models import Content #予約フォームモデルmoderu
from datetime import datetime ,timedelta#年月日の処理に使用
import calendar #月の日数取得
from django.core.mail import send_mail #メール送信処理
from django.template.loader import render_to_string #メール送信の際、txtファイルの内容を読み込みメール本文として出力

# Create your views here.

# 体験授業予約フォーム表示
def reservation_form_page(request):


    # 現在の日付を取得
    current_date = datetime.today() 

    #現在の年
    year = current_date.year

    #現在の月
    month = current_date.month

    #現在の日
    day = current_date.day
    #day = 31

    #現在の曜日を数字(月:0-日:6)で取得
    weekday = current_date.weekday()

    #月曜スタートの1週間の開始の日にちを計算{(今日の日にち)ー(月曜起点の今日の曜日までの日数)}
    start_day = day - weekday

    #今月は全部で何日かを取得
    day_total_now_month = calendar.monthrange(year, month)[1]

    #今日の日付から、今月最終日の間の日にち
    today_to_lastday =  (day_total_now_month - day) + 1



    #現在の日付を含んだ、月曜スタートの日にちを2ヶ月を配列に格納
    week_day_array = []
   
                    
    def generate_date_array():
        today = datetime.now().date()
        end_date = today + timedelta(days=60)

        date_array = []

        current_date = today
        while current_date <= end_date:
            date_array.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)

        return date_array

    week_day_array = generate_date_array()                

    #時間割のデータをDBより取得
    timeslots = TimeSlot.objects.all().order_by('start_time').reverse()

    #スケジュールのデータをDBより取得
    schedules = Schedule.objects.all()

    #コンテンツの選択肢をDBより取得
    contents = Content.objects.all()

    return render(
        request,
        template_name="trial_class_reservation/reservation_form_page.html",
        context={
            "timeslots": timeslots,
            "schedules": schedules,
            "contents": contents,
            "week_day_arry":week_day_array,
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


                """題名"""
                subject = "題名"
                
                #【本文】txtファイルを読み込み、本文として出力する
                message=render_to_string(
                    "mail/mail_message.txt", 
                    {
                        "child_name1":form.cleaned_data['child_name1'],
                        "child_name2":form.cleaned_data['child_name2'],
                        "parent_name1":form.cleaned_data['parent_name1'],
                        "parent_name2":form.cleaned_data['parent_name2'],
                        "email":form.cleaned_data['email'],
                        "phone_number":form.cleaned_data['phone_number'],
                        "date":form.cleaned_data['schedule'].date,
                        "time":target_schedule.timeslot,
                        "comment":form.cleaned_data['comment'],
                    }
                )

                """送信元メールアドレス"""
                from_email = "example@example.com"
                """宛先メールアドレス"""
                recipient_list = [
                    form.cleaned_data['email']
                ]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                if (capacity - reservation_total) == 1:
                    #予約時点で定員の残りが1枠の場合、今回の予約で満員になるので対象のスケジュールの予約可否を否(false)にする
                    target_schedule.available = False
                    target_schedule.save()

                return redirect('/reservation/complete')  # 保存後、一覧ページにリダイレクトするように変更
            else:
                #満員の時は予約フォーム画面に戻す
                return redirect('/trial_class/')
    else:
        form = PostReservationForm()

    #ここは、エラーの時の処理
    #request.session['post_error1'] = True
    return redirect('/reservation/error')


#送信完了後の処理
def post_complete(request):
    return render(request, 'trial_class_reservation/reservation_complete.html')



#エラー時の画面表示
def error(request):
    return render(request, 'trial_class_reservation/error.html')