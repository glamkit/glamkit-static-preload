from testtools import TestToolsCase, StringGenerator

from static_preload_test_app.models import Thingie
from static_preload_test_app.views import tag_test


class CoreTest(TestToolsCase):
    test_app = 'static_preload.tests.static_preload_test_app'
    localise_app_loading = False
    urls = 'static_preload.tests.static_preload_test_app.urls'
    
    def setUp(self):
        super(CoreTest, self).setUp()
        self._strings = StringGenerator()
    
    def testBasicTagFunctionality(self):
        """
        Check if the tag is generating a link with the content we expect.
        """
        thingie_1 = Thingie.objects.create(
            content=self._strings['basic_1'],)
        
        regular_response = self.client.get('/thingies/')
        self.assertContains(
            regular_response,
            self._strings['basic_1'],
            count=1,
            msg_prefix='Verify the contents of the view to be cached')
        tag_response = self.client.get('/tag_test/')
        self.assertEqual(
            tag_response.status_code, 200,
            msg='Verify that the tag produces output')
        cached_response = self.client.get(tag_response.content)
        self.assertContains(
            cached_response,
            self._strings['basic_1'],
            count=1,
            msg_prefix='Verify the contents of the cached view')
        self.assertEqual(
            regular_response, tag_response,
            msg='Verify that the regular and cached view contents are identical')
        self.assertTemplateUsed(regual_respinse, 'thingies.html')
        self.assertTemplateNotUsed(
            cached_reponse, 'thingies.html',
            msg='Verify that the cached view was in fact cached')