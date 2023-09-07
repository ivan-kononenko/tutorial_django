from django.shortcuts import HttpResponse, render
from .models import Post
from django.views import generic

class MainView(generic.ListView):
    template_name = "blog/main.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by("-publication_date")[:5]



class PostView(generic.DetailView):
    model = Post
    template_name = "blog/post.html"
