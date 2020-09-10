from django import forms
from django.contrib.admin.utils import quote
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import TokenLog


def _get_object_url(model_admin, object_id=None):
    opts = model_admin.model._meta
    if object_id is None:
        obj_url = reverse(
            'admin:%s_%s_changelist' % (opts.app_label, opts.model_name),
            current_app=model_admin.admin_site.name,
        )
    else:
        obj_url = reverse(
            'admin:%s_%s_change' % (opts.app_label, opts.model_name),
            args=(quote(object_id),),
            current_app=model_admin.admin_site.name,
        )
    return obj_url


def _save_token(model_admin, request):
    token = request.POST.get('csrfmiddlewaretoken')
    TokenLog.objects.create(token=token, user=request.user)


class CsrfTokenLogMixin:
    def add_view(self, request, form_url='', extra_context=None):
        if request.method == 'POST':
            try:
                _save_token(self, request)
            except IntegrityError:
                obj_url = _get_object_url(self)
                return HttpResponseRedirect(obj_url)

        return super().add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.method == 'POST':
            try:
                _save_token(self, request)
            except IntegrityError:
                if "_saveasnew" in request.POST:
                    object_id = None
                obj_url = _get_object_url(self, object_id)
                return HttpResponseRedirect(obj_url)

        return super().change_view(request, object_id, form_url, extra_context)


class DisableButtonsOnSubmitMixin:
    @property
    def media(self):
        return super().media + forms.Media(
            css={'all': ['token_log/disable_buttons_on_submit.css']},
            js=['admin/js/jquery.init.js', 'token_log/disable_buttons_on_submit.js'],
        )
