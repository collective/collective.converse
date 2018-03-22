require(['converse'], function (converse) {

    // Create a custom SASL Auth mechanism: SASL-HMAC
    var Strophe = converse.env.Strophe;
    Strophe.SASL_HMAC = function() {};
    Strophe.SASL_HMAC.prototype = new Strophe.SASLMechanism("HMAC", true, 60);
    Strophe.SASL_HMAC.prototype.test = Strophe.SASLPlain.prototype.test;
    Strophe.SASL_HMAC.prototype.onChallenge = Strophe.SASLPlain.prototype.onChallenge;

    var chatdata = document.getElementById('collective-xmpp-chat-data');
    converse.initialize({
        'auto_login': 'true',
        'allow_logout': false,
        'auto_list_rooms': true,
        'auto_subscribe': chatdata.getAttribute('auto_subscribe') === "True",
        'bosh_service_url': chatdata.getAttribute('bosh_url'),
        'credentials_url': chatdata.getAttribute('credentials_url'),
        'connection_options': {'mechanisms': [Strophe.SASL_HMAC]},
        'jid': chatdata.getAttribute('jid'),
        'debug': chatdata.getAttribute('debug') === "True",
        'hide_muc_server': true,
        'i18n': chatdata.getAttribute('lang')||'en',
        'locales_url': '++plone++collective.xmpp.chat/locale/{{{locale}}}/LC_MESSAGES/converse.json',
        'xhr_user_search': true
    });
});
