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
            "account?id=17": "account",
            "account?ids=1,2,3": "account",
            "account?page=1": "account",
            "account?pag_size=1": "account",
            "account?page=1&page_size=1": "account"
        })
    expected = load_mock_json("account")

    result = gw2_client.account.get()
    assert result == expected

    result = gw2_client.account.get(id=None)
    assert result == expected

    result = gw2_client.account.get(id='17')
    assert result == expected

    result = gw2_client.account.get(ids=[1, 2, 3])
    assert result == expected

    result = gw2_client.account.get(ids=123)
    assert result == expected

    result = gw2_client.account.get(page=1)
    assert result == expected

    with pytest.raises(AssertionError):
        _ = gw2_client.account.get(page_size=201)

    with pytest.raises(AssertionError):
        _ = gw2_client.account.get(page_size=-1)

    result = gw2_client.account.get(page_size=1)
    assert result == expected

    result = gw2_client.account.get(page=1, page_size=1)
    assert result == expected


def test_account_achievements(gw2_client, mock_adapter):
    """Tests the AccountAchievements object

    Args:
        gw2_client: The pytest fixture for executing api calls.
        mock_adapter: The pytest fixture for mocking the return data.
    """

    register_urls_to_files(
        mock_adapter,
        {
            "account/achievements": "account_achievements",
            "account/achievements?page=1": "account_achievements",
            "account/achievements?page_size=1": "account_achievements",
            "account/achievements?page=1&page_size=1": "account_achievements_pagesize1",
            "account/achievements?ids=1,202": "account_achievements_multiple_ids",
            "account/achievements?id=1": "account_achievements_single_id"
        })
    expected = load_mock_json("account_achievements")
    expected_page = load_mock_json("account_achievements_pagesize1")
    expected_multiple_ids = load_mock_json("account_achievements_multiple_ids")
    expected_single_id = load_mock_json("account_achievements_single_id")

    result = gw2_client.accountachievements.get()
    assert result == expected

    result = gw2_client.accountachievements.get(id=None)
    assert result == expected

    result = gw2_client.accountachievements.get(id='1')
    assert result == expected_single_id

    result = gw2_client.accountachievements.get(ids=[1, 202])
    assert result == expected_multiple_ids

    result = gw2_client.accountachievements.get(ids=123)
    assert result == expected

    result = gw2_client.accountachievements.get(page=1)
    assert result == expected

    with pytest.raises(AssertionError):
        _ = gw2_client.accountachievements.get(page_size=201)

    with pytest.raises(AssertionError):
        _ = gw2_client.accountachievements.get(page_size=-1)

    result = gw2_client.accountachievements.get(page_size=1)
    assert result == expected

    result = gw2_client.accountachievements.get(page=1, page_size=1)
    assert result == expected_page


def test_account_bank(gw2_client, mock_adapter):
    """Tests the AccountBank object

    Args:
        gw2_client: The pytest fixture for executing api calls.
        mock_adapter: The pytest fixture for mocking the return data.
    """

    register_urls_to_files(
        mock_adapter,
        {
            "account/bank": "account_bank",
            "account/bank?page=1": "account_bank",
            "account/bank?page_size=1": "account_bank",
            "account/bank?page=1&page_size=1": "account_bank",
            "account/bank?ids=20796,94884": "account_bank",
            "account/bank?id=1": "account_bank"
        })
    expected = load_mock_json("account_bank")

    result = gw2_client.accountbank.get()
    assert result == expected

    result = gw2_client.accountbank.get(id=None)
    assert result == expected

    result = gw2_client.accountbank.get(id='1')
    assert result == expected

    result = gw2_client.accountbank.get(ids=[20796, 94884])
    assert result == expected

    result = gw2_client.accountbank.get(ids=123)
    assert result == expected

    result = gw2_client.accountbank.get(page=1)
    assert result == expected

    with pytest.raises(AssertionError):
        _ = gw2_client.accountbank.get(page_size=201)

    with pytest.raises(AssertionError):
        _ = gw2_client.accountbank.get(page_size=-1)

    result = gw2_client.accountbank.get(page_size=1)
    assert result == expected

    result = gw2_client.accountbank.get(page=1, page_size=1)
    assert result == expected


def test_account_dailycrafting(gw2_client, mock_adapter):
    """Tests the AccountDailyCrafting object

    Args:
        gw2_client: The pytest fixture for executing api calls.
        mock_adapter: The pytest fixture for mocking the return data.
    """

    register_urls_to_files(
        mock_adapter,
        {
            "account/dailycrafting": "account_dailycrafting",
            "account/dailycrafting?page=1": "account_dailycrafting",
            "account/dailycrafting?page_size=1": "account_dailycrafting",
            "account/dailycrafting?page=1&page_size=1": "account_dailycrafting",
            "account/dailycrafting?ids=1,202": "account_dailycrafting",
            "account/dailycrafting?id=1": "account_dailycrafting"
        })
    expected = load_mock_json("account_dailycrafting")

    result = gw2_client.accountdailycrafting.get()
    assert result == expected

    result = gw2_client.accountdailycrafting.get(id=None)
    assert result == expected

    result = gw2_client.accountdailycrafting.get(id='1')
    assert result == expected

    result = gw2_client.accountdailycrafting.get(ids=[1, 202])
    assert result == expected

    result = gw2_client.accountdailycrafting.get(ids=123)
    assert result == expected

    result = gw2_client.accountdailycrafting.get(page=1)
    assert result == expected

    with pytest.raises(AssertionError):
        _ = gw2_client.accountdailycrafting.get(page_size=201)

    with pytest.raises(AssertionError):
        _ = gw2_client.accountdailycrafting.get(page_size=-1)

    result = gw2_client.accountdailycrafting.get(page_size=1)
    assert result == expected

    result = gw2_client.accountdailycrafting.get(page=1, page_size=1)
    assert result == expected
