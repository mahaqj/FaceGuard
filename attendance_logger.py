from web3 import Web3
import json
import hashlib

# inline hashing
def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

# ganache connection
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
assert web3.is_connected(), "Web3 not connected"

# load abi
with open("AttendanceABI.json") as f:
    abi = json.load(f)

# setup contract
contract_address = "0xEF8ED6f4c1A7E684a9f49c9A472D5541bC64Ec27"
contract = web3.eth.contract(address=contract_address, abi=abi)
account = web3.eth.accounts[0]

# main function to log attendance
def mark_attendance(name, timestamp):
    name_hash = hash_text(name)
    timestamp_hash = hash_text(timestamp)

    tx_hash = contract.functions.markAttendance(name_hash, timestamp_hash).transact({
        'from': account,
        'gas': 3000000
    })

    try:
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=5)
        print(f"Blockchain log complete: {receipt.transactionHash.hex()}")
    except Exception as e:
        print(f"Blockchain error: {e}")
        raise
