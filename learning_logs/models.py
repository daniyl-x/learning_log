from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, models.CASCADE)
    public = models.BooleanField(primary_key=False)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели"""
        text_preview = self.text[:50]
        if len(self.text) >= 50:
            text_preview += '...'
        return text_preview
