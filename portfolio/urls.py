from django.urls import path
from .views import HomeView, AboutView, ProjectListView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
]
