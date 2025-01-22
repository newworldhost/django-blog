from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from django.contrib import messages
#from .forms import CommentForm

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = posts.comment.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )
    comment_form = CommentForm()


    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
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