import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'base.settings')
django_asgi_app = get_asgi_application()

import chnls.routing

application = ProtocolTypeRouter(
    {
        'http': django_asgi_app,
        'wegsocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(chnls.routing.websocket_url))
        )
    }
)
