def inch_swap_approve(privatekey, amount, fromTokenAddress, to_symbol):
    """
    Approves the 1inch DEX to spend a certain amount of tokens.
    Args:
        privatekey (str): The private key of the Ethereum account that owns the tokens.
        amount (int): The amount of tokens to approve.
        fromTokenAddress (str): The address of the token to approve.
        to_symbol (str): The symbol of the token to approve.
    Returns:
        str: The transaction hash.
    """

    web3 = get_web3()
    account = web3.eth.account.privateKeyToAccount(privatekey)
    erc20_abi = get_erc20_abi()
    erc20_contract = web3.eth.contract(address=fromTokenAddress, abi=erc20_abi)
    to_address = get_1inch_address(to_symbol)
    nonce = web3.eth.getTransactionCount(account.address)
    tx = erc20_contract.functions.approve(to_address, amount).buildTransaction({
        'chainId': 1,
        'gas': 100000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce,
    })
    signed_tx = account.sign_transaction(tx)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()

