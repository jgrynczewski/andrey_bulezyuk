from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import reverse_lazy

from . import views

app_name = 'profiles'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name="profiles/login.html"),
        name="login"
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name="profiles/logout.html"),
        name="logout"
    ),

    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='profiles/password_reset.html',
            email_template_name = 'profiles/password_reset_email.html',
            success_url=reverse_lazy('profiles:password_reset_done'),
        ),
        name='password_reset'
    ),

    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='profiles/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password_reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='profiles/password_reset_confirm.html',
            success_url=reverse_lazy('profiles:password_reset_complete'),
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset/complete/',
        PasswordResetCompleteView.as_view(
            template_name='profiles/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    #
    # path(
    #     'password-reset/',
    #     PasswordResetView.as_view(
    #         template_name="profiles/password_reset.html",
    #         success_url = reverse_lazy('profiles:password_reset_done')
    #     ),
    #     name='password_reset'
    # ),
    # path(
    #     'password-reset/confirm/<uidb63>/<token>/',
    #     PasswordResetConfirmView.as_view(
    #         template_name="profiles/password_reset_confirm.html",
    #         success_url=reverse_lazy('profiles:password_reset_complete')
    #     ),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     'password-reset/done/',
    #     PasswordResetDoneView.as_view(
    #         template_name="profiles/password_reset_done.html",
    #     ),
    #     name="password_reset_done"
    # ),
    # path(
    #     'password_reset/complete/',
    #     PasswordResetCompleteView.as_view(
    #         template_name="profiles/password_reset_complete.html",
    #     ),
    #     name="password_reset_complete"
    # ),

    path('register/', views.register, name='register'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/update/', views.update, name='update'),
]