from process_things import process_rawtx, process_rawblock
from node_manager import NodeManager
import os

from ptpdb import set_trace

controller = NodeManager(
        zmq_url=os.environ.get("ZMQ_URL"),
)

controller.set_on_rawtx(process_rawtx)
controller.set_on_rawblock(process_rawblock)
controller.listen_to_subscriptions()

# For some logging magic
print("")
print("")
