# -*- coding:utf-8 -*-
import sys
import logging
import json
import numpy as np

sys.path.append('..')
sys.path.append('../src')

from utils.config import Config
from api.apimanager import API

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handle = logging.FileHandler("init_selfcheck.log", mode="w")
handle.setLevel(level=logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handle.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(level=logging.INFO)
console.setFormatter(formatter)

logger.addHandler(handle)
logger.addHandler(console)

np.set_printoptions(precision=16, suppress=True)
class SelfCheck():
    def __init__(self):
        pass

    def stop_nodes(self):
        for node_index in range(len(Config.NODES)):
            API.clirpc(node_index).terminate()

    def start_nodes(self):
        for node_index in range(len(Config.NODES)):
            API.clirpc(node_index).init()
            API.clirpc(node_index).exec(False)

    def clear_nodes(self):
        logger.info("----------------------------------")
        logger.info("begin clear nodes\n")
        for node_index in range(len(Config.NODES)):
            remotenodepath = Config.NODES[node_index]["path"].replace("neo-cli.dll", "")
            logger.info("begin clear " + str(node_index) + "\n")
            API.node(node_index).exec_cmd("rm -rf " + remotenodepath)
        logger.info("end clear nodes\n")

    def copy_node(self):
        logger.info("----------------------------------")
        logger.info("begin copy node\n")
        # remotenodelastfoldername = remotenodepath.split("/")[:-1]
        lastip = ""
        for node_index in range(len(Config.NODES)):
            logger.info("copy node[" + str(node_index) + "]\n")
            remotenodepath = Config.NODES[node_index]["path"].replace("neo-cli.dll", "")
            remotenodeprepath = "/".join(remotenodepath.split("/")[:-1])
            API.node(node_index).exec_cmd("mkdir -p " + remotenodeprepath)
            if lastip == Config.NODES[node_index]["ip"]:
                logger.info(lastip, "neo-cli.tar.gz has already exist...")
            else:
                logger.info("begin transfer file" + Config.RESOURCE_PATH + "/nodes/neo-cli.tar.gz" + "\n")
                API.node(node_index).exec_cmd("rm -rf " + "/root/neo-cli.tar.gz")
                API.node(node_index).sftp_transfer(Config.RESOURCE_PATH + "/nodes/neo-cli.tar.gz", "/root/neo-cli.tar.gz", node_index, "put")
                logger.info("end transfer file" + Config.RESOURCE_PATH + "/nodes/neo-cli.tar.gz" + "\n")
            API.node(node_index).exec_cmd("tar -xvf /root/neo-cli.tar.gz -C " + remotenodeprepath)
            # API.node(node_index).exec_cmd("mv " + remotenodeprepath + "/neo-cli " + remotenodepath)

            API.node(node_index).sftp_transfer(Config.RESOURCE_PATH + "/nodes/node" + str(node_index + 1) + "/config.json", remotenodepath, node_index, "put")
            API.node(node_index).sftp_transfer(Config.RESOURCE_PATH + "/nodes/node" + str(node_index + 1) + "/protocol.json", remotenodepath, node_index, "put")
            API.node(node_index).sftp_transfer(Config.RESOURCE_PATH + "/wallet/" + Config.NODES[node_index]["walletname"], remotenodepath, node_index, "put")
            lastip = Config.NODES[node_index]["ip"]
        logger.info("end copy node")
        logger.info("----------------------------------\n\n")

    def check_connected_nodes(self):
        logger.info("----------------------------------")
        logger.info("start checking connected node count\n")

        connected_node_count = API.rpc().getconnectioncount()
        if connected_node_count != len(Config.NODES) - 1:
            logger.error("connected node counts : %d, config node counts : %d" % (connected_node_count, len(Config.NODES) - 1))

        logger.info("checking connected node count OK")
        logger.info("----------------------------------\n\n")

    def check_all(self):
        # stop all nodes
        self.stop_nodes()
        self.clear_nodes()
        self.copy_node()
        self.start_nodes()
        self.check_connected_nodes()

def num2str(num):
        if num is not None or isinstance(num, int) or isinstance(num, float):
            return "num#!#start-%.20f-num#!#end" % num
        else:
            return num

if __name__ == "__main__":
    # get config
    # initconfig.get_init_config()
    jsonss = {"test": num2str(0.00000000001)}
    print(json.dumps(jsonss).replace("\"num#!#start-", "").replace("-num#!#end\"", ""))
    # print(": ", np.array([0.00000000001])[0])
    # str1 = "num:%.20f"%0.00000000001234
    # print(type(1111212121212121212121212121212))
    # start self check
    # selfcheck = SelfCheck()
    # selfcheck.check_all()
