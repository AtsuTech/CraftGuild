from django.urls import path
from . import views

#app_name = "introduction"

urlpatterns = [
    path("featureXXXXXX/",views.feature_page,name="feature_page"),
    path("online-schoolXXXX/",views.online_school_page,name="fonline_school_page"),
    path("trial-classXXXXX/",views.trial_class_page,name="trial_class_page"),
    # path("contact/",views.contact_page,name="contact_page"),
]
