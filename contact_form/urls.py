from django.urls import path
from . import views

app_name = "contact_form"

urlpatterns = [
    #path("resavation/",views.reservation_form_page,name="reservation_form_page"),
    path("contact/post", views.post_cotact_form, name='post_cotact'),
    path("contact/complete", views.post_complete, name='contact_complete'),
    path("contact/error",views.error,name='cotact_error'),
]
