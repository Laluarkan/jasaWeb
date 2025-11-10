# contract/urls.py
from django.urls import path
from . import views

app_name = 'contract'
urlpatterns = [
    path('', views.contract_list_view, name='contract_list'),
]