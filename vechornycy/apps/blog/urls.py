from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.main_page, name="main page"),
    path("<int:post_id>/", views.post, name="post"),
]
