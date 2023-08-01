from django.shortcuts import HttpResponse, render
from .models import Post, Event


def main_page(request):
    latest_post_list=Post.objects.order_by("-publication_date")[:3]
    context = {"latest_psot_list" : latest_post_list}
    return render(request, "blog/main_page.html", context)


def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)


