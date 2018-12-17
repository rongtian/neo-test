# -*- coding:utf-8 -*-
import time
import subprocess

# import utils.config


class CLIApi:
    # version	显示当前软件的版本
    def __init__(self):
        self.PROCESS = None

    def start_process(self, nodepath):
        self.PROCESS = subprocess.Popen("dotnet " + nodepath, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def check_process(self):
        if self.PROCESS is None:
            raise "no neo-cli process raised, please call 'start(nodepath)' first...."
        self.PROCESS.stdout.flush()
        self.PROCESS.stdout.clear()

    def write_process(self, cmd):
        print("cli cmd: " + cmd)
        self.PROCESS.stdin.write(cmd + "\n")

    def read_process(self, timeout=3):
        lines = []
        waitsec = 0
        while True:
            line = self.PROCESS.stdout.readlines()
            lines.append(line)
            if lines is not None:
                break
            else:
                if waitsec >= 3:
                    raise "read neo-cli process timeout: " + timeout
                time.sleep(1)
                waitsec = waitsec + 1
        return lines

    def version(self):
        self.check_process()
        self.write_process("version")
        lines = self.read_process()
        return lines

    # help	帮助菜单
    def help(self):
        self.check_process()
        self.write_process("help")
        lines = self.read_process()
        return lines

    # clear	清除屏幕
    def clear(self):
        self.check_process()
        self.write_process("clear")
        return True

    # exit	退出程序
    def exit(self):
        self.check_process()
        self.write_process("exit")
        return True

    # create wallet <path>	创建钱包文件
    def create_wallet(self, filepath):
        self.check_process()
        self.write_process("create wallet " + filepath)
        lines = self.read_process()
        return lines

    # open wallet <path>	打开钱包文件
    def open_wallet(self, filepath):
        self.check_process()
        self.write_process("open wallet " + filepath)
        lines = self.read_process()
        return lines

    # upgrade wallet <path>	升级旧版钱包文件
    def upgrade_wallet(self, filepath):
        self.check_process()
        self.write_process("upgrade wallet " + filepath)
        lines = self.read_process()
        return lines

    # rebuild index	重建钱包索引	需要打开钱包
    # 重建钱包索引。为什么要重建钱包索引，重建钱包索引有什么用？
    # 钱包中有一个字段，记录了当前钱包同步的区块高度，每新增加一个区块，钱包客户端就会同步区块，
    # 将钱包中的资产和交易更新。假设当前记录的区块高度为 100，然后你执行了 import key 命令导入了私钥，
    # 这时钱包仍然是从区块高度为 100开始计算你的资产。如果导入的地址在区块高度小于 100的时候有一些交易，
    # 这些交易和对应的资产将不会体现在钱包中，所以要重建钱包索引，强制让钱包从区块高度为0开始计算你的资产。
    # 假如由于种种原因，钱包中的某笔交易未确认，这时资产已经从钱包中扣除，
    # 但并未经过整个区块链网络的确认。如果想删掉这笔未确认的交易使钱包中的资产正常显示也需要重建钱包索引。
    # 新创建的钱包不用重建钱包索引，只有要导入私钥或者钱包中资产显示异常时才需要重建钱包索引。
    def rebuild_index(self, filepath):
        self.check_process()
        self.write_process("rebuild wallet " + filepath)
        lines = self.read_process()
        return lines

    # list address	列出钱包中的所有账户	需要打开钱包
    def list_address(self):
        self.check_process()
        self.write_process("list address")
        lines = self.read_process()
        return lines

    # list asset	列出钱包中的所有资产	需要打开钱包
    def list_asset(self):
        self.check_process()
        self.write_process("list asset")
        lines = self.read_process()
        return lines

    # list key	列出钱包中的所有公钥	需要打开钱包
    def list_key(self):
        self.check_process()
        self.write_process("list key")
        lines = self.read_process()
        return lines

    # show utxo [id|alias]	列出钱包中指定资产的 UTXO	需要打开钱包
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
    def show_utxo(self, id_alias=None):
        self.check_process()
        self.write_process("show utxo " + id_alias)
        lines = self.read_process()
        return lines

    # show gas	列出钱包中的所有可提取及不可提取的 GAS	需要打开钱包
    # examples:
    # unavailable: 133.024
    # available: 10.123
    def show_gas(self):
        self.check_process()
        self.write_process("show gas")
        lines = self.read_process()
        return lines

    # claim gas	提取钱包中的所有可提取的 GAS	需要打开钱包
    def claim_gas(self):
        self.check_process()
        self.write_process("claim gas")
        lines = self.read_process()
        return lines

    # create address [n=1]	创建地址 / 批量创建地址	需要打开钱包
    def create_address(self, n=None):
        self.check_process()
        if n is None:
            self.write_process("create address")
        else:
            self.write_process("create address " + n)
        lines = self.read_process()
        return lines

    # import key <wif|path>	导入私钥 / 批量导入私钥	需要打开钱包
    # examples:
    # import key L4zRFphDJpLzXZzYrYKvUoz1LkhZprS5pTYywFqTJT2EcmWPPpPH
    # import key key.txt
    def import_key(self, wif_path):
        self.check_process()
        self.write_process("import key " + wif_path)
        lines = self.read_process()
        return lines

    # export key [address] [path]	导出私钥	需要打开钱包
    # examples:
    # export key
    # export key AeSHyuirtXbfZbFik6SiBW2BEj7GK3N62b
    # export key key.txt
    # export key AeSHyuirtXbfZbFik6SiBW2BEj7GK3N62b key.txt
    def export_key(self, address=None, path=None):
        self.check_process()
        cmd = "export key"
        if address is not None:
            cmd = " " + address
        if path is not None:
            cmd = " " + path
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # send <id|alias> <address> <value>|all [fee=0]	向指定地址转账 参数分别为：资产 ID，对方地址，转账金额，手续费	需要打开钱包
    # examples:
    # 1. send c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b AeSHyuirtXbfZbFik6SiBW2BEj7GK3N62b 100
    # 2. send neo AeSHyuirtXbfZbFik6SiBW2BEj7GK3N62b 100
    def send(self, id_alias, address, value, fee=0):
        self.check_process()
        cmd = "send " + id_alias + " " + address + " " + value
        if fee is not None:
            cmd = " " + fee
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # import multisigaddress m pubkeys...	创建多方签名合约	需要打开钱包
    # examples:
    # import multisigaddress 1 037ebe29fff57d8c177870e9d9eecb046b27fc290ccbac88a0e3da8bac5daa630d 03b34a4be80db4a38f62bb41d63f9b1cb664e5e0416c1ac39db605a8e30ef270cc
    def import_multisigaddress(self, m, pubkeys):
        self.check_process()
        cmd = "import multisigaddress " + m + " " + pubkeys
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # sign <jsonObjectToSign>	签名 参数为：记录交易内容的 json 字符串	需要打开钱包
    def sign(self, jsonobj):
        self.check_process()
        cmd = "sign " + jsonobj
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # relay <jsonObjectToSign>	广播 参数为：记录交易内容的 json 字符串	需要打开钱包
    def relay(self, jsonobj):
        self.check_process()
        cmd = "relay " + jsonobj
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # show state	显示当前区块链同步状态
    def show_state(self):
        self.check_process()
        cmd = "show state"
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # show node	显示当前已连接的节点地址和端口
    def show_node(self):
        self.check_process()
        cmd = "show node"
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # show pool	显示内存池中的交易（这些交易处于零确认的状态）
    def show_pool(self):
        self.check_process()
        cmd = "show pool"
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # export blocks [path=chain.acc]	导出全部区块数据，导出的结果可以用作离线同步
    def export_all_blocks(self, path=None):
        self.check_process()
        cmd = "export blocks"
        if path is not None:
            cmd = " " + path
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # export blocks <start> [count]	从指定区块高度导出指定数量的区块数据，导出的结果可以用作离线同步
    def export_blocks(self, start, count=None):
        self.check_process()
        cmd = "export blocks " + start
        if count is not None:
            cmd = " " + count
        self.write_process(cmd)
        lines = self.read_process()
        return lines

    # start consensus	启动共识
    def start_consensus(self):
        self.check_process()
        cmd = "start start_consensus"
        self.write_process(cmd)
        lines = self.read_process()
        return lines
