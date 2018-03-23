from collective.converse import messageFactory as _
from zope import schema
from zope.interface import Interface
from zope.interface import Attribute


class IXMPPSecrets(Interface):
    totp_seed = Attribute(
        'totp_seed',
        'The seed value for generating time-based one-time-pin values')

    token_secret = Attribute(
        'token_secret', 'The shared secret for token generation')


class IXMPPSettings(Interface):
    """ Global XMPP settings. This describes records stored in the
        configuration registry and obtainable via plone.registry.
    """
    auto_subscribe = schema.Bool(
        title=_(u"label_xmpp_auto_subscribe",
                default=u"Automatically accept and subscribe back to "
                        u"presence subscriptions"),
        description=_(
            u"help_xmpp_auto_subscribe",
            default=u"In XMPP, presence subscriptions can be uni-directional "
            u"(similar to following someone on Twitter, but they don't "
            u"follow you back), or they can be mutual (similar to being "
            u"friends with someone on Facebook, where you both are "
            u"friends with one another. Set this option to true to ensure "
            u"that all presence subscriptions are automatically accepted "
            u"and reciprocated, making them mutual."),
        default=False,
    )

    xmpp_domain = schema.TextLine(
        title=_(u"label_xmpp_domain",
                default=u"XMPP Domain"),
        description=_(
            u"help_xmpp_domain",
            default=u"The domain which the XMPP server will serve."
            u"This is also the domain under which users are "
            u"registered. XMPP user ids are made up of the plone "
            u"username and domain, like this: ${username}@${domain}."),
        required=True,
        default=u'localhost',
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
