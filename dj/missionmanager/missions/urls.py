from django.urls import path
from . import views

urlpatterns = [
    path('missions/', views.MissionListCreateView.as_view(), name='mission-list-create'),
    path('missions/<int:pk>/', views.MissionDetailView.as_view(), name='mission-detail'),
]
