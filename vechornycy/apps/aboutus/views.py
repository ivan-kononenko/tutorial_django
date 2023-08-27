from django.shortcuts import render
from .models import Aboutus


def aboutus(request):
    aboutus=Aboutus.objects.get(pk=post_id)
    return render(request, "aboutus/aboutus.html", {"aboutus" : aboutus})

