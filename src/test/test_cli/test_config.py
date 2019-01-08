# -*- coding: utf-8 -*-
import sys
import time
sys.path.append('..')
configpath = os.path.dirname(os.path.realpath(__file__))

class test_config():
    wallet_name_json = "test.json"
    wallet_name_db3 = "test223.db3"
    wallet_name_db3_upgrade = "test223.json"
    wallet_name_nopws = "test666.db3"
    wallet_default = "wallet_5.json"
    wallet_default_address = "AHwmcxyxUva8Do8swvWeS2EkdUzhZ9JP7A"
    wallet_default_pubkey = "03ae5dddd3101c2a300f7066dc62df4bd5893036223fd0e4ef6569f19ccb6d8fab"
    wallet_name_wrong = "test223.txt"
    wallet_name_exist_wrong = "abcd.txt"	
    wallet_name_exist_erroecode_db3 = "¡Å.db3"
    wallet_name_exist_erroecode_json = "¡Å.json"
    wallet_name_null = "5_null.db3"
    wallet_password = "11111111"
    wallet_password_wrong = "22222222"
    wallet_name_notexist = "000test000.db3"
    address_default = "APfv5qVzrFKypZtH2J9fyNP7iWmtfBdaGL"
    address_default1 ="AchdSS7MhYCevUkXy6umBRaRVZzMfty5cV"
    asset_neo_id = "0xc56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b"
    asset_notexist_id = "0x025d82f7b00a9ff1cfe709abe3c4741a105d067178e645bc3ebad9bc79af47d4"
    asset_wrong_str_id = "abc"
    alias_right = "neo"
    alias_notexist = "oneo"
    pathname = "akey.txt"
    n_right = 100
    n_wrong_str = "abc"
    n_zero = 0
    wif_right = "L5bRK5eSEqppSnLN7T8wTKe7S1vnuLCgk6eFGpUHwUkjem7Jfa87"
    wif_address = "AYuKcz12thhVfQ6vQqVodMSvXFNFyn3Rx0"
    wif_notexist = "L4zRFphDJpLzXZzYrYKvUoz1LkhZprS5pTYywFqTJT2EcmWPPpPH"
    wif_wrong_str = "abc"
    path_right = "allkeys1.txt"
    path_notexist = "1allkeys1.txt"
    path_wrong = "abcd.sh"
    version = "2.9.3.0"
    
    
    
    
    
    wallet_default2="wallet_6.json"
    wallet_default3="7.json"
    wallet_default3address="APfv5qVzrFKypZtH2J9fyNP7iWmtfBdaGL"
    wallet_pwd="11111111"
    t = int(time.time())
    filename=str(t)+".txt"
    wrongfilename="abc.abc"
    key="L31rLw3AyK7PjMvioQHiVosbw64mvhwqhmPGZhhjbbxpdBDxXwEG"
    address_right="AHwmcxyxUva8Do8swvWeS2EkdUzhZ9JP7A"
    address_notexist = "AWg3L6W68bFfSS13Tf4rt8CRdG2ktaAjGb"
    asset_id_right="0xc56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b"
    asset_id_notexist = "025d82f7b00a9ff1cfe709abe3c4741a105d067178e645bc3ebad9bc79af47d4"
    wrong_str = "abc"
    wrong_int = 123
    filename2=str(t)+".acc"
    #¥”muti.jsonœÚwallet_5.json◊™1neo
    jsonObjectToSignWrong={"hex":"80000001fec6c339b9d255118a3d29cd7aa0f76c0eb168ab45cae1df9ceeee7ad175ee700000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500e1f50500000000f49c0482aa9d925399464d5cf2f2da1e454ed84c9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500e9a435000000009fbdd26490beec4cd3b5a7d50aff9865eb3b7c8c","items":{"0x4cd84e451edaf2f25c4d469953929daa82049cf4":{"script":"522102223b499165e11d29a490e6051d87e230af2cf44f081029d881fdf166fb2d96342103ae5dddd3101c2a300f7066dc62df4bd5893036223fd0e4ef6569f19ccb6d8fab52ae","parameters":[{"type":"Signature"},{"type":"Signature"}],"signatures":{"02223b499165e11d29a490e6051d87e230af2cf44f081029d881fdf166fb2d9634":"b97a12dd18f99878a7e5d969c08dbd5db21ac5990b86ffa4a3b6ef98388535bb4034b0a0a92c06f58864a3a4f574622b13241a815353177bffe904d8e901c463"}}}}
    copypath=configpath + "/resource/exportblocks/"
    mutiaddress="Ae5FRbhndo2XKRFqEQ9Mn99bRbeKqHLxWV"
    mutiname="muti.json"
    key1="021e5f82f1dac5f8662280e1e710b3a10e9c792ebd21fe31557354edd620b5d1b8"
    key2="032bbbc3dd52542af02af57927862a63faeab58c78d18d072b9d754646c3a65753"
    key3="037ebe29fff57d8c177870e9d9eecb046b27fc290ccbac88a0e3da8bac5daa630d"
    pass
