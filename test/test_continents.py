import collections
import itertools
import pytest

from test.conftest import register_urls_to_files, load_mock_json


def powerset(iterable):
    """Returns the powerset of the iterable.

    See https://docs.python.org/3.6/library/itertools.html#itertools-recipes

    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    Args:
        iterable: An iterable to create the powerset.
    """
    return itertools.chain.from_iterable(
        itertools.combinations(iterable, r) for r in range(len(iterable)+1)
    )


def test_continents_single_id(gw2_client, mock_adapter):
    """Tests all simple parameter combinations for the continents endpoint.

    First, only continent='all' is tested, then continent=2. After that,
    floor='all' is introduced, keeping continent=2 fixed.
    The same is done for all five deeper routes:
        continent     all,    2
        floors        all,   15  # 15 as string
        regions       all,   26
        maps          all, 1205  # 1205 as string
        sectors       all, 1478

    Note that only single ids per level are tested, since it is impossible
    to walk deeper if multiple IDs are given. See test_continents_multi_id
    for that test.

    The fixture loads the data as plain text, the test parses it as json.
    The test is then, if we got the correct JSON, which means the client
    constructed the correct url to hit the (mocked) API.

    Args:
        gw2_client: The pytest "gw2_client" fixture.
        mock_adapter: The pytest "mock_adapter" fixture.
    """
    # Prepare mock adapter
    url_parts = ['continents', 2,
                 'floors', '15',
                 'regions', 26,
                 'maps', '1205',
                 'sectors', 1478]
    url_to_file = {}
    for i, url_part in enumerate(url_parts):
        filename = ''.join(map(str, url_parts[:i+1]))
        url = '/'.join(map(str, url_parts[:i+1]))
        url_to_file[url] = filename
    register_urls_to_files(mock_adapter, url_to_file)

    # Alternate between resource='all' and resource=fixed_id, appending
    # the deep levels to the flat levels:
    # 1. continents='all'
    # 2. continents=2
    # 3. continents=2, floors='all'
    # 4. continents=2, floors='15'
    # ...
    kwargs = {}
    for i in range(10):
        if i % 2 == 0:
            kwargs[url_parts[i]] = 'all'
        else:
            kwargs[url_parts[i - 1]] = url_parts[i]

        expected = load_mock_json(''.join(map(str, url_parts[:i+1])))
        actual = gw2_client.continents.get(**kwargs)

        assert actual == expected, 'Incorrect for ' + str(kwargs)


def test_continents_multi_id(gw2_client, mock_adapter):
    """This test tests for each sub route, if it correctly supports handling of
    multiple ids.

    For example, /continents/2/floors?ids=1,6 by calling
    gw2_client.continents.get(continents=2, floors=(1,6))

    Args:
        gw2_client: The pytest "gw2_client" fixture.
        mock_adapter: The pytest "mock_adapter" fixture.
    """
    url_to_file = {
        'continents?ids=1,2': 'continents1_2',
        'continents/2/floors?ids=1,6': 'continents2floors1_6',
        'continents/2/floors/1/regions?ids=6,7':
            'continents2floors1regions6_7',
        'continents/2/floors/1/regions/6/maps?ids=350,549,900':
            'continents2floors1regions6maps350_549_900',
        'continents/2/floors/1/regions/7/maps/38/sectors?ids=833,834':
            'continents2floors1regions7maps38sectors833_834',
    }
    register_urls_to_files(mock_adapter, url_to_file)

    test = 'continents1_2'
    expected = load_mock_json(test)
    actual = gw2_client.continents.get(continents=[1, 2])
    assert actual == expected, 'Incorrect for ' + test

    test = 'continents1_2'
    expected = load_mock_json(test)
    actual = gw2_client.continents.get(continents='1,2')
    assert actual == expected, 'Incorrect for ' + test + ' b'

    test = 'continents2floors1_6'
    expected = load_mock_json(test)
    actual = gw2_client.continents.get(continents=2, floors=[1, 6])
    assert actual == expected, 'Incorrect for ' + test

    test = 'continents2floors1regions6_7'
    expected = load_mock_json(test)
    actual = gw2_client.continents.get(continents=2, floors=1, regions=[6, 7])
    assert actual == expected, 'Incorrect for ' + test

    test = 'continents2floors1regions6maps350_549_900'
    expected = load_mock_json(test)
    actual = gw2_client.continents.get(continents=2, floors=1, regions=6,
                                       maps=[350, 549, 900])
    assert actual == expected, 'Incorrect for ' + test

    test = 'continents2floors1regions7maps38sectors833_834'
    expected = load_mock_json(test)
    actual = gw2_client.continents.get(continents=2, floors=1, regions=7,
                                       maps=38, sectors=[833, 834])
    assert actual == expected, 'Incorrect for ' + test


def test_continents_no_continents(gw2_client):
    """Tests for missing continent IDs.

    Args:
        gw2_client: The pytest "gw2_client" fixture.
    """
    kwargs = {
        'floors': 2,
        'regions': 3,
        'maps': 4,
        'sectors': 5,
    }
    kwargs_powerset = list(map(dict, powerset(kwargs.items())))
    for kwargs in kwargs_powerset[1:]:
        with pytest.raises(KeyError, match=r'continents'):
            gw2_client.continents.get(**kwargs)


def test_continents_no_floors(gw2_client):
    """Tests for missing floor IDs.

    Args:
        gw2_client: The pytest "gw2_client" fixture.
    """
    kwargs = {
        'regions': 3,
        'maps': 4,
        'sectors': 5,
    }
    kwargs_powerset = list(map(dict, powerset(kwargs.items())))
    for kwargs in kwargs_powerset[1:]:
        with pytest.raises(KeyError, match=r'floors'):
            gw2_client.continents.get(continents=1, **kwargs)


def test_continents_no_regions(gw2_client):
    """Tests for missing region IDs.

    Args:
        gw2_client: The pytest "gw2_client" fixture.
    """
    kwargs = {
        'maps': 4,
        'sectors': 5,
    }
    kwargs_powerset = list(map(dict, powerset(kwargs.items())))
    for kwargs in kwargs_powerset[1:]:
        with pytest.raises(KeyError, match=r'regions'):
            gw2_client.continents.get(continents=1, floors=1, **kwargs)


def test_continents_no_maps(gw2_client):
    """Tests for missing map IDs.

    Args:
        gw2_client: The pytest "gw2_client" fixture.
    """
    kwargs = {
        'sectors': 5,
    }
    kwargs_powerset = list(map(dict, powerset(kwargs.items())))
    for kwargs in kwargs_powerset[1:]:
        with pytest.raises(KeyError, match=r'maps'):
            gw2_client.continents.get(continents=2, floors=1, regions=1, **kwargs)


def test_continents_inappropriate_multi_id(gw2_client):
    """Tests that only the last level can have multiple IDs, i.e. when
    supplying floors, continents must not be a list of IDs etc.

    Args:
        gw2_client: The pytest "gw2_client" fixture.
    """
    levels = ['continents', 'floors', 'regions', 'maps', 'sectors']
    for i, list_level in enumerate(levels):
        kwargs = collections.OrderedDict({level: 1 for level in levels})
        kwargs[list_level] = [1, 2]
        for level in reversed(levels):
            if level == list_level:
                break
            with pytest.raises(KeyError, match=r'too many ids'):
                gw2_client.continents.get(**kwargs)
            del kwargs[level]


def test_continents_backwards_compatibility(gw2_client, mock_adapter):
    """This test assures that the new changes to introduce all sub parts of
    the continents API does not break the old behaviour, that is accessing
    the continents via id=.

    Args:
        gw2_client: The pytest "gw2_client" fixture.
        mock_adapter: The pytest "mock_adapter" fixture.
    """
    url_to_file = {
        'continents': 'continents',
        'continents/2': 'continents2',
        'continents?ids=1,2': 'continents1_2',
    }
    register_urls_to_files(mock_adapter, url_to_file)

    expected_continent_list = load_mock_json('continents')
    assert gw2_client.continents.get() == expected_continent_list, '/continents failed'

    expected_single_id = load_mock_json('continents2')
    assert gw2_client.continents.get(id=2) == expected_single_id, '/continents?id=2 failed'


def test_continents_backwards_compatibility_ids(gw2_client, mock_adapter):
    """This test assures that the new changes to introduce all sub parts of
    the continents API does not break the old behaviour, that is accessing
    the continents via ids=.

    Args:
        gw2_client: The pytest "gw2_client" fixture.
        mock_adapter: The pytest "mock_adapter" fixture.
    """
    register_urls_to_files(mock_adapter, {'continents?ids=1,2': 'continents1_2'})
    expected_multi_id = load_mock_json('continents1_2')
    assert gw2_client.continents.get(ids=[1, 2]) == expected_multi_id, '/continents?ids=1,2 failed'
