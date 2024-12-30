"""
Tests functionality of commerce API for version 2
"""

from test.conftest import register_urls_to_files, load_mock_json


def test_coins_to_gems(gw2_client, mock_adapter):
    """Tests conversion of coins to gems

    Args:
        gw2_client: The pytest "gw2_client" fixture.
    """

    register_urls_to_files(
        mock_adapter, 
        {
            "commerce/exchange/coins?quantity=100000": 
                "coinstogems_quantity100000"
        })

    # get conversion rate of 100000 coins to gems
    result = gw2_client.commerceexchangecoins.get(quantity=100000)

    # Result should look similar to:
    # {
    #     "coins_per_gem": 2941,
    #     "quantity": 34
    # }
    assert result["coins_per_gem"] == 2941 
    assert result["quantity"] == 34


def test_coins_to_gems_small(gw2_client, mock_adapter):
    """Tests conversion of gems to coins

    Args:
        gw2_client: The pytest "gw2_client" fixture.
    """

    register_urls_to_files(
        mock_adapter, 
        {
            "commerce/exchange/gems?quantity=100": 
                "gemstocoins_quantity100"
        })

    # get conversion rate of 100 gems to coins
    result = gw2_client.commerceexchangegems.get(quantity=100)

    # Result should look similar to:
    # {
    #     "coins_per_gem": 1841,
    #     "quantity": 184134
    # }
    assert result["coins_per_gem"] == 1841 
    assert result["quantity"] == 184134


def test_transactions(gw2_client, mock_adapter):
    """Tests transactions API for account, both past and current

    Args:
        gw2_client: The pytest "gw2_client fixture.
    """

    register_urls_to_files(
        mock_adapter,
        {
            "commerce/transactions": "commerce_transactions",
            "commerce/transactions/history": "commerce_transactions_secondlevel",
            "commerce/transactions/current": "commerce_transactions_secondlevel",
            "commerce/transactions/history/buys": "commerce_historybuys",
            "commerce/transactions/history/sells": "commerce_historysells",
            "commerce/transactions/current/buys": "commerce_currentbuys",
            "commerce/transactions/current/sells": "commerce_currentsells"
        })

    # get list of second-level endpoints
    result = gw2_client.commercetransactions.get()
    assert all(["current" in result, "history" in result])

    # get list of third-level endpoints
    result = gw2_client.commercetransactions.history.get()
    assert all(["buys" in result, "sells" in result])
    result = gw2_client.commercetransactions.current.get()
    assert all(["buys" in result, "sells" in result])

    # get transaction buy history
    expected = load_mock_json("commerce_historybuys")
    result = gw2_client.commercetransactions.history.buys.get()
    assert result == expected

    # get transaction sell history
    expected = load_mock_json("commerce_historysells")
    result = gw2_client.commercetransactions.history.sells.get()
    assert result == expected

    # get transaction current buys
    expected = load_mock_json("commerce_currentbuys")
    result = gw2_client.commercetransactions.current.buys.get()
    assert result == expected

    # get transaction current sells
    expected = load_mock_json("commerce_currentsells")
    result = gw2_client.commercetransactions.current.sells.get()
    assert result == expected
