from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.defaults import *

urlpatterns = patterns('static_preload_test_app',
    url(r'^tag_test/$', 'tag_test', name='tag_test'),
    url(r'^thingies/$', 'thingies', name='thingies'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
