from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from contents.models import ContentsDetailPage #コンテンツのモデルをインポート


from learn.models import LearnItem #身につくことのモデルをインポート
from school_schedule.models import SchoolSchedule #教室のスケジュール(休校日)
from school_schedule.models import SchoolTimeSlot #時間割の時間の部分
from school_schedule.models import AvailableTime #時間割の◯の部分
from mentor.models import MentorDetailPage #メンターのモデルをインポート
from creation_flow.models import CreationFlowBlock #作成の流れのブロック
from particular.models import ParticularBlock #こだわりのブロック

from trial_class_reservation.forms import PostReservationForm
from price_plan.models import PricePlanBlock #料金プラン
from price_plan.models import PriceDescription #料金プランに関する説明文
from trial_class_reservation.models import TimeSlot #時間割モデル
from trial_class_reservation.models import Schedule #スケジュールモデル
from trial_class_reservation.models import Content #予約フォームモデルmoderu

from trial_flow.models import TrialFlowBlock #体験の流れのモデルを取得

from question.models import QuestionItem #Q&Aのモデル
from contact_form.models import ContactCategory#お問い合わせのカテゴリのモデル

from datetime import datetime ,timedelta#年月日の処理に使用
import calendar #月の日数取得
from django.core.mail import send_mail #メール送信処理
from django.template.loader import render_to_string #メール送信の際、txtファイルの内容を読み込みメール本文として出力



#import calendar
from datetime import datetime
from calendar import monthcalendar,setfirstweekday


# 特徴のページ
def feature_page(request):

    contents = ContentsDetailPage.objects.live().all()
    learns = LearnItem.objects.live().all()
    creation_flow_blocks = CreationFlowBlock.objects.live().all()
    #creation_flow_item = CreationFlowItem.objects.live().all()
    particular_blocks = ParticularBlock.objects.live().all()

     

    return render(
        request,
        template_name="all_pages_integration/feature_page.html",
         context={
            "contents": contents,
            "learns":learns,
            "creation_flow_blocks":creation_flow_blocks,
            #"creation_flow_item":creation_flow_item,
            "particular_blocks":particular_blocks,
        }
    )


#教室のページ
def online_school_page(request):

    plans = PricePlanBlock.objects.live().all()

    plan_description = PriceDescription.objects.live().all()

    mentors = MentorDetailPage.objects.live().all()

    #時間割表示用の配列を作成
    times = SchoolTimeSlot.objects.all()
    day_code = [0,1,2,3,4,5,6]
    
    week_array = []
    for time in times:
        day_data = []
        for d in day_code:
            available = AvailableTime.objects.filter(day=d, time=time)
            day_data.append({'day': d, 'available': available})
        week_array.append({'time': time, 'days': day_data})

    year = 2024
    month = 1

    # 月曜日をスタートに設定
    #setfirstweekday(1)

    cal = monthcalendar(year, month)

    # カレンダー内の各日に対応する休日を取得
    day_offs = SchoolSchedule.objects.filter(day_off__year=year, day_off__month=month)

    # カレンダーのデータを作成
    calendar_data = []
    for week in cal:
        week_data = []
        for day in week:
            if day == 0:
                week_data.append({'day': '', 'day_off': []})
            else:
                date = datetime(year, month, day)
                day_off = day_offs.filter(day_off=date)
                week_data.append({'day': day, 'day_off': day_off})
                #week_data.append({'day': day})
        calendar_data.append(week_data)

    return render(
        request,
        template_name="all_pages_integration/online_school_page.html",
         context={
            "plans":plans,
            "plan_description":plan_description,
            "week_array": week_array,
            "mentors": mentors,
            "calendar_data":calendar_data,
        }
    )

#体験授業
def trial_class_page(request):
    # 現在の日付を取得
    current_date = datetime.today() 

    #現在の年
    year = current_date.year

    #現在の月
    month = current_date.month

    #現在の日
    day = current_date.day

    #現在の曜日を数字(月:0-日:6)で取得
    weekday = current_date.weekday()

    #月曜スタートの1週間の開始の日にちを計算{(今日の日にち)ー(月曜起点の今日の曜日までの日数)}
    #start_day = day - weekday

    #今月は全部で何日かを取得
    #day_total_now_month = calendar.monthrange(year, month)[1]

    #今日の日付から、今月最終日の間の日にち
    #today_to_lastday =  (day_total_now_month - day) + 1



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
    timeslots = TimeSlot.objects.all()

    #スケジュールのデータをDBより取得
    schedules = Schedule.objects.all()

    contents = Content.objects.all()

    #体験の流れのモデルを取得
    flows = TrialFlowBlock.objects.all()

    return render(
        request,
        template_name="all_pages_integration/trial_class_page.html",
        context={
            "timeslots": timeslots,
            "schedules": schedules,
            "contents": contents,
            "flows":flows,
            "week_day_arry":week_day_array,
        }
    )

#お問あわせのページ
def contact_page(request):

    # contents = ContentsDetailPage.objects.live().all()
    questions = QuestionItem.objects.live().all()
    categorise = ContactCategory.objects.all()

    return render(
        request,
        template_name="all_pages_integration/contact_page.html",
         context={
            "questions":questions,
            "categorise": categorise,
        }
    )

#コンテンツのページ
def contents_page(request):

    contents = ContentsDetailPage.objects.live().all()

    return render(
        request,
        template_name="all_pages_integration/contents_page.html",
         context={
            "contents": contents,
        }
    )