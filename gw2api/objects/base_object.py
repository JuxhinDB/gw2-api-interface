from requests import Session
from gw2api import GuildWars2Client


class BaseAPIObject:
    """
    Base Resource handler that provides common properties
     and methods to be used by child resources.

    Can only be used once one or more `GuildWars2Client`
     have been instantiated to make sure that the `requests.Session()`
     object has been correctly set.
    """

    def __init__(self, object_type):
        """
        Initializes a **base** API object. Primarily acts as an interface
         for all child object to use.

        >>> import requests
        >>>
        >>> session = requests.Session()
        >>> object_type = 'guild'
        >>>
        >>> base_api_object = BaseAPIObject(session, object_type)

        :param object_type: String indicating what type of object to
                             interface with (i.e. 'guild'). Primarily
                             acts as the relative path to the base URL
        :raises ValueError: In the event that either a `Session` object
                             or `object_type` are not set.
        """
        if not object_type:
            raise ValueError('API Object requires `object_type` to be passed for %s'
                             .format(self.__class__.__name__))

        self.session = None
        self.object_type = object_type

        self.base_url = GuildWars2Client.BASE_URL
        self.version = GuildWars2Client.VERSION

    def get(self, url=None, **kwargs):
        """Get a resource for specific object type

            Args:
                 url: string, the url to use instead of building a base url
                 **kwargs
                     id = int, an id to append to the API call.
                     ids = list, the list of ids to append to the API call.
                     page = int, the page to start from.
                     page_size = int, the size of page to view.
                     schema_version = string, the version of the schema to use. example; '2019-02-21T00:00:00Z'

            Raises:
                AssertionError: if page_size is less than 1 or greater than 200
        """

        assert isinstance(self.session, Session), "BaseObject.session is not yet instantiated. Make sure an instance" \
                                                  "of GuildWars2APIClient is created first to be able to send requests."

        _id = kwargs.get('id')
        ids = kwargs.get('ids')
        page = kwargs.get('page')
        page_size = kwargs.get('page_size')
        schema_version = kwargs.get('schema_version')

        if not url:
            request_url = self._build_endpoint_base_url()
        else:
            request_url = url

        if bool(kwargs) and '?' not in request_url:
            request_url += '?'

        if _id:
            request_url += f'id={str(_id)}&'  # {base_url}/{object}/{id}
        elif ids:
            try:
                request_url += 'ids=' + ','.join([str(_) for _ in ids]) + '&'
            except TypeError:
                print("Could not add ids because the given ids argument is not an iterable.")

        if page:
            request_url += f'page={page}&'

        if page_size:
            assert 0 < page_size <= 200
            request_url += f'page_size={page_size}&'

        if schema_version:
            request_url += f'v={schema_version}'

        request_url = request_url.strip('&')  # Remove any trailing '&'
        request_url = request_url.strip('?')  # Remove any trailing '&'
        print(request_url)

        response = self.session.get(request_url)
        response.raise_for_status()
        return response    

    def _build_endpoint_base_url(self):
        """Construct the base URL to access an API object"""
        return '{base_url}/{version}/{object}'.format(base_url=self.base_url,
                                                      version=self.version,
                                                      object=self.object_type)

    def __repr__(self):
        return '<BaseAPIObject %r\nType: %r>' % (self.session, self.object_type)
