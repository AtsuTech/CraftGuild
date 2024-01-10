from django.shortcuts import render

#メンターのモデルをインポート
from mentor.models import MentorDetailPage
from .models import QuestionPage
from trial_class_reservation.models import Schedule

#import calendar
from datetime import datetime
from calendar import monthcalendar,setfirstweekday

# 特徴のページ
def feature_page(request):

    return render(
        request,
        template_name="introduction/feature_page.html",
    )



# 教室紹介のページ
def online_school_page(request):

    #メンターのデータを取得しpostsに格納
    mentors = MentorDetailPage.objects.live().public()
    #cln = calendar.itermonthdates(2024, 1)

    year = 2024
    month = 1

    # 月曜日をスタートに設定
    #setfirstweekday(1)

    cal = monthcalendar(year, month)

    # カレンダー内の各日に対応するイベントを取得
    events = Schedule.objects.filter(date__year=year, date__month=month)

    # カレンダーのデータを作成
    calendar_data = []
    for week in cal:
        week_data = []
        for day in week:
            if day == 0:
                week_data.append({'day': '', 'events': []})
            else:
                date = datetime(year, month, day)
                day_events = events.filter(date=date)
                week_data.append({'day': day, 'events': day_events})
                #week_data.append({'day': day})
        calendar_data.append(week_data)

    return render(
        request,
        template_name="introduction/online_school_page.html",
        context={
            "mentors": mentors,
            "calendar":calendar_data,
        }
    )




# 体験のページ
def trial_class_page(request):

    return render(
        request,
        template_name="introduction/trial_class_page.html",
    )



# お問合せのページ
# def contact_page(request):

#     questions = QuestionPage.objects.all()



#     return render(
#         request,
#         "introduction/contact_page.html",
#         {'questions': questions}
#     )
