from web3 import Web3
from solcx import compile_standard, set_solc_version
import json

# Set Solidity compiler version
set_solc_version('0.8.0')

# Compile the Solidity contract
with open('contracts/IoTData.sol', 'r') as file:
    contract_source_code = file.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"IoTDataStorage.sol": {"content": contract_source_code}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": [
                    "abi",
                    "metadata",
                    "evm.bytecode",
                    "evm.bytecode.sourceMap"
                ]
            }
        }
    }
})

# Save the compiled contract to a JSON file
with open('compiled_contracts/compiled_contract.json', 'w') as file:
    json.dump(compiled_sol, file)

# Extract ABI afrom web3 import Web3
from solcx import compile_standard, install_solc
import json
# Install a specific version of Solidity if not already installed
install_solc()  # This will use the install_solc directly
# Install Solidity compiler

# Compile the Solidity contract
with open('contracts/IoTData.sol', 'r') as file:
    contract_source_code = file.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"IoTDataStorage.sol": {"content": contract_source_code}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": [
                    "abi",
                    "metadata",
                    "evm.bytecode",
                    "evm.bytecode.sourceMap"
                ]
            }
        }
    }
})

# Save the compiled contract to a JSON file
with open('compiled_contracts/compiled_contract.json', 'w') as file:
    json.dump(compiled_sol, file)

# Extract ABI and Bytecode
abi = compiled_sol['contracts']['IoTDataStorage.sol']['IoTDataStorage']['abi']
bytecode = compiled_sol['contracts']['IoTDataStorage.sol']['IoTDataStorage']['evm']['bytecode']['object']

# Connect to local Ethereum node (Ganache)
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
web3.eth.default_account = web3.eth.accounts[0]  # Set the default account (usually the first one)

# Deploy the contract
IoTDataStorage = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = IoTDataStorage.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Get the deployed contract address
contract_address = tx_receipt.contractAddress
print(f"Contract deployed at address: {contract_address}")
_account = web3.eth.accounts[0]  # Set the default account (usually the first one)

# Deploy the contract
IoTDataStorage = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = IoTDataStorage.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Get the deployed contract address
contract_address = tx_receipt.contractAddress
print(f"Contract deployed at address: {contract_address}")
