from django.shortcuts import HttpResponse, render
from .models import Post, Event


def main_page(request):
    latest_post_list=Post.objects.order_by("-publication_date")[:3]
    context = {"latest_post_list" : latest_post_list}
    print(context)
    return render(request, "blog/main_page.html", context)


def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "blog/post.html", {"post" : post})


