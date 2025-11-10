from django.views.generic import TemplateView, ListView
from portfolio.models import Project

class HomePageView(ListView): # Ubah dari TemplateView menjadi ListView
    model = Project # Tentukan model mana yang akan diambil
    template_name = 'core/home.html' # Tetap gunakan template home.html
    context_object_name = 'latest_projects' # Nama data di template

    def get_queryset(self):
        return Project.objects.order_by('-date_completed')[:3]

class AboutPageView(TemplateView):
    template_name = 'core/about.html'

class ServicesPageView(TemplateView):
    template_name = 'core/services.html'