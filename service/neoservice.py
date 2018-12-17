# -*- coding: utf-8 -*-

import leveldb
import hashlib
import socket
import json
import requests
import os
import setproctitle
import stat
import subprocess
import time

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
from config import Configure as config
from clicontroller import CLIController

setproctitle.setproctitle("test_service")

CLIController = CLIController()


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["start_process"] = CLIController.start_process
    dispatcher["version"] = CLIController.version

    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    print(request)
    responseobj = json.loads(response.json)
    print(responseobj)
    if "error" not in responseobj:
            responseobj["error"] = 0
    else:
        if "message" in responseobj["error"]:
            responseobj["desc"] = responseobj["error"]["message"]
        if "code" in responseobj["error"]:
            responseobj["error"] = responseobj["error"]["code"]
    print(json.dumps(responseobj))
    return Response(json.dumps(responseobj), mimetype='application/json')


if __name__ == '__main__':
        run_simple(get_host_ip(), config.PORT, application)
