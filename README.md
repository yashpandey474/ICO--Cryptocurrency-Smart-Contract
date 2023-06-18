# Yashcoin ICO, Cryptocurrency, and Blockchain Project

This project combines the Yashcoin ICO smart contract, YASHCOIN cryptocurrency, and a basic implementation of a blockchain. It enables investors to participate in the Yashcoin initial coin offering (ICO), buy and sell Yashcoins using USD, and utilizes a blockchain network with a proof of work consensus algorithm.

## Features

- **Yashcoin ICO Smart Contract:** Investors can buy and sell Yashcoins using USD, while the smart contract keeps track of the total supply of Yashcoins, the conversion rate between USD and Yashcoins, and the equity of each investor in terms of Yashcoins and USD.

- **YASHCOIN Cryptocurrency:** Implements a decentralized cryptocurrency built using Python and Flask. It supports the creation and mining of new blocks, adding transactions to the blockchain, and implements a consensus protocol to ensure all nodes have the same chain.

- **Basic Blockchain Implementation:** Provides a basic blockchain implementation using Python and Flask. It includes functionalities such as mining new blocks, retrieving the full blockchain, and checking blockchain validity.

## Installation

To set up the combined project, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies for the YASHCOIN cryptocurrency and basic blockchain implementation. You may use the provided `requirements.txt` file.
3. Run the Yashcoin ICO smart contract by following the specific instructions provided in the respective repository.
4. Start the YASHCOIN cryptocurrency nodes on different ports by running the corresponding Python scripts.
5. Use an API testing tool like Postman to interact with the blockchain nodes by sending requests to the specified API endpoints.

## Usage

Here are some key interactions and functionalities available in the project:

- **Yashcoin ICO Smart Contract**
  - Use the `buy_yashcoins` function to buy Yashcoins by providing your address and the amount of USD you wish to invest.
  - Use the `sell_yashcoins` function to sell a specified amount of Yashcoins by providing your address and the number of Yashcoins you wish to sell.
  - Retrieve your current equity in terms of Yashcoins using the `equity_in_yashcoin` function.
  - Retrieve your current equity in terms of USD using the `equity_in_usd` function.

- **YASHCOIN Cryptocurrency**
  - Mine new blocks by sending a GET request to the `mine_block` endpoint.
  - Retrieve the full blockchain by sending a GET request to the `get_chain` endpoint.
  - Check blockchain validity by sending a GET request to the `is_valid` endpoint.
  - Add a transaction by sending a POST request to the `add_transaction` endpoint with the required payload.
  - Connect new nodes to the network by sending a POST request to the `connect_node` endpoint with the list of node addresses.
  - Update all nodes' chains to the most up-to-date one by sending a GET request to the `replace_chain` endpoint.

## File Organization

The project directory is organized as follows:

- yashcoin_ico
- yashcoin_cryptocurrency
- create_blockchain
- README.md
Each subdirectory contains the files specific to the ICO, cryptocurrency, and blockchain components, respectively.

## Credits
This project is based on the "Blockchain A-Z" course on Udemy, taught by Hadelin de Ponteves, Kirill Eremenko, SuperDatascience Team, Ligency
