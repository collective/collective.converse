from collective.converse import messageFactory as _
from zope import schema
from zope.interface import Interface


class IXMPPSettings(Interface):
    """ Global XMPP settings. This describes records stored in the
        configuration registry and obtainable via plone.registry.
    """
    auto_subscribe = schema.Bool(
        title=_(u"label_xmpp_auto_subscribe",
                default=u"Auto-subscribe XMPP users"),
        description=_(
            u"help_xmpp_auto_subscribe",
            default=u"Should XMPP users automatically be subscribed to one "
            u"another? "
            u"Users will automatically subscribe to all other XMPP "
            u"users in the site, but each subscription will only "
            u"be confirmed once the user being subscribed to logs "
            u"in. Be aware that this is probably a bad idea on "
            u"sites with many users!"),
        default=False,
    )

    bosh_url = schema.TextLine(
        title=_(u"label_xmpp_bosh_url",
                default=u"BOSH URL"),
        description=_(
            u"help_xmpp_bosh_url",
            default=u"The BOSH URL as exposed by your XMPP server."),
        required=True,
        default=u'http://localhost:5280/http-bind',
    )

    debug = schema.Bool(
        title=_(u"label_xmpp_debug",
                default=u"Debug"),
        description=_(
            u"help_xmpp_debug",
            default=u"Enable debug logging in the browser console."),
        default=False,
    )
