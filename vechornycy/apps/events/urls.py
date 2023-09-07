from django.urls import path
from . import views


app_name="events"
urlpatterns = [
    path("", views.MainView.as_view(), name="main page"),
    path("<int:pk>/", views.EventView.as_view(), name="post"),
        ]
