"""
This module enables you to configure your Plone site's registry for
collective.converse via buildout.

Just add something like the following under the [instance] section of your
buildout (i.e where you configure your plone instance):

zope-conf-additional +=
    <product-config collective.converse>
        instance_name Plone
        xmpp_domain localhost
        auto_subscribe 0
        bosh_url http://localhost:5280/http-bind
        debug 0
    </product-config>

WARNING: If you put the above in your buildout.cfg, your plone.registry entries
will be overridden with those values every time you restart your zope server.
In other words, you basically lose the ability to configure your xmpp settings
via Plone itself.
"""
from App.config import getConfiguration
from Products.CMFCore.utils import getToolByName
from collective.converse.interfaces import IXMPPSettings
from Products.GenericSetup.interfaces import IProfileImportedEvent
from zope.app.publication.zopepublication import ZopePublication
from zope.component import getUtility
import Globals
import Zope2
import plone.registry
import logging
import transaction

configuration = getConfiguration()
if not hasattr(configuration, 'product_config'):
    conf = None
else:
    conf = configuration.product_config.get('collective.converse')

log = logging.getLogger(__name__)


def dbconfig(event):
    """ """
    if IProfileImportedEvent.providedBy(event) and \
            event.profile_id != "profile-collective.converse:default":
        # We want to be able to automatically update the registry values
        # with the zope.conf config once the user has installed the add-on.
        return

    if conf is None:
        log.info('No product config found. Configuration will not be set')
        return

    db = Zope2.DB
    connection = db.open()
    root_folder = connection.root().get(ZopePublication.root_name, None)
    instance_name = conf.get('instance_name')
    if not instance_name:
        log.error('"instance_name" needs to be set if you want to configure '
                  'collective.converse from buildout.')

    if IProfileImportedEvent.providedBy(event):
        instance = event.tool.aq_parent
        if instance.id != instance_name:
            return
    else:
        instance = root_folder.get(instance_name)
        if instance is None:
            log.error('No Plone instance with instance_name "%s" found.'
                      % instance_name)
            return

    if Globals.DevelopmentMode and \
            bool(int(conf.get('ignore_in_debug_mode', 0))):
        log.info('Configuration settings for collective.converse are ignored '
                 'because Zope is starting up in debug_mode')
        return

    setup = getToolByName(instance, 'portal_setup')
    try:
        info = setup.getProfileInfo('profile-collective.converse:default')
    except KeyError:
        log.error('Could not find GS profile for collective.converse')
        return

    try:
        int(info.get('version', 0))
    except KeyError:
        log.error('Could not get intelligible profile version for '
                  'collective.converse')
        return

    if setup.getLastVersionForProfile('collective.converse:default') == \
            'unknown':
        log.info('Product not installed. Configuration will not be set')
        return

    registry = getUtility(
        plone.registry.interfaces.IRegistry,
        context=instance
    )
    settings = registry.forInterface(IXMPPSettings, check=False)
    if conf.get('xmpp_domain') is not None:
        settings.xmpp_domain = unicode(conf.get('xmpp_domain', u'localhost'))
    if conf.get('auto_subscribe') is not None:
        settings.auto_subscribe = bool(int(conf.get('auto_subscribe'), 0))
    if conf.get('bosh_url') is not None:
        settings.bosh_url = unicode(conf.get('bosh_url'))
    if conf.get('debug') is not None:
        settings.debug = bool(int(conf.get('debug')))
    transaction.commit()
