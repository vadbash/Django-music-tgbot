from django.shortcuts import render
from .models import ChatBotUser, MessageHistory
from rest_framework import viewsets
from .serializers import UserSerializer, MessageHistorySerializer
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = ChatBotUser.objects.all().order_by('-reg_date')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 

class MessageHistoryViewSet(viewsets.ModelViewSet):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer
    permission_classes = [permissions.IsAuthenticated] 
