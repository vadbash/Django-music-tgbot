from django.db import models

class ChatBotUser(models.Model):
    chat_id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    language_code = models.CharField(max_length=10)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.username}"

class MessageHistory(models.Model):
    message_id = models.IntegerField('Message ID')
    chat_id = models.IntegerField('Chat ID')
    full_name = models.CharField('Full name', max_length = 500)
    username = models.CharField('Username', max_length = 500)
    date = models.DateTimeField('Date', auto_now_add=True)
    text = models.CharField('Text', max_length=1500)

    def __str__(self):
        return str(self.message_id)

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
