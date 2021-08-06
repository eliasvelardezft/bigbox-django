from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import (
    Box,
    Activity
)

class BoxListView(ListView):
    model = Box
    context_object_name = 'box_list'
    template_name = 'bigbox/box_list.html'

class BoxDetailView(DetailView):
    model = Box
    template_name = 'bigbox/box_detail.html'
    context_object_name = 'box'

class BoxActivityListView(ListView):
    model = Activity
    context_object_name = 'box_activity_list'
    template_name = 'bigbox/activity_list.html'
    paginate_by = 20

class ActivityDetailView(DetailView):
    model = Activity
    context_object_name = 'activity'
    template_name = 'bigbox/activity_detail.html'