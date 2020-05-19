from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    # path("<int:flight_id>", views.flight, name="flight"),
    # path("<int:flight_id>/book", views.book, name="book")
]