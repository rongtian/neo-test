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
from neo.walletmanager import WalletManager
from neo.wallet import Wallet, Account


######################################################
# test cases
class test_cli(ParametrizedTestCase):
    def setUp(self):
        logger.open("test_rpc/" + self._testMethodName + ".log", self._testMethodName)

    def tearDown(self):
        logger.close(self.result())

    def test_01_dumpprivkey(self):
        pass


if __name__ == '__main__':
    unittest.main()
