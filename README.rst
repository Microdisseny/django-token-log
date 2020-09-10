Django Token Log
================

|Build Status| |Coverage Status| |PyPI version|

Log csrfmiddlewaretoken on POST to avoid reuse (double-commit, etc.)

When added to your ModelAdmin, CsrfTokenLogMixin will reject a POST using a
csrfmiddlewaretoken that has already been used.

When added to your ModelAdmin, DisableButtonsOnSubmitMixin will avoid a second
click on the buttons of the submit row.


Usage
-----

Install with:

::

    pip install django-token-log

Add ''token\_log'' to INSTALLED\_APPS

Add the Mixin to the ModelAdmin you want to protect:

.. code-block:: python

    from django.contrib import admin

    from token_log.mixins import CsrfTokenLogMixin, DisableButtonsOnSubmitMixin


    class MyAdmin(DisableButtonsOnSubmitMixin, CsrfTokenLogMixin, admin.ModelAdmin):
        pass


.. |Build Status| image:: https://travis-ci.org/Microdisseny/django-token-log.svg?branch=master
    :target: https://travis-ci.org/Microdisseny/django-token-log
.. |Coverage Status| image:: https://coveralls.io/repos/github/Microdisseny/django-token-log/badge.svg?branch=master
    :target: https://coveralls.io/github/Microdisseny/django-token-log?branch=master
.. |PyPI version| image:: https://badge.fury.io/py/django-token-log.svg
    :target: https://badge.fury.io/py/django-token-log
