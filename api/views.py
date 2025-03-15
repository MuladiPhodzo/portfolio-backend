from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Project, Contact
from rest_framework.response import Response
from .serializers import ProjectSerializer, ContactSerializer
from .models import Contact

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ContactViewSet(APIView):
    queryset = Contact.objects.all()
    def post(self, request):
        serializer_class = ContactSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)