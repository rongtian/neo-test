# -*- coding:utf-8 -*-
import sys
import logging

sys.path.append('..')

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

    def copy_node(self):
        # remotenodelastfoldername = remotenodepath.split("/")[:-1]
        for node_index in range(len(Config.NODES)):
            remotenodepath = Config.NODES[0]["path"].replace("neo-cli.dll", "")
            remotenodeprepath = "/".join(remotenodepath.split("/")[:-1])
            API.clirpc().exec_cmd("mkdir -p " + remotenodeprepath)
            API.node(node_index).sftp_transfer(Config.RESOURCE_PATH + "/neo-cli.tar.gz", "/root/neo-cli.tar.gz", node_index)
            API.clirpc().exec_cmd("tar -xvf /root/neo-cli.tar.gz -C " + remotenodeprepath)
            API.clirpc().exec_cmd("mv " + remotenodeprepath + "/neo-cli " + remotenodepath)

            API.node(node_index).sftp_transfer(Config.RESOURCE_PATH + "/node" + str(node_index) + "/config.json", remotenodepath, node_index)
            API.node(node_index).sftp_transfer(Config.RESOURCE_PATH + "/node" + str(node_index) + "/protocol.json", remotenodepath, node_index)
            API.node(node_index).sftp_transfer(Config.RESOURCE_PATH + "/node" + str(node_index) + "/wallet.json", remotenodepath, node_index)

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
        self.copy_node()
        self.start_nodes()
        self.check_connected_nodes()


if __name__ == "__main__":
    # get config
    # initconfig.get_init_config()

    # start self check
    selfcheck = SelfCheck()
    selfcheck.check_all()
