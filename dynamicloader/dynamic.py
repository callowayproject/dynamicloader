"""
Wrapper for changing the directories searched based on a request key
"""
import os, re
import django
version = django.VERSION

if version[0] >= 1 and version[1] >= 2:
    from django.template.loader import BaseLoader

from django.template import TemplateDoesNotExist
from django.conf import settings
from django.utils._os import safe_join

from dynamicloader.middleware import get_current_request
from dynamicloader.settings import TEMPLATE_MAP


def get_template_sources(template_name, template_dirs=None):
    """
    
    """
    request = get_current_request()
    if request:
        # Loop through the request.META mapping attributes
        for key, val in TEMPLATE_MAP.items():
            # Get the value from the request for that key
            req_val = request.META.get(key, None)
            if req_val is not None:
                # The request value exists, 
                for key, val in val.items():
                    if key.search(req_val):
                        for filepath in val:
                            yield safe_join(filepath, template_name)


def load_template_source(template_name, template_dirs=None):
    for filepath in get_template_sources(template_name, template_dirs):
        try:
            file = open(filepath)
            try:
                return (file.read().decode(settings.FILE_CHARSET), filepath)
            finally:
                file.close()
        except IOError:
            pass
    raise TemplateDoesNotExist(template_name)
load_template_source.is_usable = True


if version[0] >= 1 and version[1] >= 2:
    class Loader(BaseLoader):
        """
        Django 1.2 version of the template loader class
        """
        is_usable = True
        
        def get_template_sources(self, template_name, template_dirs=None):
            """
            Looks in the saved request object from the middleware for
            directories and passes back the path. Doesn't verify that the
            path is valid, though.
            """
            request = get_current_request()
            if request:
                # Loop through the request.META mapping attributes
                for key, val in TEMPLATE_MAP.items():
                    # Get the value from the request for that key
                    req_val = request.META.get(key, None)
                    if req_val is not None:
                        # The request value exists, 
                        for key, val in val.items():
                            if key.search(req_val):
                                for filepath in val:
                                    yield safe_join(filepath, template_name)
        
        def load_template_source(self, template_name, template_dirs=None):
            for filepath in self.get_template_sources(template_name, template_dirs):
                try:
                    file = open(filepath)
                    try:
                        return (file.read().decode(settings.FILE_CHARSET), filepath)
                    finally:
                        file.close()
                except IOError:
                    pass
            raise TemplateDoesNotExist(template_name)
        