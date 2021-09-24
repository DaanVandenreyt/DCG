from .base import *


if DEBUG:
    ALLOWED_HOSTS += [
        '*',
    ]

    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

    # tricks to have debug toolbar when developing with docker
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS = ['127.0.0.1', ip[:-1] + '1']
