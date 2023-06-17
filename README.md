# Yashcoin ICO Smart Contract

This is the source code for the Yashcoin ICO smart contract, a cryptocurrency project created as part of the "Blockchain A-Z" course on Udemy. The smart contract is implemented in Solidity, a programming language specifically designed for writing smart contracts on the Ethereum platform.

# Overview
The Yashcoin ICO smart contract enables investors to participate in the initial coin offering (ICO) for Yashcoin by buying and selling Yashcoins using USD. The smart contract keeps track of the total supply of Yashcoins, the conversion rate between USD and Yashcoins, and the equity of each investor in terms of Yashcoins and USD.

# Functionality
__buy_yashcoins__: Allows investors to buy Yashcoins by providing the investor's address and the amount of USD they wish to invest. The function calculates the equivalent number of Yashcoins based on the current USD to Yashcoin conversion rate and updates the investor's equity accordingly.

__sell_yashcoins__: Allows investors to sell a specified amount of Yashcoins by providing the investor's address and the number of Yashcoins they wish to sell. The function deducts the sold Yashcoins from the investor's equity and updates their USD equity accordingly.

__equity_in_yashcoin__: Retrieves the current equity of an investor in terms of Yashcoins by providing the investor's address.

__equity_in_usd__: Retrieves the current equity of an investor in terms of USD by providing the investor's address.

# Deployment and Interactions
To deploy the Yashcoin ICO smart contract and interact with it, you can use Ethereum Wallet or any other Ethereum client that supports smart contract deployment and function interactions. Once deployed, you can interact with the smart contract using its address and ABI (Application Binary Interface) to call the available functions and monitor investor balances and equity.

# Credits
This project is based on the "Blockchain A-Z" course on Udemy, taught by Hadelin de Ponteves, Kirill Eremenko, SuperDatascience Team, Ligency Team. 
