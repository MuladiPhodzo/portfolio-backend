from django.shortcuts import render
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# ✅ Fix: Move Home function outside the class
def home(request):
    return render(request, "portfolio/home.html")  # Ensure templates are configured correctly

