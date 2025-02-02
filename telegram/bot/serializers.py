from .models import ChatBotUser, MessageHistory
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatBotUser
        fields = ('chat_id', 'url', 'full_name', 'username', 'language_code', 'reg_date')


class MessageHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageHistory
        fields = ('message_id', 'url' ,'chat_id', 'full_name', 'username', 'date', 'text')