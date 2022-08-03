from scripts.helpful_scripts import get_account
from brownie import OurToken, config, network
from web3 import Web3


def deploy_our_token():
    account = get_account()
    initial_supply = Web3.toWei(100, "ether")
    ourtoken = OurToken.deploy(
        initial_supply,
        {"from": account, "required_confs": 1},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed token!")
    return ourtoken


def main():
    deploy_our_token()
