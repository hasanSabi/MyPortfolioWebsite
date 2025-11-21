import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Project

projects = [
    {
        "title": "College Management System",
        "description": "A comprehensive system for managing college activities, student records, and attendance. Built with Django to ensure scalability and security.",
        "tech_stack": "Django, Python, SQLite, Bootstrap",
        "github_link": "https://github.com/sabihul/college-management-system"
    },
    {
        "title": "Network Verification Tool",
        "description": "A Python-based tool for verifying network configurations and topologies using Mininet. Automates the testing of network protocols.",
        "tech_stack": "Python, Mininet, NetworkX",
        "github_link": "https://github.com/sabihul/network-verification"
    },
    {
        "title": "Posts API",
        "description": "A high-performance RESTful API for managing blog posts and comments. Implements authentication, pagination, and filtering.",
        "tech_stack": "Python, FastAPI, PostgreSQL, Docker",
        "github_link": "https://github.com/sabihul/posts-api"
    }
]

for p in projects:
    Project.objects.get_or_create(title=p['title'], defaults=p)
    print(f"Created project: {p['title']}")

print("Database populated successfully!")
