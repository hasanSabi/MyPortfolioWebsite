from django.views.generic import TemplateView, ListView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Project
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

class AboutView(TemplateView):
    template_name = 'portfolio/about.html'

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    ordering = ['-created_at']

class ContactView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        # Here you would typically send an email
        messages.success(self.request, "Thanks for reaching out! I'll get back to you soon.")
        return super().form_valid(form)
