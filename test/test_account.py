"""
Tests functionality of accounts API for version 2
"""


__version__ = '0.1.0'


import pytest
from test.conftest import register_urls_to_files, load_mock_json


def test_account(gw2_client, mock_adapter):
    """Tests the Account object

    Args:
        gw2_client: The pytest fixture for executing api calls.
        mock_adapter: The pytest fixture for mocking the return data.
    """

    register_urls_to_files(
        mock_adapter,
        {
            "account": "account",
            "account/17": "invalid_endpoint",
            "account?ids=1,2,3": "account",  # The api ignores ids, page, and page_size on this endpoint
            "account?page=1": "account",
            "account?pag_size=1": "account",
        })
    expected = load_mock_json("account")
    expected_error = load_mock_json("invalid_endpoint")

    result = gw2_client.account.get()
    assert result == expected

    result = gw2_client.account.get(id=None)
    assert result == expected

    result = gw2_client.account.get(id='17')
    assert result == expected_error

    result = gw2_client.account.get(ids=[1, 2, 3])
    assert result == expected

    result = gw2_client.account.get(ids=123)
    assert result == expected

    result = gw2_client.account.get(page=1)
    assert result == expected

    with pytest.raises(AssertionError):
        _ = gw2_client.account.get(page_size=201)

    result = gw2_client.account.get(page_size=1)
    assert result == expected


def test_account_achievements(gw2_client, mock_adapter):
    """Tests the Account Achievements object

    Args:
        gw2_client: The pytest fixture for executing api calls.
        mock_adapter: The pytest fixture for mocking the return data.
    """

    register_urls_to_files(
        mock_adapter,
        {
            "account/achievements": "account_achievements",
            "account/achievements?page=1&page_size=1": "account_achievements_pagesize1",
            "account/achievements?ids=1,202": "account_achievements_multiple_ids",
            "account/achievements/17": "invalid_endpoint"
        })
    expected = load_mock_json("account_achievements")
    expected_page = load_mock_json("account_achievements_pagesize1")
    expected_multiple_ids = load_mock_json("account_achievements_multiple_ids")
    expected_error = load_mock_json("invalid_endpoint")

    result = gw2_client.accountachievements.get()
    assert result == expected

    result = gw2_client.accountachievements.get(id=None)
    assert result == expected

    result = gw2_client.accountachievements.get(id='17')
    assert result == expected_error

    result = gw2_client.accountachievements.get(ids=[1, 202])
    print(result)
    print(expected_multiple_ids)
    assert result == expected_multiple_ids

    result = gw2_client.accountachievements.get(ids=123)
    assert result == expected

    result = gw2_client.accountachievements.get(page=1)
    assert result == expected

    with pytest.raises(AssertionError):
        _ = gw2_client.accountachievements.get(page_size=201)

    result = gw2_client.accountachievements.get(page_size=1)
    assert result == expected

    result = gw2_client.accountachievements.get(page=1, page_size=1)
    assert result == expected_page
