from iot_simulation import generate_iot_data  # Correctly import the function

import json
import time
from web3 import Web3

# Connect to local Ethereum node
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
web3.eth.default_account = web3.eth.accounts[0]

# Load the contract
contract_address = '0xbB9fCf9F9C338FBc4c4cE5Ce241F3bBae4D800e2'  # Replace with your deployed contract address
with open('compiled_contracts/compiled_contract.json', 'r') as file:
    contract_json = json.load(file)

abi = contract_json['contracts']['IoTDataStorage.sol']['IoTDataStorage']['abi']
iot_contract = web3.eth.contract(address=contract_address, abi=abi)

def record_data_to_blockchain(data):
    """Record IoT data to the blockchain."""
    tx_hash = iot_contract.functions.storeData(json.dumps(data)).transact()
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Data recorded in transaction: {receipt.transactionHash.hex()}")

# Example integration with IoT data generation
if __name__ == "__main__":
    while True:
        iot_data = generate_iot_data()
        print(f"Generated IoT Data: {iot_data}")
        record_data_to_blockchain(iot_data)
        time.sleep(5)
