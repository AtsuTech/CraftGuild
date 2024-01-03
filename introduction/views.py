from django.shortcuts import render

#メンターのモデルをインポート
from mentor.models import MentorDetailPage
from .models import QuestionPage


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

    return render(
        request,
        template_name="introduction/online_school_page.html",
        context={
            "mentors": mentors,
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
