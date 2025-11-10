from django.urls import path
from .views import ProjectListView, ProjectDetailView

app_name = 'portfolio' # Namespace

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    # <int:pk> artinya Primary Key (ID) dari proyek, misal: /portfolio/1/
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]