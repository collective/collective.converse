---
labels:
- Stage-Alpha
...

Introduction
============

This is an experimental authentication module that does an asynchronous
HTTP call to verify a cookie, as received via BOSH or websocket.

Details
=======

The XMPP client asks to use the EXTERNAL authentication method, and includes in
the websocket connection or BOSH request a cookie.

Prosody sends this cookie to the authentication provider, which verifies it.
