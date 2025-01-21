from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    Models = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 3

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
        "coder": "Matt Rudge"},
    )
def event_detail(request, event_id):
    
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, event_id=event_id)

    return render(
        request,
        "events/event_detail.html",
        {"event": event}
    )