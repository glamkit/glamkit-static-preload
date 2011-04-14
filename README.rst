======================
GLAMkit static-preload
======================

Installation
------------

Usage
-----

Settings
--------

PRELOAD_INVALIDATING_MODELS
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A list of models that will trigger cache invalidation when modified. The list 
should be in ``['app.Model1', 'app.Model2' ... ]`` format.

Defaults to ``[]``, i.e. caches are permanent, unless time-based 
invalidation is used.

PRELOAD_INVALIDATE_DAILY
~~~~~~~~~~~~~~~~~~~~~~~~
Setting this to ``True`` will result in the cache being invalidated daily. This 
is useful when the models used in your preloaded views have "expiration" dates.

Defaults to ``False``.

*Note that arbitrary invalidation time periods are not supported yet.*
