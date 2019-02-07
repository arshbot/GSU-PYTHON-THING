def log_block(blockhash, our_txs, tx_count, DASHBOARD_BLOCK_COUNTER, DASHBOARD_TX_COUNTER, DASHBOARD_FAILED_COUNTER):
    # Clears dashboard
    print("\033[A                                           \033[A")
    print("\033[A                                           \033[A")

    # Print block
    print("         |         ")
    print("         |         ")
    print("+--------+--------+")
    print("|                 |")
    print("|                 |" + " Block hash: " + str(blockhash.hex()))
    print("|                 |" + " Total Txs: " + str(tx_count))
    print("|                 |")
    print("|                 |")
    print("|                 |")
    print("+--------+--------+")

    # Prints dashboard
    print("Total Blocks: " + str(DASHBOARD_BLOCK_COUNTER) + ", Failed Blocks: " + str(DASHBOARD_FAILED_BLOCK_COUNTER))
    print(
        "Total Txs Confirmed: "
        + str(DASHBOARD_TX_COUNTER)
        + ", Failed Txs: "
        + str(DASHBOARD_FAILED_COUNTER)
    )

def print_welcome():
        print(
            """
        
██████╗ ██╗      ██████╗  ██████╗██╗  ██╗ ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗    
██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██║  ██║██╔══██╗██║████╗  ██║    
██████╔╝██║     ██║   ██║██║     █████╔╝ ██║     ███████║███████║██║██╔██╗ ██║    
██╔══██╗██║     ██║   ██║██║     ██╔═██╗ ██║     ██╔══██║██╔══██║██║██║╚██╗██║    
██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗╚██████╗██║  ██║██║  ██║██║██║ ╚████║    
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    
                                                                                  
██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗                                   
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗                                  
██████╔╝█████╗  ███████║██║  ██║█████╗  ██████╔╝                                  
██╔══██╗██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗                                  
██║  ██║███████╗██║  ██║██████╔╝███████╗██║  ██║                                  
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                  
                                                                                                                              
                                                                                  

        """
        )
