import json
import os

from Products.Five import BrowserView
from plone import api
from imio.webspellchecker.browser.controlpanel import IWebspellcheckerControlPanelSchema
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class WebspellcheckerInitJS(BrowserView):
    JS_SCRIPT_TEMPLATE = """
    $.getScript("{js_bundle_url}", function() {
        window.WEBSPELLCHECKER_CONFIG = {wsc_config};
    });
    """

    def __call__(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IWebspellcheckerControlPanelSchema)
        if settings.enabled:
            language = api.portal.get_current_language()
            return JS_SCRIPT_TEMPLATE.format(
                js_bundle_url=settings.js_bundle_url,
                wsc_config=self.format_json_settings(settings, language)
            )

    def format_json_settings(self, settings, language):
        """
        @return: Python dictionary of settings
        """

        return json.dumps({
            "autoSearch": True,
            "lang": 'auto',
            "localization": language,
            "theme": settings.theme,
            "removeBranding": settings.hide_branding,
            "serviceProtocol": settings.service_protocol,
            "serviceHost": settings.service_host,
            "servicePort": settings.service_port,
            "servicePath": settings.service_path,
        })
