from zope import component
from plone.registry.interfaces import IRegistry
from plone.app.layout.navigation.root import getNavigationRoot
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from collective.converse.interfaces import IXMPPSettings


class ChatData(ViewletBase):
    """ """

    def __init__(self, context, request, view, manager):
        super(ChatData, self).__init__(context, request, view, manager)
        pm = getToolByName(context, 'portal_membership')
        member = pm.getAuthenticatedMember()
        registry = component.getUtility(IRegistry)
        settings = registry.forInterface(IXMPPSettings, check=False)

        username = member.getId()
        # TODO: Fix hardcoding
        self.jid = u"{}@{}".format(username, 'mind')
        self.auto_subscribe = settings.auto_subscribe
        self.bosh_url = settings.bosh_url
        self.debug = settings.auto_subscribe
        self.credentials_url = '{}/@@xmpp-credentials'.format(
            getNavigationRoot(self.context)
        )

        pstate = component.getMultiAdapter(
            (context, request), name='plone_portal_state')
        self.lang = pstate.language()
