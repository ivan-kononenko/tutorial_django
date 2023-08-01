from django.urls import path
from . import views


urlpatterns = [
    path("", views.main_page, name="main page"),
    path("<int:post_id>/", views.detail, name="detail"),
]
