 git clone https://github.com/bitcoin/bitcoin
 cd bitcoin

./autogen.sh
./configure --disable-wallet
make

# Now we have a crypto node
# Start

./src/bitcoind -testnet -txindex=0 -server -maxconnections=10 -zmqpubrawblock=tcp://127.0.0.1:28332 -zmqpubrawtx=tcp://127.0.0.1:28332 -prune=550

# Let our precious sync

# if you don't have python 3.0+ figure that out

# Create a new project fodler for files

touch logs.py nodemanager.py start.py



