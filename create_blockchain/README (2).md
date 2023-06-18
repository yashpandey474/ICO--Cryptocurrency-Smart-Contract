# Create-Blockchain

This is a basic implementation of a blockchain using Python and Flask. It was developed as part of the "Blockchain A-Z" course on Udemy. The blockchain can be interacted with using Postman to send HTTP requests to the Flask web application.

## Prerequisites

- Python 3.x
- Flask
- Postman

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
Install the required dependencies:

bash
Copy code
pip install flask
Start the Flask application:

bash
Copy code
python3 blockchain.py
The application will be running at http://0.0.0.0:5002.

Available Endpoints
Mine a New Block

Method: GET
URL: http://localhost:5002/mine_block
This endpoint triggers the mining process, solving the proof of work problem and creating a new block. It returns information about the mined block.

Get the Full Blockchain

Method: GET
URL: http://localhost:5002/get_chain
This endpoint returns the full blockchain and its length.

Check Blockchain Validity

Method: GET
URL: http://localhost:5002/is_valid
This endpoint checks the validity of the blockchain by verifying the previous hash and proof of work for each block.

Credits
This project was developed based on the "Blockchain A-Z" course on Udemy by Hadelin de Ponteves, Kirill Eremenko, SuperDatascience Team, Ligency Team. 
