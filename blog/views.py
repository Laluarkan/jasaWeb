from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    # Kita cari berdasarkan 'slug', bukan 'pk' (lebih baik untuk SEO)
    slug_field = 'slug'
    slug_url_kwarg = 'slug'