from client import GuildWars2Client


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

        assert GuildWars2Client.session

        self.session = GuildWars2Client.session
        self.object_type = object_type

        self.base_url = GuildWars2Client.BASE_URL
        self.version = GuildWars2Client.VERSION

    def get(self, **kwargs):
        """Get a resource for specific object type"""
        request_url = self._build_endpoint_url()
        return self.session.get(request_url)

    def _build_endpoint_url(self):
        """Construct the base URL to access an API object"""
        return '{base_url}/{version}/{object}'.format(base_url=self.base_url,
                                                      version=self.version,
                                                      object=self.object_type)

    def __repr__(self):
        return '<BaseAPIObject %r\nType: %r>' % (self.session, self.object_type)
