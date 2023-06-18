# YASHCOIN

YASHCOIN is a decentralized cryptocurrency built using Python and Flask. It implements a blockchain network with proof of work consensus algorithm. This project was created as part of the Blockchain A-Z course on Udemy.

# Features

Creation and mining of new blocks
Adding transactions to the blockchain
Consensus protocol to ensure all nodes have the same chain
Web-based interface using Flask
Integration with Postman for testing
Getting Started

# To run the YASHCOIN application, follow the steps below:

1. Clone the repository to your local machine.
2. Run the blockchain nodes on different ports:
1. Node 1: python yashcoin_node_5001.py
2. Node 2: python yashcoin_node_5002.py
3. Node 3: python yashcoin_node_5003.py
4. Use Postman or any other API testing tool to send requests to the blockchain nodes.
API Endpoints

# Mine a new block
1. URL: http://localhost:5001/mine_block
2. Method: GET
3. Description: Mines a new block and adds it to the blockchain.

# Get the full blockchain
1. URL: http://localhost:5001/get_chain
2. Method: GET
3. Description: Retrieves the entire blockchain.

# Check blockchain validity
1. URL: http://localhost:5001/is_valid
2. Method: GET
3. Description: Checks if the blockchain is valid.

# Add a transaction
1. URL: http://localhost:5001/add_transaction
2. Method: POST
3. Description: Adds a transaction to the blockchain. Requires a JSON payload with 'sender', 'receiver', and 'amount' fields.


# Connect new nodes
1. URL: http://localhost:5001/connect_node
2. Method: POST
3. Description: Connects new nodes to the blockchain network. Requires a JSON payload with a 'nodes' array containing the addresses of the new nodes.

# Replace the blockchain
1. URL: http://localhost:5001/replace_chain
2. Method: GET
3. Description: Requests all nodes in the network to update their chains to the most up-to-date one.

# Acknowledgments

I would like to thank the creators of the Blockchain A-Z course on Udemy for providing the foundation for this project
