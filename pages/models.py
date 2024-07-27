from django.db import models
from django.utils.translation import gettext_lazy as _

class InfoModel(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    info = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('info')
        verbose_name_plural = _('infos')
