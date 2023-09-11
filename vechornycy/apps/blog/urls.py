from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.MainView.as_view(), name="main page"),
    path("<int:pk>/", views.PostView.as_view(), name="post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

