======================
GLAMkit static-preload
======================

Installation
------------

Requirements
~~~~~~~~~~~~
* Django 1.3+

To run the tests, glamkit-testtools is also required.

Usage
-----

Add ``static_preload`` to ``INSTALLED_APPS``, then in your template, 
``{% load static_preload %}``. Then use the "static_preload" templatetag to 
generate a URL to the statically served version of a local URL. The first
argument is the URL to preload, and the optional following arguments are
additional strings (which can be template variables) to append to GET 
parameters, e.g.::

	{% static_preload "/something/to/preload" "query=foo&page=bar" request.GET.urlencode %}

Settings
--------

PRELOAD_CACHE_ROOT
~~~~~~~~~~~~~~~~~~
The absolute path to the directory where the cached preloaded views will be 
stored.

Defaults to the "CACHE" subdirectory in ``MEDIA_ROOT``.

PRELOAD_CACHE_URL
~~~~~~~~~~~~~~~~~
The URL at which the cache root as defined above is being served from.

If ``PRELOAD_CACHE_ROOT`` is a subdirectory of ``MEDIA_ROOT```, which is its 
default behaviour, the default value of ``PRELOAD_CACHE_URL`` will be 
automatically calculated with the assumption that ``MEDIA_ROOT`` is available 
at ``MEDIA_URL``. Otherwise, an ``ImproperlyConfiguredError`` will be raised 
if a value is not provided.

PRELOAD_RAISE_ERRORS
~~~~~~~~~~~~~~~~~~~~
Setting this to ``True`` will result in any IOErrors (e.g. due to permission
or disk space issues on the cache folder) being raised instead of a fallback
to a non-preloaded URL.

Defaults to ``False``.

PRELOAD_INVALIDATING_MODELS
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A list of models that will trigger cache invalidation when modified. The list 
should be in ``['app.Model1', 'app.Model2', ... ]`` format.

Defaults to ``[]``, i.e. caches are permanent until the server is restarted, 
unless time-based invalidation is used.

PRELOAD_INVALIDATE_DAILY
~~~~~~~~~~~~~~~~~~~~~~~~
Setting this to ``True`` will result in the cache being invalidated daily. This 
is useful when the models used in your preloaded views have "expiration" dates.

Defaults to ``False``.

*Note that arbitrary invalidation time periods are not supported yet.*
