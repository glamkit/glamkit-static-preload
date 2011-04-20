import re

from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('static_preload.tests.static_preload_test_app.views',
    url(r'^tag_test/$', 'tag_test', name='tag_test'),
    url(r'^thingies/$', 'thingies', name='thingies'),
) 

# Serve static media (we can't use django.conf.urls.static, since it relies on 
# DEBUG being False)
urlpatterns += patterns('',
    url(r'^%s/(?P<path>.*)$' % re.escape(settings.MEDIA_URL.strip('/')),
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT},
    ),
)
