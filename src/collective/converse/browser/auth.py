from Products.Five import BrowserView
from datetime import datetime
import collective.converse
import base64
import hashlib
import hmac
import json
import logging
import plone.api
import pyotp
import random
log = logging.getLogger(__name__)


class XMPPCredentials(BrowserView):

    def __call__(self):
        return json.dumps({
            'jid': self.get_jid(),
            'password': self.get_token()
        })

    def get_token(self):
        # FIXME: these should be read from secrets.cfg
        otp_seed = 'XVGR73KMZH2M4XMY'
        token_secret = 'JYXEX4IQOEYFYQ2S3MC5P4ZT4SDHYEA7'

        otp_service = pyotp.TOTP(
            otp_seed,
            digits=collective.converse.OTP_DIGITS,
            interval=collective.converse.OTP_INTERVAL
        )
        otp = otp_service.generate_otp(
            otp_service.timecode(datetime.utcnow())
        )
        nonce = ''.join([str(random.randint(0, 9)) for i in range(32)])
        string_to_sign = otp + nonce + self.get_jid()
        signature = hmac.new(
            token_secret,
            string_to_sign,
            hashlib.sha256
        ).digest()
        return u"{} {}".format(otp+nonce, base64.b64encode(signature))

    def get_jid(self):
        user = plone.api.user.get_current()
        return u"{}@{}".format(user.id, 'mind')
