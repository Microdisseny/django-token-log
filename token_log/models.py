from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TokenLog(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    token = models.TextField(_('token'), null=False, blank=False, unique=True)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='tokenlogs',
        verbose_name=_('token logs'),
        on_delete=models.CASCADE
    )
