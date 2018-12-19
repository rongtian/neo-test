# -*- coding:utf-8 -*-
import time
import subprocess
import threading
import os

# import utils.config


# 方法二：从Thread继承，并重写run()
class CLIReadThread(threading.Thread):
    def __init__(self, process):
        super(CLIReadThread, self).__init__()
        self.process = process
        self.readlines = None

    def readlines(self):
        return self.readlines

    def run(self):
        self.process.stdin.write("\n")
        self.readlines = self.process.stdout.readlines()


class CLIController:
    # version   显示当前软件的版本
    def __init__(self, scriptname):
        # step index
        self.stepindex = 0
        # step except functions
        self.stepexceptfuncs = {}
        # scripts folder
        self.prefixful = "cliscripts"
        self.scriptname = scriptname

        self.scriptpath = self.prefixful + "/" + scriptname + ".sh"
        if not os.path.exists(self.scriptpath):
            os.makedirs(self.scriptpath)

        self.neopath = "/root/neo/nodes/node5/neo-cli.dll"
        self.logfile = open(self.scriptpath, "w")  # 打开文件
        self.logfile.write("#!/usr/bin/expect\n")
        self.logfile.write("set timeout 3")
        self.logfile.write("spawn dotnet " + self.neopath + "\n")

    def writeline(self, str):
        self.logfile.write(str + "\n")

    def writesend(self, str):
        self.logfile.write("send \"" + str + "\"\\r" + "\n")
        pass

    def writeexcept(self, str):
        self.logfile.write("expect \"" + str + "\"" + "\n")
        pass

    def kill(self):
        os.system("kill -9 dotnet")

    def exec(self, exitatlast=True):
        if exit:
            self.exit()
        msg = ""
        process = subprocess.Popen("./" + self.scriptpath, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        while True:
            line = process.stdout.readline()
            if line != "":
                msg += line
            else:
                break

        msgblocks = {}
        lines = msg.split('\n')
        for line in lines:
            newblockindex = -1
            newblockname = ""
            if line.find("[START CLI COMMAND]") != -1:
                newblockindex = line.split('-')[2]
                newblockname = line.split('-')[1]
                continue
            elif line.find("[END CLI COMMAND]") != -1:
                newblockindex = -1
            else:
                if newblockindex != -1:
                    msgblock = msgblocks[newblockname + "-" + newblockindex]
                    if msgblock is None:
                        msgblock = ""
                    msgblock += line
                    msgblocks[newblockname + "-" + newblockindex] = msgblock

        for key in self.stepexceptfuncs.keys():
            exceptfunc = self.stepexceptfuncs[key]
            if exceptfunc is not None:
                print("compare step result: " + key)
                exceptret = False
                if key in msgblocks.keys():
                    exceptret = exceptfunc(msgblocks[key])
                else:
                    exceptret = exceptfunc(None)
                if not exceptret:
                    return (False, key, msg)
        return (True, "", msg)

    def version(self, exceptfunc=None):
        self.writesend("version")
        self.stepexceptfuncs["[version]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # help  帮助菜单
    def help(self, exceptfunc=None):
        self.writesend("help")
        self.stepexceptfuncs["[help]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # clear 清除屏幕
    def clear(self):
        self.writesend("clear")

    # exit  退出程序
    def exit(self):
        self.writesend("exit")

    # create wallet <path>  创建钱包文件
    def create_wallet(self, filepath, password, exceptfunc=None):
        self.writeline("echo '[START CLI COMMAND]-[create wallet]-" + str(self.stepindex) + "'")
        self.writesend("create wallet " + filepath)
        # input password
        self.writeexcept("*password:")
        self.writesend(password)
        # confirm password
        self.writeexcept("*password:")
        self.writesend(password)
        self.writeline("echo '[FINISH CLI COMMAND]-[create wallet]-" + str(self.stepindex) + "'")
        # register except function
        self.stepexceptfuncs["[create wallet]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # open wallet <path>    打开钱包文件
    def open_wallet(self, filepath, password, exceptfunc=None):
        self.writesend("open wallet " + filepath)
        # input password
        self.writeexcept("*password:")
        self.writesend(password)
        # register except function
        self.stepexceptfuncs["[open wallet]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # upgrade wallet <path> 升级旧版钱包文件
    def upgrade_wallet(self, filepath, exceptfunc=None):
        self.writesend("upgrade wallet " + filepath)
        # register except function
        self.stepexceptfuncs["[upgrade wallet]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # rebuild index 重建钱包索引  需要打开钱包
    # 重建钱包索引。为什么要重建钱包索引，重建钱包索引有什么用？
    # 钱包中有一个字段，记录了当前钱包同步的区块高度，每新增加一个区块，钱包客户端就会同步区块，
    # 将钱包中的资产和交易更新。假设当前记录的区块高度为 100，然后你执行了 import key 命令导入了私钥，
    # 这时钱包仍然是从区块高度为 100开始计算你的资产。如果导入的地址在区块高度小于 100的时候有一些交易，
    # 这些交易和对应的资产将不会体现在钱包中，所以要重建钱包索引，强制让钱包从区块高度为0开始计算你的资产。
    # 假如由于种种原因，钱包中的某笔交易未确认，这时资产已经从钱包中扣除，
    # 但并未经过整个区块链网络的确认。如果想删掉这笔未确认的交易使钱包中的资产正常显示也需要重建钱包索引。
    # 新创建的钱包不用重建钱包索引，只有要导入私钥或者钱包中资产显示异常时才需要重建钱包索引。
    def rebuild_index(self, exceptfunc=None):
        self.writesend("rebuild index")
        # register except function
        self.stepexceptfuncs["[rebuild index]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # list address  列出钱包中的所有账户  需要打开钱包
    def list_address(self, exceptfunc=None):
        self.writesend("list address")
        # register except function
        self.stepexceptfuncs["[list address]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # list asset    列出钱包中的所有资产  需要打开钱包
    def list_asset(self, exceptfunc=None):
        self.writesend("list asset")
        # register except function
        self.stepexceptfuncs["[list asset]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # list key  列出钱包中的所有公钥  需要打开钱包
    def list_key(self, exceptfunc=None):
        self.writesend("list key")
        # register except function
        self.stepexceptfuncs["[list key]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # show utxo [id|alias]  列出钱包中指定资产的 UTXO 需要打开钱包
    # examples:
    # 1. neo>show utxo neo
    #    8674c38082e59455cf35cee94a5a1f39f73b617b3093859aa199c756f7900f1f:2
    #    total: 1 UTXOs
    # 2. neo>show utxo gas
    #    8674c38082e59455cf35cee94a5a1f39f73b617b3093859aa199c756f7900f1f:1
    #    total: 1 UTXOs
    # 3. neo>show utxo 025d82f7b00a9ff1cfe709abe3c4741a105d067178e645bc3ebad9bc79af47d4
    #    8674c38082e59455cf35cee94a5a1f39f73b617b3093859aa199c756f7900f1f:0
    #    total: 1 UTXOs
    def show_utxo(self, id_alias=None, exceptfunc=None):
        if id_alias is None:
            self.writesend("show utxo")
        else:
            self.writesend("show utxo " + id_alias)
        # register except function
        self.stepexceptfuncs["[list key]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # show gas  列出钱包中的所有可提取及不可提取的 GAS   需要打开钱包
    # examples:
    # unavailable: 133.024
    # available: 10.123
    def show_gas(self, exceptfunc=None):
        self.writesend("show gas")
        # register except function
        self.stepexceptfuncs["[show gas]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # claim gas 提取钱包中的所有可提取的 GAS    需要打开钱包
    def claim_gas(self, exceptfunc=None):
        self.writesend("claim gas")
        # register except function
        self.stepexceptfuncs["[claim gas]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # create address [n=1]  创建地址 / 批量创建地址   需要打开钱包
    def create_address(self, n=None, exceptfunc=None):
        if n is None:
            self.writesend("create address")
        else:
            self.writesend("create address " + str(n))
        # register except function
        self.stepexceptfuncs["[create address]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # import key <wif|path> 导入私钥 / 批量导入私钥   需要打开钱包
    # examples:
    # import key L4zRFphDJpLzXZzYrYKvUoz1LkhZprS5pTYywFqTJT2EcmWPPpPH
    # import key key.txt
    def import_key(self, wif_path, exceptfunc=None):
        self.writesend("import key " + str(wif_path))
        # register except function
        self.stepexceptfuncs["[import key]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # export key [address] [path]   导出私钥    需要打开钱包
    # examples:
    # export key
    # export key AeSHyuirtXbfZbFik6SiBW2BEj7GK3N62b
    # export key key.txt
    # export key AeSHyuirtXbfZbFik6SiBW2BEj7GK3N62b key.txt
    def export_key(self, address=None, path=None, exceptfunc=None):
        addressstr = ""
        pathstr = ""
        if address is not None:
            addressstr = address
        if path is not None:
            pathstr = path
        self.writesend("export key " + str(addressstr) + " " + str(pathstr))
        # register except function
        self.stepexceptfuncs["[export key]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # send <id|alias> <address> <value>|all [fee=0] 向指定地址转账 参数分别为：资产 ID，对方地址，转账金额，手续费   需要打开钱包
    # examples:
    # 1. send c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b AeSHyuirtXbfZbFik6SiBW2BEj7GK3N62b 100
    # 2. send neo AeSHyuirtXbfZbFik6SiBW2BEj7GK3N62b 100
    def send(self, id_alias, address, value, fee=0, exceptfunc=None):
        self.writesend("send " + str(id_alias) + " " + str(address) + " " + str(value) + " " + str(fee))
        # register except function
        self.stepexceptfuncs["[send]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # import multisigaddress m pubkeys...   创建多方签名合约    需要打开钱包
    # examples:
    # import multisigaddress 1 037ebe29fff57d8c177870e9d9eecb046b27fc290ccbac88a0e3da8bac5daa630d 03b34a4be80db4a38f62bb41d63f9b1cb664e5e0416c1ac39db605a8e30ef270cc
    def import_multisigaddress(self, m, pubkeys, exceptfunc=None):
        self.writesend("import multisigaddress " + str(m) + " " + " ".join(pubkeys))
        # register except function
        self.stepexceptfuncs["[import multisigaddress]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # sign <jsonObjectToSign>   签名 参数为：记录交易内容的 json 字符串 需要打开钱包
    def sign(self, jsonobj, exceptfunc=None):
        self.writesend("sign " + jsonobj)
        # register except function
        self.stepexceptfuncs["[sign]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # relay <jsonObjectToSign>  广播 参数为：记录交易内容的 json 字符串 需要打开钱包
    def relay(self, jsonobj, exceptfunc=None):
        self.writesend("relay " + jsonobj)
        # register except function
        self.stepexceptfuncs["[relay]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # show state    显示当前区块链同步状态
    def show_state(self, exceptfunc=None):
        self.writesend("show state")
        # register except function
        self.stepexceptfuncs["[show state]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # show node 显示当前已连接的节点地址和端口
    def show_node(self, exceptfunc=None):
        self.writesend("show node")
        # register except function
        self.stepexceptfuncs["[show node]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # show pool 显示内存池中的交易（这些交易处于零确认的状态）
    def show_pool(self, exceptfunc=None):
        self.writesend("show pool")
        # register except function
        self.stepexceptfuncs["[show pool]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # export blocks [path=chain.acc]    导出全部区块数据，导出的结果可以用作离线同步
    def export_all_blocks(self, path=None, exceptfunc=None):
        if path is None:
            self.writesend("export blocks")
        else:
            self.writesend("export blocks " + path)
        # register except function
        self.stepexceptfuncs["[export blocks]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # export blocks <start> [count] 从指定区块高度导出指定数量的区块数据，导出的结果可以用作离线同步
    def export_blocks(self, start, count=None, exceptfunc=None):
        if count is None:
            self.writesend("export blocks " + str(start))
        else:
            self.writesend("export blocks " + str(start) + " " + str(count))
        # register except function
        self.stepexceptfuncs["[export blocks]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1

    # start consensus   启动共识
    def start_consensus(self, exceptfunc=None):
        self.writesend("start consensus")
        # register except function
        self.stepexceptfuncs["[start consensus]-" + str(self.stepindex)] = exceptfunc
        self.stepindex += 1
