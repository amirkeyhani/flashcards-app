from django.urls import path

from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    # path('', TemplateView.as_view(template_name='cards/base.html'), name='home'), 
    path('', CardListView.as_view(), name='card-list'),
    path('new', CardCreateView.as_view(), name='card-create'), 
    path('edit/<int:pk>', CardUpdateView.as_view(), name='card-update'),
    path('box/<int:box_num>', BoxView.as_view(), name='box'),
]
