from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MultimediaclassificationSerializer, MultimediaSerializer
from .models import Multimedia, Multimediaclassification
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class MultimediaView(viewsets.ModelViewSet):
    serializer_class = MultimediaSerializer
    queryset = Multimedia.objects.all()


# Solo si el usuario está autenticado.
@permission_classes([IsAuthenticated])
class MultimediaclassificationView(viewsets.ModelViewSet):
    serializer_class = MultimediaclassificationSerializer
    queryset = Multimediaclassification.objects.all()
