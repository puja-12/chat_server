import os

from channels.auth import AuthMiddlewareStack

from justchat.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application
from channels.routing import  ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import justchat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE','chat.settings')
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
      "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(justchat.routing.websocket_urlpatterns))
),
        # Just HTTP for now. (We can add other protocols later.)
    }
)