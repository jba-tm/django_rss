from django.views import generic
from django.http import response
from feeds.models import Post, Source
from feeds.utils import update_feeds

from .tasks import get_those_feeds

__all__ = ('PostsListView', 'PostDetailView', 'UpdateFeedView', 'SourceDetailView', 'SourceListView')


class PostsListView(generic.ListView):
    template_name = 'posts/index.html'
    model = Post
    paginate_by = 10


class PostDetailView(generic.DetailView):
    template_name = 'posts/detail.html'
    model = Post


class UpdateFeedView(generic.RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        update_feeds(30)
        return super().get(request, *args, **kwargs)


class SourceListView(generic.ListView):
    model = Source
    template_name = 'source/index.html'
    paginate_by = 10


class SourceDetailView(generic.DetailView):
    model = Source
    template_name = 'source/detail.html'
