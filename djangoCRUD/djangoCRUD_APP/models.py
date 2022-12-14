from django.db import models

class Articles(models.Model):
    title = models.CharField("Название",max_length=100)
    url = models.CharField("Ссылка",max_length=100)
    content = models.TextField("Контент",max_length=1000)
    published = models.CharField("Публикация",max_length=20)
    category = models.CharField("Категория",max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"