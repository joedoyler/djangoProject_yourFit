from django.urls import path
from . import views

urlpatterns = [
    path('forum/', BlogListView, name='blogs'),
    path('blog/<int:_id>', BlogDetailView, name='blog'),
]
