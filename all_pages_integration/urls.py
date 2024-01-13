from django.urls import path
from . import views

app_name = "all_pages_integration"

urlpatterns = [
    path("feature/",views.feature_page,name="feature_page"),
    path("online_school/",views.online_school_page,name="fonline_school_page"),
    path("trial_class/",views.trial_class_page,name="trial_class_page"),
    path("contact/",views.contact_page,name="contact_page"),
    path("contents/",views.contents_page,name="contents_page"),
]
