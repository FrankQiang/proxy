from . import api
from .resources.proxy import ProxyAPI

api.add_resource(ProxyAPI, '/proxy')
