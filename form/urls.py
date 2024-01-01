from django.urls import path
from . import views

app_name = "introduction"

urlpatterns = [
    path("calendar/",views.calendar_field,name="feature_page"),
]
