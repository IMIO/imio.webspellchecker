import os

from Products.Five import BrowserView
from plone import api
from imio.webspellchecker.browser.controlpanel import IWebspellcheckerControlPanelSchema
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class JsView(BrowserView):
    def __call__(self):
        language = api.portal.get_current_language()
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IWebspellcheckerControlPanelSchema)
        if settings.enabled:
            js_string = """
                $.ajax({{
                    type: 'GET',
                    url: '{js_bundle_url}',
                    dataType: 'script',
                    cache: true
                }});
                window.WEBSPELLCHECKER_CONFIG = {{
                    autoSearch:true,
                    lang:'auto',
                    theme:'{theme}',
                    removeBranding: {hide_branding},
                    serviceProtocol:'{service_protocol}',
                    serviceHost:'{service_host}',
                    servicePort:'{service_port}',
                    servicePath:'{service_path}',
                    localization:'{language}'
                }};
            """.format(
                js_bundle_url=settings.js_bundle_url,
                language=language,
                theme=settings.theme,
                hide_branding=str(settings.hide_branding).lower(),
                service_protocol=settings.service_protocol,
                service_host=settings.service_host,
                service_port=settings.service_port,
                service_path=settings.service_path,
            )
            return js_string
