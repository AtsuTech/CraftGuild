from django.shortcuts import render

# Create your views here.
# 特徴のページ
def calendar_field(request):

    times = [
        '10:00〜11:20',
        '11:40〜13:00',
        '14:20〜15:40',
        '16:00〜17:20',
        '17:40〜19:00',
    ]

    return render(
        request,
        template_name="form/calendar_field.html",
        context={
            "times": times,
        }
    )
