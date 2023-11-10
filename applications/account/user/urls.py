from django.urls import path
from applications.account.user.views import RegistrationView

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration')
]
