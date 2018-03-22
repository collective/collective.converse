# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from collective.converse import messageFactory as _
from collective.converse.interfaces import IXMPPSettings
from plone.app.registry.browser import controlpanel
from z3c.form import button
import logging

log = logging.getLogger(__name__)


class XMPPSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IXMPPSettings
    id = "XMPPSettingsEditForm"
    label = _(u"Converse.js XMPP settings")

    @button.buttonAndHandler(_('Save'), name=None)
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(_(u"Changes saved"),
                                                      "info")
        self.context.REQUEST.RESPONSE.redirect("@@xmpp-settings")

    @button.buttonAndHandler(_('Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(_(u"Edit cancelled"),
                                                      "info")
        self.request.response.redirect("%s/%s" % (self.context.absolute_url(),
                                                  self.control_panel_view))


class XMPPSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """ XMPP settings control panel.
    """
    form = XMPPSettingsEditForm
