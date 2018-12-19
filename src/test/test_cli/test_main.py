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
from api.clicontroller import CLIController

######################################################
# test cases
class test_cli(ParametrizedTestCase):
    def setUp(self):
        self.clicon = CLIController(self._testMethodName)
        logger.open("test_cli/" + self._testMethodName + ".log", self._testMethodName)

    def tearDown(self):
        logger.close(self.result())

    def test_01_createwallet(self):
        try:
            self.clicon.create_wallet("test.json", "111111")
        except AssertError as e:
            logger.error(e.msg)
        except Exception as e:
            logger.error(traceback.format_exc())


if __name__ == '__main__':
    unittest.main()
