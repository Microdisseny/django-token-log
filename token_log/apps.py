from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TokenLogConfig(AppConfig):
    name = 'token_log'
    verbose_name = _('token log')
