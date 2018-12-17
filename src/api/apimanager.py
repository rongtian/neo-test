import sys

sys.path.append('..')
sys.path.append('../..')

from api.node import NodeApi
from api.rpc import RPCApi
from api.cli import CLIApi


class APIManager():
    # Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(APIManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.nodeapi = NodeApi()
        self.rpcapi = RPCApi()
        self.cliapi = CLIApi()

    def node(self):
        return self.nodeapi

    def rpc(self, node=0):
        self.rpcapi.setnode(node)
        return self.rpcapi

    def cli(self):
        return self.cliapi


API = APIManager()
