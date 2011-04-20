import os
from hashlib import md5

from django import template
from django.conf import settings
from django.core.urlresolvers import resolve, NoReverseMatch
from django.http import Http404, HttpRequest
from django.test.client import RequestFactory

from ..settings import CACHE_ROOT, CACHE_URL, RAISE_ERRORS

register = template.Library()


def hash(input):
    """
    Returns an MD5 hexdigest of provided string.
    e.g.: '59b82aa4663e0a4489bb8ffe71669ecd'
    """
    md5hash = md5()
    md5hash.update(input)
    return md5hash.hexdigest()

class StaticPreloadNode(template.Node):
    def __init__(self, url, *params):
        self.url = url
        self.params = params
    
    def render(self, context):
        # If url can't be determined, bail
        try:
            url = self.url.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        # Resolve parameters, ignoring failures
        params = []
        for param in self.params:
            try:
                params += [param.resolve(context)]
            except template.VariableDoesNotExist:
                pass
        # Combine the parameters into a single GET string
        params = '&'.join(p.lstrip('?').strip('&') for p in params if len(p))
        # Get view for url
        try:
            view, args, kwargs = resolve(url)
        except Http404:
            # In a future version, we may support external URLs, bail for now
            return ''
        # TODO: set extensions based on view's mimetype
        full_url = '%s?%s' % (url, params)
        # Avoid security, forbidden character, and filename length issues by
        # using a hash of the requested URL as the filename
        filename = hash(full_url)
        file_path = os.path.join(CACHE_ROOT, filename)
        if not os.path.exists(file_path):
            # Generate a cached version of the request.
            try:
                with open(file_path, 'w') as fp:
                    fp.write(
                        view(
                            RequestFactory().get(full_url),
                            *args, **kwargs
                        ).content,
                    )
            except IOError as error:
                # Since at this point we know we're able to get the view 
                # output, returning the URL for the uncached Django-served 
                # version is a better fallback than an empty string.
                # However, since it could be difficult to detect when 
                # something  actually went wrong, the 'PRELOAD_RAISE_ERRORS' 
                # setting can used to expose the error, despite Django's
                # recommendation not to raise errors in templatetags.
                if RAISE_ERRORS:
                    raise error
                return full_url
        return '%s/%s' % (CACHE_URL, filename)
        

@register.tag
def static_preload(parser, token):
    args = token.split_contents()[1:]
    if not args:
        raise template.TemplateSyntaxError(
            'static_preload tag requires at least one argument.')
    return StaticPreloadNode(*map(template.Variable, args))
