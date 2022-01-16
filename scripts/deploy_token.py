from brownie import MarvelToken, config, network
from scripts.helpful_scripts import get_account
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(10000, "ether")


def deploy_lottery():
    account = get_account()
    token = MarvelToken.deploy(
        INITIAL_SUPPLY,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )

    print("Deployed MarvelToken!")
    return token


def main():
    deploy_lottery()
