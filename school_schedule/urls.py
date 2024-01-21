from django.urls import path
from . import views

app_name = "school_schedule"

urlpatterns = [
    path("add/timeslot/",views.add_timeslot,name="add_timeslot"),
    path("edit/timeslot/<int:id>",views.edit_timeslot,name="edit_timeslot"),
    path("delete/timeslot/<int:id>",views.delete_timeslot,name="delete_timeslot"),
    path("add/available",views.add_available,name="add_available"),
    path("delete/available/<int:id>",views.delete_available,name="delete_available"),
    path("add/schedule/",views.add_schedule,name="add_schedule"),
    path("delete/<int:id>",views.delete_schedule,name="delete_schedule"),

    # path("reservation/post", views.post_reservation_form, name='post_reservation'),
    # path('reservation/complete', views.post_complete, name='reservation_complete'),
]
