import hashlib
import json
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_properties = []
        self.create_block(proof=100, previous_hash='1')  # Genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'properties': self.current_properties,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.current_properties = []
        self.chain.append(block)
        return block

    def add_property(self, owner_name, property_id, location, value):
        self.current_properties.append({
            'owner_name': owner_name,
            'property_id': property_id,
            'location': location,
            'value': value
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def verify_property(self, property_id):
        for block in self.chain:
            for prop in block['properties']:
                if prop['property_id'] == property_id:
                    return prop
        return None
