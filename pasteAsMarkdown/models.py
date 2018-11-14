from django.db import models


class Markdown(models.Model):
    markdown_txt = models.TextField()
    path = models.CharField(blank=True, unique=True, max_length=40)

    def __str__(self):
        return self.markdown_txt
