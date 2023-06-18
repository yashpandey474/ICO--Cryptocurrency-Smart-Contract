#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 00:02:58 2023

@author: kpandey

MODULE 2: CREATE A CRYPTOCURRENCY
"""

#NEED A WEB BASED BLOCKCHAIN: FLASK
#USER-FRIENDLY INTERFACE: POSTMAN


#IMPORTING THE LIBRARIES
import  datetime #TIMESTAMP OF BLOCK
import hashlib #HASH OF BLOCK
import json #RETURN DATA ABOUT BLOCK
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse

##1. ADDING TRANSACTIONS
##2. MAKING THE CONSENSUS PROTOCOL



#PART 1 - BUILDING A BLOCKCHAIN



#PART 2  - MINE NEW BLOCKS FOR SOME TRANSACTIONS



#PART 3 - DECENTRALISING THE BLOCKCHAIN




#OPTION1: MAKE SEVERAL FUNCTIONS
#OPTION2: WITH A CLASS: BEST OPTION

#PART 1 - BUILDING A BLOCKCHAIN
class Blockchain:
    
    #COMPONENTS OF BLOCKCHAIN
    
    def __init__(self): #ALWAYS TAKES IN SELF AS ARGUMENT
        #INITIALISE THE CHAIN TO CONTAIN BLOCKS #EMPTY LIST
        self.chain = []
        
        
        #TRANSACTIONS; ONLY PUT IN BLOCK WHEN MINED
        self.transactions = [] #BEFORE CREATE BLOCK
        
        #GENESIS BLOCK
        self.create_block(proof = 1, previous_hash = '0') #PROOF AND PREVIOUS HASH

        #ADD NODES
        self.nodes = set()

        #DIFFERENCE BETWEEN CREATE BLOCK AND MINE BLOCK
        #MINE GETS PROOF OF WORK AND THEN CALL CREATE BLOCK
        
    def create_block(self, proof, previous_hash):
        
        #NEW BLOCK: DICTIONARY!
        block = {'index': len(self.chain)+1, 
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions #ALL CURRENT TRANSACTIONS
                 }
        
        #TRANSACTIONS ADDED TO A BLOCK
        self.transactions = []
        
        #ADD IT TO CHAIN
        self.chain.append(block)
        
        #RETURN THE BLOCK
        return block
    
    def get_previous_block(self):
        
        return self.chain[-1]
    
    
    #PROOF OF WORK: WHAT THE MINERS HAVE TO FIND AND SOLVE
    #CHALLENGING TO SOLVE, EASY TO VERIFY
    
    def proof_of_work(self, previous_proof):
        
        new_proof = 1 #INCREMENTED UNTIL PROBLEM SOLVED
        check_proof = False #TRUE WHEN SOLUTION FOUND
        
        while (check_proof is False):
            
            #PROBLEM:  4 LEADING ZEROES IN HASH [SIMPLE]
            
            #64 CHARACTER STRING: encode adds b before string
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest() #NON-SYMMETRICAL OPERATION
            
            #EXPECTED FORMAT
            if hash_operation[:4] == '0000':
                #MINER WINS!
                check_proof = True
                
            else:
                #INCREMENT NEW PROOF
                new_proof+=1
    
        return new_proof
    
    #HASH FUNCTION: HASH EACH BLOCK
    def hash(self, block):
        
        #CONVERT DICTIONARY TO STRING
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    #CHECK BLOCKCHAIN: 
    #1. EACH BLOCK HAS CORRECT PROOF_OF_WORK,
    #2. PREVIOUS HASH MATCHES OF EACH BLOCK
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1 #IN DICTIONARY
        
        while(block_index < len(chain)):
            
            #CURRENT BLOCK
            block = chain[block_index]
            
            #PREVIOUS HASH CHECK
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            #PROOF OF WORK
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest() #NON-SYMMETRICAL OPERATION
            
            if hash_operation[:4] !='0000':
                return False
            
            #UPDATE VARIABLES
            previous_block = block
            block_index += 1
            
        return True
    
    #1. ADD TRANSACTION
    def add_transaction(self, sender, receiver, amount):
        self.transactions.append(
            {'sender':sender,
             'receiver': receiver,
             'amount': amount
                }
        )
        #INDEX OF BLOCK CONTAINING THIS TRANSACTION
        previous_block = self.get_previous_block()
        return previous_block['index']
    
    
    #2. CONSENSUS: ALL NODES CONTAIN THE SAME CHAIN
    
    #ADDING A NODE
    def add_node(self, address):
        
        #PARSE ADDRESS OF NODE
        parsed_url = urlparse(address)
        
        self.nodes.add(parsed_url.netloc)
        
    
    #REPLACE THE SHORTER CHAINS WITH THE LARGEST CHAIN IN NETWORK
    def replace_chain(self):
        
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        
        for node in network:
            
            #SEND REQUEST TO GET THE CHAIN
            response = requests.get(f"http://{node}/get_chain")
            
            #CHECK SUCESS
            if response.status_code == 200:
                
                #GET LENGTH OF CHAIN
                length = response.json()['length']
                chain = response.json()['chain']
                
                #CHECK IF LARGEST CHAIN & CHAIN IS VALID
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
                    
        if longest_chain: #NOT NONE
        
            #REPLACE CHAIN
            self.chain = longest_chain
            
            #REPLACED
            return True
        
        return False
    
    

#PART 2 - MINING OUR BLOCKCHAIN

#INTEGRATE THE TRANSACTIONS
#ADD SOME NODES
#REQUEST TO ADD A TRANSACTION TO BLOCKCHAIN


#create an address for the node on Port: 5001

    
#CREAATING A WEB APP TO VISUALISE BLOCKCHAIN
app = Flask(__name__)

node_address = str(uuid4()).replace('-', '') #RANDOM ADDRESS WITH DASHES REMOVED
#INCLUDE TRANSACTIONS IN MINE BLOCK
    
#CREATING A BLOCKCHAIN:INSTANTIATE THE BLOCKCHAIN
blockchain = Blockchain()

#MINE A NEW BLOCK BY MAKING A NEW REQUEST


#WHAT URL SHOULD TRIGGER THE FUNCTION & HTTP METHOD: GET TO RETRIEVE SOMETHING; POST TO CREATE SOMETHING
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    
    #SOLVE PROOF OF WORK PROBLEM
    
    #GET THE PREVIOUS PROOF
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    
    proof = blockchain.proof_of_work(previous_proof)
    

    #MINER GETS SOME CRYPTOCURRENCY AS REWARD
    blockchain.add_transaction(sender=node_address, receiver='Miner', amount = 10)
    
    
    #CREATE THE BLOCK
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    
    print(f"MINED PREVIOUS HASH = {previous_hash}\nHASH OF PREVIOUS BLOCK = {blockchain.hash(previous_block)}")
    
    
    #DISPLAY THE BLOCK IN POSTMAN: INFO OF BLOCK AND MESSAGE TO MINER
    response = {'message': 'Congratulations, you just mined a new block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']
                }
    
    #JSONIFIED RESPONSE AND HTTP STATUS CODE FOR SUCCESSFUL HTTP REQUEST
    return jsonify(response), 200
    

#FULL BLOCKCHAIN DISPLAYED IN INTERFACE POSTMAN
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)
                }
    
    return jsonify(response), 200


@app.route('/is_valid', methods = ['GET'])
def is_valid():
    response = {'Valid': blockchain.is_chain_valid(blockchain.chain),
                'Timestamp Of Verification': datetime.datetime.now()
                }
    
    return jsonify(response),200



#POST REQUEST TO ADD A TRANSACTION TO THE BLOCKCHAIN
@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
    #JSON FILE WITH DATA FROM POSTMAN
    json = request.get_json()
    
    #CHECK ALL KEYS IN JSON FILE PRESENT
    transaction_keys = ['sender','receiver','amount']
    
    
    if not all (key in json for key in transaction_keys):
        #400->BAD REQUEST CODE
        return "Failure. All elements of transaction not present", 400
    
    #FIND INDEX OF BLOCK THAT WILL HAVE THIS TRANSACTION
    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    
    #RETURN THE RESPONSE
    response = {
            'message': f"Success. Transaction will be added to block {index}"
        }
    
    #SUCCESS CODE RETURNED FOR POST REQUEST: 201
    return jsonify(response), 201


#PART 3 - DECENTRALISING THE BLOCKCHAIN
#-> 1. CONNECT NEW NODES TO BLOCKCHAIN
#-> 2. REQUEST TO APPLY CONSENSUS GETTING THE MOST UP-TO-DATE BLOCKCHAIN


#1. CONNECTING NEW NODES
#-> POSTMAN WILL SEND A JSON FILE WITH ALL NODES + NEW NODE

@app.route('/connect_node', methods = ['POST'])
def connect_node():
    #JSON FILE WITH NODES
    json = request.get_json()
    
    #LIST OF ADDRESSES
    nodes = json.get('nodes')
    
    #CHECK
    if nodes is None:
        return "Failure. No nodes sent", 400
    
    #ADD NODES TO SET
    for node in nodes:
        blockchain.add_node(node)

    
    #RETURN RESPONSE
    response = {
        'message': 'Success. All nodes now connected',
        'Total Number of nodes': len(list(blockchain.nodes))
        }
    
    return jsonify(response), 201
    
#2. CHECK IF CHAIN IS UPDATED
@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    
    response = {}
    
    if is_chain_replaced:
        response = {'messsage': 'The chain was replaced',
                    'new chain': blockchain.chain}
        
    else:
        response = {'message': 'The chain is already up-to-date',
                    'chain': blockchain.chain}
        
    #SUCCESS RETURNED
    return jsonify(response), 200




if __name__ == '__main__':
    print("Successfully executed")
    #RUNNING THE APPLICATION
    app.run(host= '0.0.0.0', port = 5001)




