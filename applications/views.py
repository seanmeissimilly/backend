from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApplicationSerializer, ApplicationclassificationSerializer
from .models import Application, Applicationclassification
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class ApplicationView(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class ApplicationclassificationView(viewsets.ModelViewSet):
    serializer_class = ApplicationclassificationSerializer
    queryset = Applicationclassification.objects.all()
