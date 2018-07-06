"""
Tests functionality of commerce API for version 2
"""

import inspect
import functools
import json
import os
import pathlib
import pytest
import requests_mock

from gw2api import GuildWars2Client



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
    result = gw2_client.commerceexchangecoins.get(quantity = 100000)

    # Result should look similar to:
    # {
    #     "coins_per_gem": 2941,
    #     "quantity": 34
    # }
    assert result["coins_per_gem"] == 2941 
    assert result["quantity"] == 34


def test_coins_to_gems(gw2_client, mock_adapter):
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
    result = gw2_client.commerceexchangegems.get(quantity = 100)

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



@functools.lru_cache()
def mocks_path():
    """Returns the path to the stored mock JSON files.

    Returns:
        The path to the mock files to be loaded and sent to the API requests.
    """
    this_file = inspect.getframeinfo(inspect.currentframe()).filename
    return pathlib.Path(os.path.dirname(os.path.abspath(this_file))) / 'mocks'


def load_mock_text(filename_stem):
    """Loads the mocks/{filename_stem}.json.

    Args:
        filename_stem: The stem of the filename to load, e.g. 'continents' would
                       load mocks/continents.json.
    Returns:
        The file content as text.
    """
    with (mocks_path() / '{}.json'.format(filename_stem)).open() as f:
        return f.read()

def load_mock_json(filename_stem):
    """Loads the mocks/{filename_stem}.json and parses it as JSON. Returns
    the resulting dictionary.

    Args:
        filename_stem: The stem of the filename to load, e.g. 'continents' would
                       load mocks/continents.json.
    Returns:
        The dictionary from the parsed JSON file.
    """
    return json.loads(load_mock_text(filename_stem))

def register_urls_to_files(adapter, url_to_file):
    """Registers a dictionary of urls to filename_stems with the mock adapter:

        {
            'continents/2': 'continents2'
        }

    would register the URL https://api.guildwars2.com/v2/continents/2 to
    return the contents of mocks/continents2.json.

    Args:
        adapter: The mock adapter to register the urls against.
        url_to_file: A dictionary mapping url parts to filenames, see above.
    """
    for url, filename_stem in url_to_file.items():
        url = '{}/v2/{}'.format(GuildWars2Client.BASE_URL, url)
        response = load_mock_text(filename_stem)
        adapter.register_uri('GET', url, text=response)

@pytest.fixture
def mock_adapter():
    """Creates a mock adapter instance.

    As this is a pytest fixture, tests only need to provide an argument
    with the name `mock_adapter` gain access to the mock adapter.

    Returns:
        A mock adapter. This exposes the register_uri function which can be used
        to mock requests.
    """
    return requests_mock.Adapter()

@pytest.fixture
def gw2_client(mock_adapter):
    """Creates a GuildWars2Client instance and mounts the mock adapter onto its
    session.

    As this is a pytest fixture, tests only need to provide an argument
    with the name `gw2_client` to gain access to the mocked instance.

    Returns:
        A GuildWars2Client instance with a mock session.
    """
    gw2_client = GuildWars2Client(api_key = "empty-api-key")
    gw2_client.session.mount('https://', mock_adapter)
    return gw2_client

