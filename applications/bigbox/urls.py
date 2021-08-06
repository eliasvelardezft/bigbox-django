from django.contrib import admin
from django.urls import path
from .views import (
    BoxListView,
    BoxDetailView,
    BoxActivityListView,
    ActivityDetailView
)

urlpatterns = [
    path('box/', BoxListView.as_view(), name='box-list-view'),
    
    path('box/<int:pk>/', BoxDetailView.as_view(), name='box-detail-view'),
    path('box/<int:box_id>/activity/', BoxActivityListView.as_view(), name='box-activity-list-view'),
    path('box/<int:box_id>/activity/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail-view'),

    path('box/<slug:slug>/', BoxDetailView.as_view(), name='box-detail-view-slug'),
    path('box/<slug:slug>/activity/', BoxActivityListView.as_view(), name='box-activity-list-view-slug'),
    path('box/<slug:slug>/activity/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail-view-slug'),
]
