import os

from Products.Five import BrowserView
from plone import api


class JsView(BrowserView):

    def __call__(self):
        wsc_token = os.getenv("WSC_TOKEN", "")
        language = api.portal.get_current_language()
        return """
            $.getScript("https://svc.webspellchecker.net/spellcheck31/wscbundle/wscbundle.js", function (){{}})
            window.WEBSPELLCHECKER_CONFIG = {{
                autoSearch:true,
                // enableAutoSearchIn: ['.mce_editable'],
                lang:'auto',
                localization:'{language}',
                serviceId:'{wsc_token}' // the activation key for the Cloud-based version
            }};
        """.format(wsc_token=wsc_token, language=language)


