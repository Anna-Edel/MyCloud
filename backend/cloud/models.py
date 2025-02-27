# backend/cloud/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CloudUser(AbstractUser):
    full_name = models.CharField("Полное имя", max_length=255)
    storage_path = models.CharField("Путь к хранилищу", max_length=255, blank=True)

    def __str__(self):
        return self.username

class CloudFile(models.Model):
    user = models.ForeignKey(CloudUser, on_delete=models.CASCADE, related_name='files')
    original_name = models.CharField("Оригинальное имя", max_length=255)
    file = models.FileField("Файл", upload_to='user_files/')
    size = models.PositiveIntegerField("Размер файла")
    upload_date = models.DateTimeField("Дата загрузки", auto_now_add=True)
    last_download_date = models.DateTimeField("Последнее скачивание", null=True, blank=True)
    comment = models.TextField("Комментарий", blank=True)
    special_link = models.CharField("Специальная ссылка", max_length=255, blank=True)

    def __str__(self):
        return self.original_name
