# -*- coding:utf-8 -*-
import copy
import json
import sys

sys.path.append('..')
sys.path.append('../src')

from utils.taskdata import Task
from utils.taskrunner import TaskRunner
from utils.error import RPCError


class RPCApi:
    REQUEST_BODY = {
        "jsonrpc": "2.0",
        "method": "",
        "params": [],
        "id": 1
    }

    def __init__(self):
        self.currentnode = 0

    def setnode(self, node):
        self.currentnode = node

    def simplerun(self, rpcmethod, params, jsonrpc='2.0', id=1):
        request = copy.copy(RPCApi.REQUEST_BODY)
        request["method"] = rpcmethod
        request["params"] = params
        request["jsonrpc"] = jsonrpc
        request["id"] = id

        ijson = {}
        ijson["TYPE"] = "RPC"
        ijson["NODE_INDEX"] = int(self.currentnode)
        ijson["REQUEST"] = request
        ijson["RESPONSE"] = None
        task = Task(name=rpcmethod, ijson=ijson)
        (result, response) = TaskRunner.run_single_task(task, False)
        if response is None:
            raise Exception("rpc connect error")
        if response["jsonrpc"] != jsonrpc:
            raise Exception("rpc connect jsonrpc not valid: " + response["jsonrpc"])
        if response["id"] != id:
            raise Exception("rpc connect id not valid: " + str(response["id"]))
        if "error" in response.keys():
            raise RPCError(json.dumps(response["error"]))
        return response["result"]

    def dumpprivkey(self, address=None):
        params = []
        if address is not None:
            params.append(address)
        return self.simplerun("dumpprivkey", params)

    def getaccountstate(self, address=None):
        params = []
        if address is not None:
            params.append(address)
        return self.simplerun("getaccountstate", params)

    def getassetstate(self, asset_id=None):
        params = []
        if asset_id is not None:
            params.append(asset_id)
        return self.simplerun("getassetstate", params)

    def getbalance(self, asset_id=None):
        params = []
        if asset_id is not None:
            params.append(asset_id)
        return self.simplerun("getbalance", params)

    def getbestblockhash(self):
        return self.simplerun("getbestblockhash", [])

    def getblock(self, hash=None, verbose=None):
        params = []
        if hash is not None:
            params.append(hash)
        if verbose is not None:
            params.append(verbose)
        return self.simplerun("getblock", params)

    def getblockcount(self):
        return self.simplerun("getblockcount", [])

    def getblockheader(self, hash=None, verbose=None):
        params = []
        if hash is not None:
            params.append(hash)
        if verbose is not None:
            params.append(verbose)
        return self.simplerun("getblockheader", params)

    def getblockhash(self, index=None):
        params = []
        if index is not None:
            params.append(index)
        return self.simplerun("getblockhash", params)

    def getblocksysfee(self, index=None):
        params = []
        if index is not None:
            params.append(index)
        return self.simplerun("getblocksysfee", params)

    def getconnectioncount(self):
        return self.simplerun("getconnectioncount", [])

    def getcontractstate(self, script_hash=None):
        params = []
        if script_hash is not None:
            params.append(script_hash)
        return self.simplerun("getcontractstate", params)

    def getnewaddress(self):
        params = []
        return self.simplerun("getnewaddress", [])

    def getrawmempool(self):
        params = []
        return self.simplerun("getrawmempool", [])

    def getrawtransaction(self, txid=None, verbose=None):
        params = []
        if txid is not None:
            params.append(txid)
        if verbose is not None:
            params.append(verbose)
        return self.simplerun("getrawtransaction", params)

    def getstorage(self, script_hash=None, key=None):
        params = []
        if script_hash is not None:
            params.append(script_hash)
        if key is not None:
            params.append(key)
        return self.simplerun("getstorage", params)

    def gettxout(self, txid=None, n=0):
        params = []
        if txid is not None:
            params.append(txid)
        if n is not None:
            params.append(n)
        return self.simplerun("gettxout", params)

    def getpeers(self):
        params = []
        return self.simplerun("getpeers", [])

    def getvalidators(self):
        params = []
        return self.simplerun("getvalidators", [])

    def getversion(self):
        params = []
        return self.simplerun("getversion", [])

    def getwalletheight(self):
        params = []
        return self.simplerun("getwalletheight", [])

    def invoke(self, scripthash=None, params=None):
        iparams = []
        if scripthash is not None:
            iparams.append(scripthash)
        if params is not None:
            iparams.append(params)
        return self.simplerun("invoke", iparams)

    def invokefunction(self, scripthash=None, operation=None, params=None):
        iparams = []
        if scripthash is not None:
            iparams.append(scripthash)
        if operation is not None:
            iparams.append(operation)
        if params is not None:
            iparams.append(params)
        return self.simplerun("invokefunction", iparams)

    def invokescript(self, script=None):
        params = []
        if script is not None:
            params.append(script)
        return self.simplerun("invokescript", params)

    def listaddress(self):
        params = []
        return self.simplerun("listaddress", [])

    def sendfrom(self, asset_id=None, _from=None, to=None, value=None, fee=None):
        params = []
        if asset_id is not None:
            params.append(asset_id)
        if _from is not None:
            params.append(_from)
        if to is not None:
            params.append(to)
        if value is not None:
            params.append(value)
        if fee is not None:
            params.append(fee)
        return self.simplerun("sendfrom", params)

    def sendrawtransaction(self, hex=None):
        params = []
        if hex is not None:
            params.append(hex)
        return self.simplerun("sendrawtransaction", params)

    def sendtoaddress(self, asset_id=None, address=None, value=None, fee=None, change_address=None):
        params = []
        if asset_id is not None:
            params.append(asset_id)
        if address is not None:
            params.append(address)
        if value is not None:
            params.append(value)
        if fee is not None:
            params.append(fee)
        if change_address is not None:
            params.append(change_address)
        return self.simplerun("sendtoaddress", params)

    def sendmany(self, params=None):
        iparams = []
        if params is not None:
            iparams.append(params)
        return self.simplerun("sendmany", iparams)

    def validateaddress(self, address=None):
        params = []
        if address is not None:
            params.append(address)
        return self.simplerun("validateaddress", params)
