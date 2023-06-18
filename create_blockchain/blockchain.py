#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 00:02:58 2023

@author: kpandey

MODULE 1: CREATING A BLOCKCHAIN 
"""

#NEED A WEB BASED BLOCKCHAIN: FLASK
#USER-FRIENDLY INTERFACE: POSTMAN


#IMPORTING THE LIBRARIES
import  datetime #TIMESTAMP OF BLOCK
import hashlib #HASH OF BLOCK
import json #RETURN DATA ABOUT BLOCK
from flask import Flask, jsonify


#DATETIME IS NOT JSON SERIALISABLE
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)


#OPTION1: MAKE SEVERAL FUNCTIONS
#OPTION2: WITH A CLASS: BEST OPTION

#PART 1 - BUILDING A BLOCKCHAIN
class Blockchain:
    
    #COMPONENTS OF BLOCKCHAIN
    
    def __init__(self): #ALWAYS TAKES IN SELF AS ARGUMENT
        #INITIALISE THE CHAIN TO CONTAIN BLOCKS #EMPTY LIST
        self.chain = []
        
        #GENESIS BLOCK
        self.create_block(proof = 1, previous_hash = '0') #PROOF AND PREVIOUS HASH


        #DIFFERENCE BETWEEN CREATE BLOCK AND MINE BLOCK
        #MINE GETS PROOF OF WORK AND THEN CALL CREATE BLOCK
        
    def create_block(self, proof, previous_hash):
        
        #NEW BLOCK: DICTIONARY!
        block = {'index': len(self.chain)+1, 
                 'timestamp': datetime.datetime.now(),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'data': 'Sample Data'}
        
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
            hash_operation = hashlib.sha256(str(1 + new_proof**2 - previous_proof**2 - 2*new_proof**3 + 5*previous_proof).encode()).hexdigest() #NON-SYMMETRICAL OPERATION
            
            #EXPECTED FORMAT
            if hash_operation[:4] == '00000':
                #MINER WINS!
                check_proof = True
                
            else:
                #INCREMENT NEW PROOF
                new_proof+=1
    
        return new_proof
    
    #HASH FUNCTION: HASH EACH BLOCK
    def hash(self, block):
        
        #CONVERT DICTIONARY TO STRING
        encoded_block = json.dumps(block, sort_keys=True, cls=CustomJSONEncoder).encode()
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
            hash_operation = hashlib.sha256(str(1 + proof**2 - previous_proof**2 - 2*proof**3 + 5*previous_proof).encode()).hexdigest() #NON-SYMMETRICAL OPERATION
            
            if hash_operation[:4] !='00000':
                return False
            
            #UPDATE VARIABLES
            previous_block = block
            block_index += 1
            
        return True

#PART 2 - MINING OUR BLOCKCHAIN
    
#CREAATING A WEB APP TO VISUALISE BLOCKCHAIN
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.json_encoder = CustomJSONEncoder

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
    
    #CREATE THE BLOCK
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    
    #DISPLAY THE BLOCK IN POSTMAN: INFO OF BLOCK AND MESSAGE TO MINER
    response = {'message': 'Congratulations, you just mined a new block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']
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

if __name__ == '__main__':
#RUNNING THE APPLICATION
    app.run(host= '0.0.0.0', port = 5002)


























