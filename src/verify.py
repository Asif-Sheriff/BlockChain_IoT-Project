from web3 import Web3
import json

# Connect to the local Ethereum node (Ganache)
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
web3.eth.default_account = web3.eth.accounts[0]

# Load the contract ABI
with open('compiled_contracts/compiled_contract.json', 'r') as file:
    contract_json = json.load(file)

abi = contract_json['contracts']['IoTDataStorage.sol']['IoTDataStorage']['abi']
contract_address = '0xb7b86406b926174f0a0a52f6e45f36764f55fb30'  # Replace with your deployed contract address
iot_contract = web3.eth.contract(address=contract_address, abi=abi)

def verify_data(expected_data):
    """
    Verifies the data stored on the blockchain matches the expected data.
    """
    data_count = iot_contract.functions.getDataCount().call()
    for i in range(data_count):
        stored_timestamp, stored_data = iot_contract.functions.getData(i).call()
        print(f"Stored Data {i}: {stored_data} at {stored_timestamp}")
        if json.loads(stored_data) == expected_data:
            print("Data verified successfully!")
        else:
            print("Data verification failed.")

# Example of verifying a generated IoT data
generated_data = {'temperature': 23.45}  # Replace with the actual data you generated and stored
verify_data(generated_data)
