from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = [
    path('source/', views.SourceListView.as_view(), name='source-list'),
    path('source/<int:pk>/', views.SourceDetailView.as_view(), name='source-detail'),
    path('', views.PostsListView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update-feed/', views.UpdateFeedView.as_view(), name='update-feed'),
]
