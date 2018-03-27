from zope import component
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.root import getNavigationRoot
from plone.app.layout.viewlets.common import ViewletBase
from collective.converse.interfaces import IXMPPSettings
import plone.api


class InitializationViewlet(ViewletBase):
    """ """

    def __init__(self, context, request, view, manager):
        super(InitializationViewlet, self).__init__(
            context, request, view, manager)

        pm = getToolByName(context, 'portal_membership')
        member = pm.getAuthenticatedMember()
        registry = component.getUtility(IRegistry)
        settings = registry.forInterface(IXMPPSettings, check=False)

        root = getNavigationRoot(self.context)
        username = member.getId()
        self.jid = u"{}@{}".format(username, settings.xmpp_domain)
        self.auto_subscribe = settings.auto_subscribe
        self.bosh_url = settings.bosh_url
        self.debug = settings.auto_subscribe
        self.credentials_url = '{}/@@xmpp-credentials'.format(root)
        self.xhr_user_search_url = '{}/@@search-users'.format(root)

        user = plone.api.user.get_current()
        self.nickname = user.getProperty('fullname')

        pstate = component.getMultiAdapter(
            (context, request), name='plone_portal_state')
        self.lang = pstate.language()
