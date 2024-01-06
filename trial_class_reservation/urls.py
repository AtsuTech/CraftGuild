from django.urls import path
from . import views

app_name = "introduction"

urlpatterns = [
    path("resavation/",views.reservation_form_page,name="reservation_form_page"),
    path('create/', views.post_reservation_form, name='post_reservation_form'),
]
