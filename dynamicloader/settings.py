from django.conf import settings
"""
The dynamic template loader uses a mapping of ``request.META`` keys that maps a
regular expressions of potential values of that ``request.META`` key to a sequence
of template directories.

The ``DYN_TEMPLATE_MAP`` is a list of *exceptions* to the normal templates, as
Django is smart enough to use multiple template loaders.

For example::

DYN_TEMPLATE_MAP = \
    {
        'SERVER_NAME': 
            {
                re.compile('www1'): (os.path.join(settings.PROJ_ROOT,'www1templates'),)
                re.compile('www2'): (os.path.join(settings.PROJ_ROOT,'www2templates'),)
            },
        'HTTP_USER_AGENT': 
            {
                re.compile('Explorer'): (os.path.join(settings.PROJ_ROOT,'ie-templates'),)
            }
    }

This ``DYN_TEMPLATE_MAP`` looks for ``www1`` or ``www2`` in the ``SERVER_NAME``
header, and provides a place to look for templates respectively. If the 
``SERVER_NAME`` value is ``www.example.com``\ , Django simply moves on to the
next template loader.

This ``DYN_TEMPLATE_MAP`` also looks for ``Explorer`` in the ``HTTP_USER_AGENT``
header and provides a separate directory for Internet Explorer template overrides.

While it is not recommended that you use multiple headers, it is possible. The 
only issue is that the first template found will be used and it will not combine
values.
"""
TEMPLATE_MAP = getattr(settings, 'DYN_TEMPLATE_MAP', {})