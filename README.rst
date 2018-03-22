Introduction
============

``collective.converse`` integrates `converse.js <https://conversejs>`_ and the
`Prosody <https://prosody.im>`_ XMPP server into `Plone <https://plone.com>`_.

Features
========

* Manually or automatically subscribe to other users.
* With manual roster subscriptions, you can accept or decline contact requests.
* Chat statuses (online, busy, away, offline)
* Custom status messages
* Typing notifications (i.e when the contact is typing)
* Third person messages (/me )
* Multi-user chat in chatrooms
* Chatrooms can be configured (privacy, persistency etc.)
* Topics can be set for chatrooms
* Full name and profile picture support (via VCards)

Installation
============

Prosody is installed and configured via the `prosody.cfg` buildout profile.
Extend it in your own buildout in order to use it.

    [buildout]
    extends = /path/to/prosody.cfg
