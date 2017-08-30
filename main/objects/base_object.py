
class BaseAPIObject:
    """
    Base Resource handler that provides common properties
     and methods to be used by child resources.
    """

    def __init__(self, session, object_type):
        """
        Initializes a **base** API object. Primarily acts as an interface
         for all child object to use.

        >>> import requests
        >>>
        >>> session = requests.Session()
        >>> object_type = 'guild'
        >>>
        >>> base_api_object = BaseAPIObject(session, object_type)

        :param session: `requests.Session()` object,
                        see :class:`main.client.GuildWars2Client`
        :param object_type: String indicating what type of object to
                             interface with (i.e. 'guild'). Primarily
                             acts as the relative path to the base URL
        :raises ValueError: In the event that either a `Session` object
                             or `object_type` are not set.
        """
        if not (session and object_type):
            raise ValueError('API Object requires `session` and `object_type` to be passed for %s'
                             .format(self.__class__.__name__))

        self.session = session
        self.object_type = object_type

    def get(self, **kwargs):
        """Get a resource for specific object type"""
        raise NotImplementedError

    def __repr__(self):
        return '<BaseAPIObject %r\n%r>'.format(self.session, self.object_type)
