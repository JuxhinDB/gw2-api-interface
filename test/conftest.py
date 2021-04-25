"""Configuration items for running tests
"""

__version__ = '0.1.0'

import inspect
import functools
import json
import os
import pathlib
import pytest
import requests_mock

from gw2api import GuildWars2Client


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
    gw2_client = GuildWars2Client(api_key="empty-api-key")
    gw2_client.session.mount('https://', mock_adapter)
    return gw2_client
