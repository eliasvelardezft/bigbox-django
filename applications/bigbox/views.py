from django.db.models.query import QuerySet
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity_list_first_five'] = self.get_object().activities.all()[:5]
        return context
    

class BoxActivityListView(ListView): 
    model = Activity
    context_object_name = 'box_activity_list'
    template_name = 'bigbox/activity_list.html'
    paginate_by = 20
    
    def get_queryset(self):
        if 'slug' in self.kwargs:
            activities = Box.objects.get(slug=self.kwargs['slug']).activities.all()
        else:
            activities = Box.objects.get(pk=self.kwargs['pk']).activities.all()
            
        return super().get_queryset().filter(id__in=activities)

class ActivityDetailView(DetailView):
    model = Activity
    context_object_name = 'activity'
    template_name = 'bigbox/activity_detail.html'

    def get_queryset(self):
        if 'slug' in self.kwargs:
            activities = Box.objects.get(slug=self.kwargs['slug']).activities.all()
        else:
            activities = Box.objects.get(pk=self.kwargs['box_id']).activities.all()
        return super().get_queryset().filter(id__in=activities)
    