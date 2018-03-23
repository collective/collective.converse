import zope.interface
from collective.converse.interfaces import IXMPPSecrets


class XMPPSecrets(object):
    zope.interface.implements(IXMPPSecrets)

    def __init__(self, *args, **kw):
        self.otp_secret = ''
        self.token_secret = ''
