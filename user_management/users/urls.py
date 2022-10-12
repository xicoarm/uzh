# users/urls.py

from django.urls import path, include
from users.views import dashboard, start_charging, stats

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("start_charging", start_charging),
    path("stats", stats)
]