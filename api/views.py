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
    """
    API view to handle contact form submissions.
    """
    def get(self, request): 
        """
        Handle GET request to retrieve all contact entries.
        """
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Handle POST request to create a new contact entry.
        """
        serializer= ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)