# -*- coding:utf-8 -*-
import unittest
import os
import sys
import time
import traceback
import json
from test_config import test_config

sys.path.append('..')
sys.path.append('../..')
testpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(testpath)

from utils.logger import LoggerInstance as logger
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.error import AssertError, RPCError
from utils.config import Config
from api.apimanager import API
from neo.walletmanager import WalletManager
from neo.wallet import Wallet, Account


######################################################
# test cases
class test_rpc_1(ParametrizedTestCase):
    def setUp(self):
        API.cli().init(self._testMethodName, Config.NODES[0]["path"])
        logger.open("test_rpc/" + self._testMethodName + ".log", self._testMethodName)

    def tearDown(self):
        API.cli().terminate()
        logger.close(self.result())

    ###invoke 141-152
    ###正确的值
    def test_141_invoke(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invoke(test_config.invokescript, [{"type": "String","value": "name"},{"type":"Boolean","value": False}])
            self.ASSERT(result["state"]=="HALT, BREAK", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###invokescript_notexist
    def test_142_invoke(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invoke(test_config.invokescript_notexist, [{"type": "String","value": "name"},{"type":"Boolean","value": False}])
            self.ASSERT(result["state"]=="FAULT, BREAK", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###wrong_str
    def test_143_invoke(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invoke(test_config.wrong_str, [{"type": "String","value": "name"},{"type":"Boolean","value": False}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###scripthash  ""        
    def test_145_invoke(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invoke("", [{"type": "String","value": "name"},{"type":"Boolean","value": False}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
    
    ###scripthash不填    
    def test_146_invoke(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invoke([{"type": "String","value": "name"},{"type":"Boolean","value": False}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###param []
    def test_149_invoke(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invoke(test_config.invokescript, [])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###param wrong_str
    def test_150_invoke(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invoke(test_config.invokescript, [test_config.wrong_str])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###param ""
    def test_151_invoke(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invoke(test_config.invokescript, [""])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###param不填
    def test_152_invoke(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invoke(test_config.invokescript)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    

    
    ###invokefunction 153-170
    ###正确的值
    def test_153_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript, "name", [])
            self.ASSERT(result["state"]=="HALT, BREAK", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###invokescript_notexist
    def test_154_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript_notexist, "name", [])
            self.ASSERT(result["state"]=="FAULT, BREAK", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###invokescript wrong_str
    def test_155_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.wrong_str, "name", [])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###invokescript ""
    def test_157_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction("", "name", [])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###invokescript不填
    def test_158_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction( "name", [])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###operation不存在
    def test_160_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript, "test", [])
            self.ASSERT(result["state"]=="FAULT, BREAK", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###operation abc
    def test_161_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript, test_config.wrong_str, [])
            self.ASSERT(result["state"]=="FAULT, BREAK", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###operation ""
    def test_163_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript, "", [])
            self.ASSERT(result["state"]=="FAULT, BREAK", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###operation 不填
    def test_164_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript, params=[])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Specified cast is not valid.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###param []
    def test_166_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript, "name", [])
            self.ASSERT(result["state"]=="HALT, BREAK", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###params abc
    def test_167_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript, "name", test_config.wrong_str)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###param ""
    def test_169_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript, "name", "")
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###param不填
    def test_170_invokefunction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokefunction(test_config.invokescript, "name")
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")

    ###invokescript 171-176
    ###正确的值
    def test_171_invokescript(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokescript(test_config.invokescript)
            print ("result:"+str(result))
            self.ASSERT(result["tx"]==test_config.tx, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###script invokescript_notexist
    def test_172_invokescript(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokescript(test_config.invokescript_notexist)
            print ("result:"+str(result))
            self.ASSERT(result["state"]=='FAULT, BREAK', "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###script abc
    def test_173_invokescript(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().gettxout(test_config.invokescript_wrong_str)
            print ("result:"+str(result))
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###script ""
    def test_175_invokescript(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokescript("")
            print ("result:"+str(result))
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###script不填        
    def test_176_invokescript(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().invokescript()
            print ("result:"+str(result))
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
    
    ###listaddress 177-178
    ###正确的值
    def test_177_listaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().listaddress()
            print ("result:"+str(result))
            self.ASSERT(result[0]["address"]==WalletManager().wallet(0).account().address(), "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###不打开钱包
    def test_178_listaddress(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().listaddress()
            print ("result:"+str(result))
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Access denied.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")

    ###sendfrom 179-213 
    ###正确的值
    def test_179_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=0,change_address=WalletManager().wallet(0).account().address())
            self.ASSERT(result["type"]=="ContractTransaction", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###asset_id_notexist
    def test_180_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom("test_config.asset_id_notexist",
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###wrong_str
    def test_181_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.wrong_str,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###asset_id ""        
    def test_183_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom("",
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###asset_id 不填
    def test_184_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(traceback.format_exc().split("TypeError: ")[1]=="sendfrom() missing 1 required positional argument: 'to'\n", "")
            
    ###from格式正确但不存在
    def test_186_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                test_config.address_notexist,
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###from abc
    def test_187_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                test_config.wrong_str,
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###from ""        
    def test_189_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                "",
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###from不填
    def test_190_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(traceback.format_exc().split("TypeError: ")[1]=="sendfrom() missing 1 required positional argument: 'to'\n", "")
            
            
    ###to格式正确但不存在
    def test_192_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                test_config.address_notexist,
                value=10,fee=0)
            self.ASSERT(result["type"]=="ContractTransaction", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###to abc
    def test_193_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                test_config.wrong_str,
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            

    ###to ""        
    def test_195_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                "", value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###to不填
    def test_196_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(traceback.format_exc().split("TypeError: ")[1]=="sendfrom() missing 1 required positional argument: 'to'\n", "")
    
    ###value=0        
    def test_199_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=0,fee=0)
            self.ASSERT(result["type"]=="ContractTransaction", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###value过大
    def test_200_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=1000000000,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Insufficient funds", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###value<0        
    def test_201_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=-1,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(json.loads(e.msg)["message"]=="Invalid params", "")
            
    ###value abc
    def test_202_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=test_config.wrong_str,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(json.loads(e.msg)["message"]=="Invalid params", "")
            
    ###value ""
    def test_203_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value="",fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(json.loads(e.msg)["message"]=="Invalid params", "")
    
    ###value不填
    def test_204_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(),fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(traceback.format_exc().split("TypeError: ")[1]=="sendfrom() missing 1 required positional argument: 'value'\n", "")
            
    ###fee=0.00000001    
    def test_207_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=0.00000001)
            self.ASSERT(result["net_fee"]==0.00000001, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###0<fee<0.00000001
    def test_208_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=0.00000000001)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Arithmetic operation resulted in an overflow.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee过大
    def test_209_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=100000000)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Insufficient funds", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee<0
    def test_210_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=-1)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Invalid params", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee ""
    def test_211_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee="")
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Input string was not in a correct format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee不填
    def test_212_sendfrom(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10)
            self.ASSERT(result["size"]==262, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    #不打开钱包
    def test_213_sendfrom(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendfrom(test_config.asset_id_right,
                WalletManager().wallet(0).account().address(),
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Access denied", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            

    ###sendrawtransaction 214-219
    ###send 0xc56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b AWrEuiUfQ8WdHmaB25M5Frd6LyJyuCnv2u 1  从钱包5转账1个NEO给钱包6
    ###正确的值
    def test_214_sendrawtransaction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendrawtransaction(test_config.hex_right)
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###hex_notexists
    def test_215_sendrawtransaction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendrawtransaction(test_config.hex_notexists)
            self.ASSERT(result!=None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
            #self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###wrong_str
    def test_216_sendrawtransaction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendrawtransaction(test_config.wrong_str)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###hex ""        
    def test_218_sendrawtransaction(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendrawtransaction("")
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###hex不填
    def test_219_sendrawtransaction(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendrawtransaction()
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
    


            
    ###sendtoaddress 221-250 
    ###正确的值
    def test_221_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee=0,change_address=WalletManager().wallet(0).account().address())
            self.ASSERT(result["type"]=="ContractTransaction", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###asset_id_notexist
    def test_222_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_notexist,
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="not found", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###asset_id abc        
    def test_224_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress("abc",
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###asset_id ""
    def test_225_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress("",
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###asset_id不填
    def test_226_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###value超出原有金额        
    def test_228_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), 1000000000,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Insufficient funds", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###value<0
    def test_229_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), -1,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Invalid params", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###value 0.1
    def test_230_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), 0.1,fee=0)
            self.ASSERT(result["type"]=="ContractTransaction", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###value abc
    def test_232_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), test_config.wrong_str,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###value ""
    def test_233_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), "",fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###value不填
    def test_234_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(),fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###address_notexist
    def test_236_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                test_config.address_notexist, value=10,fee=0)
            self.ASSERT(result["type"]=="ContractTransaction", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###address abc
    def test_238_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                "abc", value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###address ""
    def test_239_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                "", value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###address 不填
    def test_240_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee=0.00000001
    def test_241_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee=0.00000001)
            self.ASSERT(result["type"]=="ContractTransaction", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee太小
    def test_242_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee=0.000000001)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Arithmetic operation resulted in an overflow.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee=10
    def test_244_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee=10)
            self.ASSERT(result["type"]=="ContractTransaction", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee=-1
    def test_245_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee=-1)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Invalid params", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee过大
    def test_246_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee=1000000000)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Insufficient funds", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee abc
    def test_247_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee=test_config.wrong_str)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Input string was not in a correct format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee ""
    def test_248_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee="")
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Input string was not in a correct format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee不填
    def test_249_sendtoaddress(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10)
            self.ASSERT(result["type"]=="ContractTransaction", "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    #不打开钱包
    def test_250_sendtoaddress(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendtoaddress(test_config.asset_id_right,
                WalletManager().wallet(1).account().address(), value=10,fee=0)
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Access denied", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")

    
    ###sendmany 251-279
    ###需要先打开钱包
    ###100个同时转账，都为正确
    def test_251_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()}])
            self.ASSERT(result!=None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
    
    ###100个同时转账，50组出错        
    def test_252_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address()}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Invalid params", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###单独一组转账,正确
    def test_253_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0}])
            self.ASSERT(result!=None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    #asset不合法
    def test_254_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.wrong_str,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
    
    #[{"":""}]
    def test_255_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"":""}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###"value": -1
    def test_256_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address(),"fee":0}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Invalid params", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###"value": ""
    def test_257_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":"","address":WalletManager().wallet(1).account().address(),"fee":0}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###"address": "abc"
    def test_258_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":test_config.wrong_str,"fee":0}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###"address": ""
    def test_259_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":"","fee":0}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###第一个[]出错
    def test_260_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address(),"fee":0},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0},{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
        except Exception as e:
            logger.error(traceback.format_exc())
            
    ###三个[]同时出错
    def test_261_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address(),"fee":0},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address(),"fee":0},{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address(),"fee":0}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
        except Exception as e:
            logger.error(traceback.format_exc())
            
    ###[""]
    def test_262_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([""])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Invalid params", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###[]不填
    def test_263_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee=0.00000001
    def test_264_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0.00000001}])
            self.ASSERT(result!=None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###0<fee<0.00000001
    def test_266_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0.0000000001}])
            self.ASSERT(result!=None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Arithmetic operation resulted in an overflow.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
    
    ###0<fee<原有本金
    def test_267_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":1}])
            self.ASSERT(result!=None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
            
    ###fee<0
    def test_268_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":-1,"address":WalletManager().wallet(1).account().address(),"fee":1}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee>原有本金
    def test_269_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":1000000000}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Insufficient funds", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee="abc"
    def test_270_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":"abc"}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Input string was not in a correct format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee=""
    def test_271_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":""}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Input string was not in a correct format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###fee不填
    def test_272_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address()}])
            self.ASSERT(result!=None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    #change_address不存在
    def test_274_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0,"change_address":test_config.address_notexist}])
            self.ASSERT(result!=None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###change_address="abc"
    def test_276_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0,"change_address":test_config.wrong_str}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###change_address=""
    def test_277_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0,"change_address":""}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="One of the identified items was in an invalid format.", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###change_address不填
    def test_278_sendmany(self):
        try:
            API.cli().open_wallet(Config.WALLET_PATH + "/" + Config.NODES[0]["walletname"], "11111111")
            API.cli().list_address(lambda msg: msg.find(WalletManager().wallet(0).account().address()) >= 0)
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###不打开钱包
    def test_279_sendmany(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().sendmany([{"asset":test_config.asset_id_right,"value":1,"address":WalletManager().wallet(1).account().address(),"fee":0}])
            self.ASSERT(result==None, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Access denied", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            

    ###validateaddress 280-285完成
    ###正确的值
    def test_280_validateaddress(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().validateaddress(WalletManager().wallet(0).account().address())
            print ("result:"+str(result))
            self.ASSERT(result["isvalid"]==True, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###address_notexist
    def test_281_validateaddress(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().validateaddress(test_config.address_notexist)
            print ("result:"+str(result))
            self.ASSERT(result["isvalid"]==False, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###abc
    def test_283_validateaddress(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().validateaddress(test_config.wrong_str)
            print ("result:"+str(result))
            self.ASSERT(result["isvalid"]==False, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###""
    def test_284_validateaddress(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().validateaddress("")
            print ("result:"+str(result))
            self.ASSERT(result["isvalid"]==False, "")
        except AssertError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(False, "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(False, "")
            
    ###address不填
    def test_285_validateaddress(self):
        try:
            (status, info, climsg) = API.cli().exec(False)
            logger.print(climsg)
            self.ASSERT(status, info)
            result = API.rpc().validateaddress()
            print ("result:"+str(result))
            self.ASSERT(result["isvalid"]==False, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(json.loads(e.msg)["message"]=="Index was out of range. Must be non-negative and less than the size of the collection.\nParameter name: index", "")
        except Exception as e:
            logger.error(traceback.format_exc())
            self.ASSERT(True, "")


if __name__ == '__main__':
    unittest.main()
