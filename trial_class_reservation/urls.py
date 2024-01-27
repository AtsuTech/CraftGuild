from django.urls import path
from . import views

app_name = "trial_class_reservation"

urlpatterns = [
    #path("resavation/",views.reservation_form_page,name="reservation_form_page"),
    path("reservation/post", views.post_reservation_form, name='post_reservation'),
    path("reservation/complete", views.post_complete, name='reservation_complete'),
    path("reservation/error",views.error,name='reservation_error'),
]
