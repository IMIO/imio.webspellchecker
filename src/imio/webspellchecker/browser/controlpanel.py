from Products.CMFCore.utils import getToolByName
from Products.ResourceRegistries.tools.JSRegistry import JSRegistryTool
from imio.webspellchecker import _
from Products.CMFPlone.utils import safe_unicode
from Products.statusmessages.interfaces import IStatusMessage
from plone.app.registry.browser.controlpanel import RegistryEditForm, ControlPanelFormWrapper
from z3c.form import button
from zope import schema
from zope.interface import implementer
from zope.interface import Interface

from plone import api
from imio.webspellchecker.interfaces import IIWebspellcheckerControlPanelSettings



class IWebspellcheckerControlPanelSchema(Interface):
    """
    """

    enabled = schema.Bool(
        title=_(u"Enabled"),
        description=_(u"Enable or disable Webspellchecker."),
        required=True,
        default=True,
    )
    hide_branding = schema.Bool(
        title=_(u"Hide branding"),
        description=_(u"Note: only available for server version."),
        required=True,
        default=False,
    )
    enable_grammar = schema.Bool(
        title=_(u"Enable grammar"),
        description=_(u"Enable grammar correction."),
        required=True,
        default=True,
    )
    theme = schema.Choice(
        title=_(u"Theme"),
        description=_(u""),
        required=True,
        vocabulary="imio.webspellchecker.vocabularies.Themes",
        default=u"default",
    )
    js_bundle_url = schema.TextLine(
        title=_(u"WSC JS bundle URL"),
        description=_(u""),
        required=True,
        default=u"default",
    )
    service_protocol = schema.Choice(
        title=_(u"Service protocol"),
        description=_(u""),
        required=False,
        vocabulary="imio.webspellchecker.vocabularies.HttpProtocols",
        default=u"https",
    )
    service_host = schema.TextLine(
        title=_(u"Service host"), description=_(u""), required=False, default=u"",
    )
    service_port = schema.Int(
        title=_(u"Service port"), description=_(u""), required=False, default=443,
    )
    service_path = schema.TextLine(
        title=_(u"Service path"), description=_(u""), required=False, default=u"",
    )
    service_id = schema.TextLine(
        title=_(u"Service ID"), description=_(u""), required=False, default=u"",
    )


@implementer(IIWebspellcheckerControlPanelSettings)
class WebspellcheckerControlPanelEditForm(RegistryEditForm):
    schema = IWebspellcheckerControlPanelSchema
    label = _(u"Webspellchecker settings")
    description = _(u"Webspellchecker settings control panel")

    def unregisterJS(self):
        id = api.portal.get_registry_record('js_bundle_url', interface=IWebspellcheckerControlPanelSchema)
        jstool = api.portal.get_tool('portal_javascripts')
        jstool.unregisterResource(id)

    def registerJS(self, data):
        jstool = api.portal.get_tool('portal_javascripts')  # type: JSRegistryTool
        jstool.registerScript(
            data["js_bundle_url"],
            enabled=True,
            cookable=False,
            skipCooking=True,
            cacheable=False
        )

    @button.buttonAndHandler(_('Save'), name=None)
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        self.unregisterJS()
        self.applyChanges(data)
        self.registerJS(data)
        IStatusMessage(self.request).addStatusMessage(_(u'Changes saved'), 'info')
        self.context.REQUEST.RESPONSE.redirect('@@webspellchecker-controlpanel')

    @button.buttonAndHandler(_('Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(_(u'Edit cancelled'), 'info')
        self.request.response.redirect(
            '{context_url}/{view}'.format(
                context_url=self.context.absolute_url(),
                view="@@overview-controlpanel"
            )
        )

class WebspellcheckerSettings(ControlPanelFormWrapper):
    form = WebspellcheckerControlPanelEditForm
