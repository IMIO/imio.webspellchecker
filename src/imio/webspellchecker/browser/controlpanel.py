from imio.webspellchecker import _
from Products.CMFPlone.utils import safe_unicode
from Products.statusmessages.interfaces import IStatusMessage
from plone.app.registry.browser.controlpanel import RegistryEditForm, ControlPanelFormWrapper
from z3c.form import button
from zope import schema
from zope.interface import implementer
from zope.interface import Interface

import os


class IIWebspellcheckerControlPanelSettings(Interface):
    """
    Settings for Document Generator.
    """


class IWebspellcheckerControlPanelSchema(Interface):
    """
    """

    service_id = schema.TextLine(
        title=_(u'Service ID'),
        description=_(u''),
        required=False,
        default=u"",
    )


@implementer(IIWebspellcheckerControlPanelSettings)
class WebspellcheckerControlPanelEditForm(RegistryEditForm):
    schema = IWebspellcheckerControlPanelSchema
    label = _(u'Webspellchecker settings')
    description = _(u'Webspellchecker settings control panel')


class WebspellcheckerSettings(ControlPanelFormWrapper):
    form = WebspellcheckerControlPanelEditForm
