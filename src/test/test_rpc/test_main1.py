# -*- coding:utf-8 -*-
import unittest
import os
import sys
import traceback

sys.path.append('..')
sys.path.append('../..')
testpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(testpath)

from utils.logger import LoggerInstance as logger
from utils.parametrizedtestcase import ParametrizedTestCase
from utils.error import AssertError, RPCError
from api.apimanager import API
from neo.wallet import Wallet, Account
from utils.config import Config

######################################################
# test cases
class test_rpc_1(ParametrizedTestCase):
    def setUp(self):
        logger.open("test_rpc/" + self._testMethodName + ".log", self._testMethodName)

    def tearDown(self):
        logger.close(self.result())

    def test_01_dumpprivkey(self):
        try:
            result = API.rpc().dumpprivkey(Config.NODES[0]["wallet"].account().address())
            self.ASSERT(result is "", "privkey not match")
        except AssertError as e:
            logger.error(e.msg)
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_02_getaccountstate(self):
        try:
            result = API.rpc().getaccountstate(Config.NODES[0]["wallet"].account().address())
            self.ASSERT(result, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_03_getassetstate(self):
        try:
            result = API.rpc().getaccountstate("c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b")
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_04_getbalance(self):
        try:
            result = API.rpc().getbalance("c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b")
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_05_getbestblockhash(self):
        try:
            result = API.rpc().getbestblockhash()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_06_getblock(self):
        try:
            bestblockhash = API.rpc().getbestblockhash()
            result = API.rpc().getblock(bestblockhash, 1)
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_07_getblockcount(self):
        try:
            result = API.rpc().getblockcount()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_08_getblockheader(self):
        try:
            bestblockhash = API.rpc().getbestblockhash()
            result = API.rpc().getblockheader(bestblockhash, 1)
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_09_getblockhash(self):
        try:
            result = API.rpc().getblockhash(1)
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_10_getblocksysfee(self):
        try:
            result = API.rpc().getblocksysfee(1)
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_11_getconnectioncount(self):
        try:
            result = API.rpc().getconnectioncount()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_12_getcontractstate(self):
        try:
            result = API.rpc().getcontractstate("dc675afc61a7c0f7b3d2682bf6e1d8ed865a0e5f")
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_13_getnewaddress(self):
        try:
            result = API.rpc().getnewaddress()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_14_getrawmempool(self):
        try:
            result = API.rpc().getrawmempool()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_15_getrawtransaction(self):
        try:
            result = API.rpc().getrawtransaction("f4250dab094c38d8265acc15c366dc508d2e14bf5699e12d9df26577ed74d657")
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_16_getstorage(self):
        try:
            result = API.rpc().getstorage("f4250dab094c38d8265acc15c366dc508d2e14bf5699e12d9df26577ed74d657", "key")
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_17_gettxout(self):
        try:
            result = API.rpc().gettxout("f4250dab094c38d8265acc15c366dc508d2e14bf5699e12d9df26577ed74d657")
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_18_getpeers(self):
        try:
            result = API.rpc().getpeers()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_19_getvalidators(self):
        try:
            result = API.rpc().getvalidators()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_20_getversion(self):
        try:
            result = API.rpc().getversion()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_21_getwalletheight(self):
        try:
            result = API.rpc().getwalletheight()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_22_invoke(self):
        try:
            result = API.rpc().invoke("", [])
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_23_invokefunction(self):
        try:
            result = API.rpc().invokefunction("", "function", [])
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_24_invokescript(self):
        try:
            result = API.rpc().invokescript("f4250dab094c38d8265acc15c366dc508d2e14bf5699e12d9df26577ed74d657")
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_25_listaddress(self):
        try:
            result = API.rpc().listaddress()
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_26_sendfrom(self):
        try:
            result = API.rpc().sendfrom("c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b",
                Config.NODES[0]["wallet"].account().address(),
                Config.NODES[1]["wallet"].account().address(), 100)
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_27_sendrawtransaction(self):
        try:
            result = API.rpc().sendrawtransaction("f4250dab094c38d8265acc15c366dc508d2e14bf5699e12d9df26577ed74d657")
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_28_sendtoaddress(self):
        try:
            result = API.rpc().sendtoaddress("c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b",
                Config.NODES[0]["wallet"].account().address(), 100)
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_29_sendmany(self):
        try:
            result = API.rpc().sendmany([])
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())

    def test_30_validateaddress(self):
        try:
            result = API.rpc().validateaddress(Config.NODES[1]["wallet"].account().address())
            self.ASSERT(result, "")
        except AssertError as e:
            logger.error(e.msg)
        except RPCError as e:
            logger.error(e.msg)
            self.ASSERT(True, "")
        except Exception as e:
            logger.error(traceback.format_exc())


if __name__ == '__main__':
    unittest.main()
