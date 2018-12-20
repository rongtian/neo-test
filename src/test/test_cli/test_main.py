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

	
	'''
	def test_01_createwallet(self):
		try:
			self.clicon.create_wallet("test.json", "11111111", lambda msg: msg.find("address"))
			(result, stepname, msg) = self.clicon.exec()
			print(msg)
			self.ASSERT(result, "create wallet failed")
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())

	def test_02_openwallet(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			(result, stepname, msg) = self.clicon.exec()
			print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_03_upgradewallet(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.upgrade_wallet("test2.json")
			self.clicon.list_address()
			(result, stepname, msg) = self.clicon.exec()
			print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_04_rebuildindex(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.upgrade_wallet("test2.json")
			self.clicon.rebuild_index()
			(result, stepname, msg) = self.clicon.exec()
			print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_05_list(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.list_asset()
			self.clicon.list_key()
			(result, stepname, msg) = self.clicon.exec()
			print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_06_showutxo(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.show_utxo()
			(result, stepname, msg) = self.clicon.exec()
			print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_07_showgas(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.show_gas()
			(result, stepname, msg) = self.clicon.exec()
			print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_08_claimgas(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.claim_gas()
			(result, stepname, msg) = self.clicon.exec()
			print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	
	def test_09_createaddress(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.create_address()
			self.clicon.list_address()
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_10_importkey(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.import_key("L4zRFphDJpLzXZzYrYKvUoz1LkhZprS5pTYywFqTJT2EcmWPPpPH")
			self.clicon.list_address()
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())

	
	def test_11_exportkey(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.export_key("11111111", None, "allkeys.txt")
			self.clicon.list_address()
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_12_send(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.list_address()
			self.clicon.send("11111111", "c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b", "AeSHyuirtXbfZbFik6SiBW2BEj7GK3N62b", 100)
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	

	def test_13_importmultisigaddress(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.import_multisigaddress(1, ["037ebe29fff57d8c177870e9d9eecb046b27fc290ccbac88a0e3da8bac5daa630d", "03b34a4be80db4a38f62bb41d63f9b1cb664e5e0416c1ac39db605a8e30ef270cc"])
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_14_sign(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.sign("{\"key\" : \"037ebe29fff57d8c177870e9d9eecb046b27fc290ccbac88a0e3da8bac5daa630d\"}")
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_15_relay(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.relay("{\"key\" : \"037ebe29fff57d8c177870e9d9eecb046b27fc290ccbac88a0e3da8bac5daa630d\"}")
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_16_showstate(self):
		try:
			self.clicon.show_state(5)
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_17_shownode(self):
		try:
			self.clicon.show_node()
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())	
	
	def test_18_shownode(self):
		try:
			self.clicon.show_pool()
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())		
	
	def test_19_exportallblocks(self):
		try:
			self.clicon.export_all_blocks("chain.acc")
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
	def test_20_exportblocks(self):
		try:
			self.clicon.export_blocks(0, 100)
			(result, stepname, msg) = self.clicon.exec()
			logger.print(msg)
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	'''
	def test_21_startconsensus(self):
		try:
			self.clicon.open_wallet("test.json", "11111111")
			self.clicon.start_consensus()
			(result, stepname, msg) = self.clicon.exec(False)
			logger.print(msg)
			self.clicon.terminate()
		except AssertError as e:
			logger.error(e.msg)
		except Exception as e:
			logger.error(traceback.format_exc())
	
if __name__ == '__main__':
	unittest.main()
