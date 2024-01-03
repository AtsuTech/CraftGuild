from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.urls import path

app_name = "accounts"


urlpatterns = [
    path('login/',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='accounts/login.html'
        ),
        name='login'),

    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
