from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.MainView.as_view(), name="main page"),
    path("<int:pk>/", views.PostView.as_view(), name="post"),
]
