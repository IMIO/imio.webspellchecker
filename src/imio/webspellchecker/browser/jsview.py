import json
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
            js_string = "window.WEBSPELLCHECKER_CONFIG = {};".format(
                json.dumps(self.get_settings())
            )
            return js_string

    def get_settings(self):
        """
        @return: Python dictionary of settings
        """

        language = api.portal.get_current_language()
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IWebspellcheckerControlPanelSchema)

        return {
            "autoSearch": True,
            "lang": 'auto',
            "localization": language,
            "theme": settings.theme,
            "removeBranding": settings.hide_branding,
            "serviceProtocol": settings.service_protocol,
            "serviceHost": settings.service_host,
            "servicePort": settings.service_port,
            "servicePath": settings.service_path,
        }
