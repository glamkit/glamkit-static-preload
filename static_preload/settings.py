import os
from django.conf import settings

RAISE_ERRORS = getattr(settings, 'PRELOAD_RAISE_ERRORS', False)

CACHE_ROOT = getattr(settings, 'PRELOAD_CACHE_ROOT',
    os.path.join(settings.MEDIA_ROOT, 'CACHE/static_preload/'))

try:
    CACHE_URL = getattr(settings, 'PRELOAD_CACHE_URL').rstrip('/')
except AttributeError:
    CACHE_URL = settings.MEDIA_URL.rstrip('/') + '/CACHE/static_preload'
