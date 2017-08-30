import requests


class GuildWars2Client:
    """Parent client that handles authentication and requests"""

    BASE_URL = 'https://api.guildwars2.com'
    VERSION = 'v2'
    LANG = 'en'

    def __init__(self, base_url=BASE_URL, version=VERSION, lang=LANG, api_key=None, proxy=None):

        assert version in ('v1', 'v2')
        assert lang in ('en', 'es', 'de', 'fr', 'ko', 'zh')

        self.lang = lang
        self.proxy = proxy
        self.version = version
        self.api_key = api_key
        self.base_url = base_url

        self.session = self.__build_requests_session()

        # Constructs a list of API Objects to be assigned to this instance
        self.__build_object_clients()

    def __repr__(self):
        return '<GuildWars2Client Base URL: %r\nVersion: %r\nAPI Key: %r\nProxy: %r>'\
            .format(self.base_url, self.version, self.api_key, self.proxy)

    def __build_requests_session(self):
        """Build Request Session that handles all HTTP requests"""
        session = requests.Session()

        session.headers.update({
            'User-Agent': 'juxhindb-gw2-api-interface-python-wrapper',
            'Accept': 'application/json',
            'Accept-Language': self.lang
        })

        if self.api_key:
            assert isinstance(self.api_key, str)
            session.headers.update({'Authorization': 'Bearer ' + self.api_key})

        return session

    def __build_object_clients(self):
        """Creates and assigned API Objects to the class instance"""

        if self.version == 'v1':
            from main.objects.api_version_1 import API_OBJECTS
        elif self.version == 'v2':
            from main.objects.api_version_2 import API_OBJECTS
        else:
            raise ValueError('Unable to import API Objects, make '
                             'sure the version passed is valid - ' + self.version)

        objects = API_OBJECTS

        for object_ in objects:
            setattr(self, object_.__class__.__name__.lower(), object_)


