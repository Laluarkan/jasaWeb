from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'blog' # Namespace

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    # <slug:slug> artinya mencari berdasarkan slug
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]