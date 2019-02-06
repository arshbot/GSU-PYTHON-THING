import zmq
import requests
from time import sleep
from logs import print_welcome
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


class NodeManager:
    def __init__(self, zmq_url):
        self.zmq_url = zmq_url

        self.node_is_synced = False
        self.on_rawblock = None
        self.on_rawtx = None
        self.zmq_socket = None

        self.setup_subscriptions()
        print_welcome()

    def set_on_rawblock(self, processBlock):
        self.on_rawblock = processBlock

    def set_on_rawtx(self, processTx):
        self.on_rawtx = processTx

    def setup_subscriptions(self):
        context = zmq.Context()
        self.zmq_socket = context.socket(zmq.SUB)
        self.zmq_socket.setsockopt(zmq.SUBSCRIBE, b"rawtx")
        self.zmq_socket.setsockopt(zmq.SUBSCRIBE, b"rawblock")
        self.zmq_socket.connect(self.zmq_url)

    def listen_to_subscriptions(self):
        while True:
            topic, message, _ = self.zmq_socket.recv_multipart()
            if topic == b"rawtx":
                self.on_rawtx(message)
            elif topic == b"rawblock":
                try:
                    self.on_rawblock(message)
                except AssertionError:
                    return