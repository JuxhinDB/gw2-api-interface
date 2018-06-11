import copy
import requests


class GuildWars2Client:
    """Parent client that stores the API Objects and metadata"""

    LANG = 'en'
    VERSION = 'v2'
    BASE_URL = 'https://api.guildwars2.com'

    def __init__(self, base_url=BASE_URL, version=VERSION, lang=LANG,
                 api_key=None, proxy=None, verify_ssl=True):

        assert version in ('v1', 'v2')
        assert lang in ('en', 'es', 'de', 'fr', 'ko', 'zh')

        self.lang = lang
        self.proxy = proxy
        self.api_key = api_key
        self.version = version
        self.base_url = base_url
        self.verify_ssl = verify_ssl

        if not self.verify_ssl:
            # Disable SSL Warnings in that case to avoid unnecessary verbosity
            requests.packages.urllib3.disable_warnings()

        GuildWars2Client.LANG = lang
        GuildWars2Client.VERSION = version
        GuildWars2Client.BASE_URL = base_url

        # This must be done before we build and assign the API objects (below)
        #  so as to avoid initializing them with a null session
        self.session = self.__build_requests_session()

        # Constructs a list of API Objects to be assigned to this instance
        self.__build_object_clients()

    def __build_requests_session(self):
        """Build Request Session that handles all HTTP requests"""
        session = requests.Session()

        # Particularly useful then passing requests through a local proxy
        session.verify = self.verify_ssl

        session.headers.update({
            'User-Agent': 'juxhindb-gw2-api-interface-python-wrapper',
            'Accept': 'application/json',
            'Accept-Language': GuildWars2Client.LANG
        })

        if self.api_key:
            assert isinstance(self.api_key, str)
            session.headers.update({'Authorization': 'Bearer ' + self.api_key})

        if self.proxy:
            # If this hits, the proxy format should be:
            # {
            #    'http': HTTP_PROXY_HOST:PORT,
            #    'https': HTTPS_PROXY_HOST:PORT
            # }
            assert isinstance(self.proxy, dict)
            session.proxies = self.proxy

        return session

    def __build_object_clients(self):
        """Creates and assigned API Objects to the class instance"""

        if GuildWars2Client.VERSION == 'v1':
            from gw2api.objects.api_version_1 import API_OBJECTS
        elif GuildWars2Client.VERSION == 'v2':
            from gw2api.objects.api_version_2 import API_OBJECTS
        else:
            raise ValueError('Unable to import API Objects, make '
                             'sure the version passed is valid - ' + GuildWars2Client.VERSION)

        objects = API_OBJECTS

        for object_ in objects:
            object_ = copy.copy(object_)
            object_.session = self.session
            setattr(self, object_.__class__.__name__.lower(), object_)

    def __repr__(self):
        return '<GuildWars2Client %s\nVersion: %s\nAPI Key: %s\nLanguage: %s\nProxy: %s\nVerify SSL?: %s>'\
             % (self.base_url, self.version, self.api_key, self.lang, self.proxy, self.verify_ssl)