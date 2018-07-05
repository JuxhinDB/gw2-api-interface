"""
Tests functionality of conversion rate API for version 2
"""

from gw2api import GuildWars2Client


def test_coins_to_gems(gw2_client):
    """Tests conversion of coins to gems

    Args:
        gw2_client: The pytest "gw2_client" fixture.
    """

    # get conversion rate of 100000 coins to gems
    result = gw2_client.commerceexchangecoins.get(quantity = 100000)

    # Result should look similar to:
    # {
    #     "coins_per_gem": 2941,
    #     "quantity": 34
    # }
    assert "coins_per_gem" in result.keys()
    assert "quantity" in result.keys()


def test_coins_to_gems(gw2_client):
    """Tests conversion of gems to coins

    Args:
        gw2_client: The pytest "gw2_client" fixture.
    """

    # get conversion rate of 100 gems to coins
    result = gw2_client.commerceexchangegems.get(quantity = 100)

    # Result should look similar to:
    # {
    #     "coins_per_gem": 1841,
    #     "quantity": 184134
    # }
    assert "coins_per_gem" in result.keys()
    assert "quantity" in result.keys()
