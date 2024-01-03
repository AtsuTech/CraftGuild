from django.urls import path
from . import views

app_name = "introduction"

urlpatterns = [
    path("feature/",views.feature_page,name="feature_page"),
    path("online-school/",views.online_school_page,name="fonline_school_page"),
    path("trial-class/",views.trial_class_page,name="trial_class_page"),
    # path("contact/",views.contact_page,name="contact_page"),
]
