from blockchain_parser.utils import decode_varint
from bitcoinlib.transactions import Transaction

DASHBOARD_BLOCK_COUNTER = 0
DASHBOARD_TX_COUNTER = 0 
DASHBOARD_FAILED_COUNTER = 0

def process_rawtx(raw):
    return

def process_rawblock(raw):
    global DASHBOARD_BLOCK_COUNTER, DASHBOARD_TX_COUNTER, DASHBOARD_FAILED_COUNTER
    DASHBOARD_BLOCK_COUNTER += 1
    block_header = raw[:80]
    block = raw[80:]
    version = block_header[:4]
    prev_merkle_root = block_header[4:36]
    merkle_root = block_header[36:68]

    blockhash = calculate_id(block_header)

    tx_count = 0 

    transaction_data = raw_hex[80:]

    # Decoding the number of transactions, offset is the size of
    # the varint (1 to 9 bytes)
    n_transactions, offset = decode_varint(transaction_data)

    
    for i in range(n_transactions):
        transaction = Transaction.import_raw(transaction_data[offset:])
        offset += transaction.size

    # for rawtx in get_block_transactions(raw):
    #     tx_count += 1
    #     print(rawtx)

    
    log_block(blockhash, txs, tx_count, DASHBOARD_BLOCK_COUNTER, DASHBOARD_TX_COUNTER, DASHBOARD_FAILED_COUNTER)
    return

def calculate_id(raw):
    # Double sha of raw in big endian
    return sha256(sha256(raw).digest()).digest()[::-1]