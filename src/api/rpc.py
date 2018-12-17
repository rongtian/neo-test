# -*- coding:utf-8 -*-
import copy
import json

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

    def dumpprivkey(self, address):
        return self.simplerun("dumpprivkey", [address])

    def getaccountstate(self, address):
        return self.simplerun("getaccountstate", [address])

    def getassetstate(self, asset_id):
        return self.simplerun("getassetstate", [asset_id])

    def getbalance(self, asset_id):
        return self.simplerun("getbalance", [asset_id])

    def getbestblockhash(self):
        return self.simplerun("getbestblockhash", [])

    def getblock(self, hash, verbose=None):
        if verbose is None:
            return self.simplerun("getblock", [hash])
        else:
            return self.simplerun("getblock", [hash, verbose])

    def getblockcount(self):
        return self.simplerun("getblockcount", [])

    def getblockheader(self, hash, verbose=None):
        if verbose is None:
            return self.simplerun("getblockheader", [hash])
        else:
            return self.simplerun("getblockheader", [hash, verbose])

    def getblockhash(self, index):
        return self.simplerun("getblockhash", [index])

    def getblocksysfee(self, index):
        return self.simplerun("getblocksysfee", [index])

    def getconnectioncount(self):
        return self.simplerun("getconnectioncount", [])

    def getcontractstate(self, script_hash):
        return self.simplerun("getcontractstate", [script_hash])

    def getnewaddress(self):
        return self.simplerun("getnewaddress", [])

    def getrawmempool(self):
        return self.simplerun("getrawmempool", [])

    def getrawtransaction(self, txid, verbose=None):
        if verbose is None:
            return self.simplerun("getrawtransaction", [txid])
        else:
            return self.simplerun("getrawtransaction", [txid, verbose])

    def getstorage(self, script_hash, key):
        return self.simplerun("getstorage", [script_hash, key])

    def gettxout(self, txid, n=0):
        return self.simplerun("gettxout", [txid, n])

    def getpeers(self):
        return self.simplerun("getpeers", [])

    def getvalidators(self):
        return self.simplerun("getvalidators", [])

    def getversion(self):
        return self.simplerun("getversion", [])

    def getwalletheight(self):
        return self.simplerun("getwalletheight", [])

    def invoke(self, scripthash, params):
        return self.simplerun("invoke", [scripthash, params])

    def invokefunction(self, scripthash, operation, params):
        return self.simplerun("invokefunction", [scripthash, operation, params])

    def invokescript(self, script):
        return self.simplerun("invokescript", [script])

    def listaddress(self):
        return self.simplerun("listaddress", [])

    def sendfrom(self, asset_id, _from, to, value, fee=None):
        params = [asset_id, _from, to, value]
        if fee is not None:
            params.append(fee)
        return self.simplerun("sendfrom", params)

    def sendrawtransaction(self, hex):
        return self.simplerun("sendrawtransaction", [hex])

    def sendtoaddress(self, asset_id, address, value, fee):
        return self.simplerun("sendtoaddress", [asset_id, address, value, fee])

    def sendmany(self, params):
        return self.simplerun("sendmany", params)

    def validateaddress(self, address):
        return self.simplerun("validateaddress", [address])
