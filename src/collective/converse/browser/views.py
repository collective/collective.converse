from datetime import datetime
from App.config import getConfiguration
from zExceptions.unauthorized import Unauthorized
from Products.Five import BrowserView
from Products.CMFPlone.controlpanel.browser.usergroups_usersoverview \
    import UsersOverviewControlPanel
import base64
import collective.converse
import hashlib
import hmac
import json
import logging
import plone.api
import pyotp
import random
log = logging.getLogger(__name__)


class SearchUsers(BrowserView):

    def __call__(self, *args, **kw):
        searchtext = self.request.form.get('q')
        # search terms of less then 3 chars return empty list
        if len(searchtext) < 2:
            return []
        panel = UsersOverviewControlPanel(self.context, self.request)
        return json.dumps([{
            'fullname': u['fullname'],
            'id': u['id']
            } for u in panel.doSearch(searchtext)])


class XMPPCredentials(BrowserView):

    def __call__(self):
        self.jid = self.get_jid()
        return json.dumps({
            'jid': self.jid,
            'password': self.get_token()
        })

    def get_token(self):
        configuration = getConfiguration()
        conf = configuration.product_config.get('collective.converse')

        otp_service = pyotp.TOTP(
            conf.get('otp_seed'),
            digits=collective.converse.OTP_DIGITS,
            interval=collective.converse.OTP_INTERVAL
        )
        otp = otp_service.generate_otp(
            otp_service.timecode(datetime.utcnow())
        )
        nonce = ''.join([str(random.randint(0, 9)) for i in range(32)])
        string_to_sign = otp + nonce + self.jid
        signature = hmac.new(
            conf.get('token_secret'),
            string_to_sign,
            hashlib.sha256
        ).digest()
        return u"{} {}".format(otp+nonce, base64.b64encode(signature))

    def get_jid(self):
        portal_membership = plone.api.portal.get_tool('portal_membership')
        if portal_membership.isAnonymousUser():
            raise Unauthorized()

        user = plone.api.user.get_current()
        domain = plone.api.portal.get_registry_record(
            'collective.converse.interfaces.IXMPPSettings.xmpp_domain'
        )
        return u"{}@{}".format(user.id, domain)
