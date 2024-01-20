from django.urls import path
from . import views

app_name = "school_schedule"

urlpatterns = [
    path("add/schedule/",views.add_schedule,name="add_schedule"),
    path("delete/<int:id>",views.delete_schedule,name="delete_schedule"),
    # path("reservation/post", views.post_reservation_form, name='post_reservation'),
    # path('reservation/complete', views.post_complete, name='reservation_complete'),
]
