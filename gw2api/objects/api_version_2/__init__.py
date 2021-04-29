from gw2api.objects.base_object import BaseAPIObject


class BaseAPIv2Object(BaseAPIObject):
    """Extends the base API handler to automatically handle pagination and id parameters"""

    def get(self, **kwargs):
        return super().get(id=kwargs.get('id'),
                           ids=kwargs.get('ids'),
                           url=kwargs.get('url'),
                           page=kwargs.get('page'),
                           page_size=kwargs.get('page_size')).json()


class Account(BaseAPIv2Object):
    """
        This returns information about the player's account.
        Authenticated Endpoint.
    """
    pass


class AccountAchievements(BaseAPIv2Object):
    """
        This returns information about the player's progress on achievements.
        Authenticated Endpoint.
    """
    pass


class AccountBank(BaseAPIv2Object):
    """
        This returns the items stored in a player's vault.
        Authenticated Endpoint.
    """
    pass


class AccountBuildStorage(BaseAPIv2Object):
    """
         This returns the templates stored in a player's build storage.
         Authenticated Endpoint.
     """
    pass


class AccountDailyCrafting(BaseAPIv2Object):
    """
         This returns information about time-gated recipes that have been crafted by the account since daily-reset.
         Authenticated Endpoint.
     """
    pass


class AccountDungeons(BaseAPIv2Object):
    """
         This resource returns the dungeons completed since daily dungeon reset.
         Authenticated Endpoint.
     """
    pass


class AccountDyes(BaseAPIv2Object):
    """
         This returns the unlocked dyes of the account.
         Authenticated Endpoint.
     """
    pass


class AccountEmote(BaseAPIv2Object):
    """
         This returns the player's unlocked emotes.
         Authenticated Endpoint.
     """
    pass


class AccountFinishers(BaseAPIv2Object):
    """
         This returns information about finishers that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountGliders(BaseAPIv2Object):
    """
         This returns information about gliders that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountHomeCats(BaseAPIv2Object):
    """
         This returns information about unlocked home instance cats.
         Authenticated Endpoint.
     """
    pass


class AccountHomeNodes(BaseAPIv2Object):
    """
         This returns information about unlocked home instance nodes.
         Authenticated Endpoint.
     """
    pass


class AccountInventory(BaseAPIv2Object):
    """
         This returns the shared inventory slots in an account.
         Authenticated Endpoint.
     """
    pass


class AccountLuck(BaseAPIv2Object):
    """
         This returns the total amount of luck consumed on an account.
         Authenticated Endpoint.
     """
    pass


class AccountMailCarriers(BaseAPIv2Object):
    """
         This returns information about mail carriers that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountMapChests(BaseAPIv2Object):
    """
         This returns information about Hero's Choice Chests acquired by the account since daily-reset.
         Authenticated Endpoint.
     """
    pass


class AccountMasteries(BaseAPIv2Object):
    """
         This returns information about masteries that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountMasteryPoints(BaseAPIv2Object):
    """
         This returns information about the total amount of masteries that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountMaterials(BaseAPIv2Object):
    """
         This returns the materials stored in a player's vault.
         Authenticated Endpoint.
     """
    pass


class AccountMinis(BaseAPIv2Object):
    """
         This returns the unlocked miniatures of the account.
         Authenticated Endpoint.
     """
    pass


class AccountMountsSkins(BaseAPIv2Object):
    """
         This returns the unlocked mount skins of the account.
         Authenticated Endpoint.
     """
    pass


class AccountMountsTypes(BaseAPIv2Object):
    """
         This returns the unlocked mounts of the account.
         Authenticated Endpoint.
     """
    pass


class AccountNovelties(BaseAPIv2Object):
    """
         This returns information about novelties that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountOutfits(BaseAPIv2Object):
    """
         This returns information about outfits that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountPvPHeroes(BaseAPIv2Object):
    """
         This returns information about pvp heroes that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountRaids(BaseAPIv2Object):
    """
         This returns the completed raid encounters since weekly raid reset.
         Authenticated Endpoint.
     """
    pass


class AccountRecipes(BaseAPIv2Object):
    """
         This returns information about recipes that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountSkins(BaseAPIv2Object):
    """
         This returns the unlocked skins of the account.
         Authenticated Endpoint.
     """
    pass


class AccountTitles(BaseAPIv2Object):
    """
         This returns information about titles that are unlocked for an account.
         Authenticated Endpoint.
     """
    pass


class AccountWallet(BaseAPIv2Object):
    """
         This returns the currencies of the account.
         Authenticated Endpoint.
     """
    pass


class AccountWorldBosses(BaseAPIv2Object):
    """
         This returns information about which world bosses have been killed by the account since daily-reset.
         Authenticated Endpoint.
     """
    pass


class Achievements(BaseAPIv2Object):
    """
        This returns all achievements in the game, including localized names and icons.
    """
    pass


class AchievementsCategories(BaseAPIv2Object):
    """
        This returns all the categories for achievements.
    """
    pass


class AchievementsDaily(BaseAPIv2Object):
    """
        This returns the current set of daily achievements.
    """
    pass


class AchievementsDailyTomorrow(BaseAPIv2Object):
    """
        This returns the next set of daily achievements.
    """
    pass


class AchievementsGroups(BaseAPIv2Object):
    """
        This returns all the top-level groups for achievements.
    """
    pass


class BackstoryAnswers(BaseAPIv2Object):
    """
        This returns information about the Biography answers that are in the game.
    """
    pass


class BackstoryQuestions(BaseAPIv2Object):
    """
        This returns information about the Biography questions that are in the game.
    """
    pass


class Build(BaseAPIv2Object):
    """
        This returns the current build id of the game.
    """
    pass


class Characters(BaseAPIv2Object):
    """
         This returns information about characters attached to a specific account.
         Authenticated Endpoint.
     """
    pass


class CharactersBackstory(BaseAPIv2Object):
    """
         This returns information about the backstory of a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersBuildTabs(BaseAPIv2Object):
    """
         This returns information about an accounts build template tabs.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersBuildTabsActive(BaseAPIv2Object):
    """
         This returns information about an accounts build template tabs.
         Only those flagged True in is_active are returned.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersCore(BaseAPIv2Object):
    """
         This returns core information about a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersCrafting(BaseAPIv2Object):
    """
         This returns information about the crafting disciplines available
         to a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersEquipment(BaseAPIv2Object):
    """
         This returns information about the equipment on a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersEquipmentTabs(BaseAPIv2Object):
    """
         This returns information about an accounts equipment template tabs.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersEquipmentTabsActive(BaseAPIv2Object):
    """
         This returns information about an accounts equipment template tabs.
         Only those flagged True in is_active are returned.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersHeroPoints(BaseAPIv2Object):
    """
         This returns information about the hero points obtained by a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersInventory(BaseAPIv2Object):
    """
         This returns information about the inventory of a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersQuests(BaseAPIv2Object):
    """
         This returns information about the quests selected that by a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersRecipes(BaseAPIv2Object):
    """
         This returns information about recipes that the given character can use.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersSab(BaseAPIv2Object):
    """
         This returns information about Super Adventure Box on a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersSkills(BaseAPIv2Object):
    """
         This returns information about the skills equipped on a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersSpecialization(BaseAPIv2Object):
    """
         This returns information about the specializations equipped on a character attached to a specific account.
         Authenticated Endpoint.
     """
    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class CharactersTraining(BaseAPIv2Object):
    """
         This returns information about the training of a character attached to a specific account.
         Authenticated Endpoint.
     """

    def get(self, char_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                char_id: string, the id of the character to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', char_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class Colors(BaseAPIv2Object):
    """
         This returns all dye colors in the game, including localized names and their color component information.
     """
    pass


class CommerceDelivery(BaseAPIv2Object):
    """
         This provides access to the current items and coins available for pickup on this account.
         Authenticated Endpoint.
     """
    pass


class CommerceExchangeCoins(BaseAPIv2Object):
    """Returns the current coins to gems exchange rate"""

    def get(self, quantity):
        """Returns the current coins to gems exchange rate

        Args:
            quantity: The number of coins to convert to gems

        Returns:
            The JSON response
        """

        endpoint_url = self._build_endpoint_base_url()
        endpoint_url += "?quantity=" + str(quantity)

        return super().get(url=endpoint_url)


class CommerceExchangeGems(BaseAPIv2Object):
    """Returns the current gems to coins exchange rate"""

    def get(self, quantity):
        """Returns the current gems to coins exchange rate

        Args:
            quantity: The number of gems to convert to coins

        Returns:
            The JSON response
        """
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url += "?quantity=" + str(quantity)

        return super().get(url=endpoint_url)


class CommerceListings(BaseAPIv2Object):
    """
         This returns current buy and sell listings from the trading post.
     """
    pass


class CommercePrices(BaseAPIv2Object):
    """
         This returns current aggregated buy and sell listing information from the trading post.
     """
    pass


class CommerceTransactions(BaseAPIv2Object):
    """Returns information on an account's past and current trading post transactions"""
    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, val):
        self._session = val
        self.history.session = val
        self.current.session = val
        self.history.buys.session = val
        self.history.sells.session = val        
        self.current.buys.session = val
        self.current.sells.session = val

    def __init__(self, object_type):
        """
        Initializes a CommerceTransactions API object. See BaseAPIObject's __init__ documentation

        :param object_type: String indicating what type of object to
                             interface with (i.e. 'guild'). Primarily
                             acts as the relative path to the base URL
        :raises ValueError: In the event that either a `Session` object
                             or `object_type` are not set.
        """

        self._session = None

        # create second-level endpoints
        self.history = BaseAPIv2Object(object_type + "/history")
        self.current = BaseAPIv2Object(object_type + "/current")

        # create third-level endpoints
        self.history.buys = BaseAPIv2Object(self.history.object_type + "/buys")
        self.history.sells = BaseAPIv2Object(self.history.object_type + "/sells")
        self.current.buys = BaseAPIv2Object(self.current.object_type + "/buys")
        self.current.sells = BaseAPIv2Object(self.current.object_type + "/sells")

        super().__init__(object_type)


class Continents(BaseAPIv2Object):
    """
        This returns static information about the
        continents, floors, regions, maps, sectors, points of interest and tasks.
    """
    def _validate_kwargs(self, **kwargs):
        """Validates the keyword arguments.

        Since the continents endpoint is hierarchical, each level is dependent
        on its predecessor.

        Hence, the validation checks for the leaf supplied and walks up the
        tree to see if
        1. any higher level is missing
        2. any higher level supplies multiple ids
        In either case, a KeyError is raised.

        Special care is taken of the 'id' and 'ids' keywords, as those
        are synonymous for continents.

        Args:
            kwargs: The keyword arguments to validate.

        Raises:
            KeyError: if any needed level is missing, or any non-leaf level
            provides multiple IDs.
        """
        def raise_for_non_int(value):
            try:
                int(str(value))
            except ValueError:
                raise KeyError('too many ids supplied for {}'.format(level))

        levels = ['sectors', 'maps', 'regions', 'floors', 'continents']
        for i, current_level in enumerate(levels):
            if current_level in kwargs:
                for level in reversed(levels[i+1:]):  # All higher levels
                    if level not in kwargs:  # Check if level is supplied
                        if level != 'continents':  # Backwards compatibility for ids
                            raise KeyError('Please provide the {} key.'.format(level))
                        else:
                            if 'id' not in kwargs:
                                raise KeyError('Please provide the continents key.')
                    else:  # Check if no higher level supplies multiple IDs
                        if level != 'continents':
                            raise_for_non_int(kwargs.get(level))
                        else:  # Backwards compatibility for ids
                            value = kwargs.get(level) or kwargs.get('ids')
                            raise_for_non_int(value)

    def get(self, **kwargs):
        """Gets the continents resource.

        This resource is slightly different than other API resources, hence
        its differs slightly. Instead of using the id and ids attributes,
        this resource can walk along several levels:
            continents, floors, regions, maps, sectors

        For each layer, individual (single) IDs can be specified.
        For the leaf layer, i.e. the last specified layer, multiple IDs
        can be specified.

        If one layer is specified, all previous layers must be specified, too.
        For example, if specifying regions=38, then floors and continents need
        to be supplied, too.

        Args:
            kwargs: Can be any combination of
                    - continents
                    - floors
                    - regions
                    - maps
                    - sectors
                    With values being either single ints (ids), lists of ints,
                    or strings. A special case is 'all', which can be used
                    to get a list of all ids in a subresource.
        Returns:
            The JSON response.

        Raises:
            KeyError: if the validation of the keyword arguments fails.
        """
        request_url = self._build_endpoint_base_url()

        self._validate_kwargs(**kwargs)

        _id = kwargs.get('id')
        ids = kwargs.get('ids')
        continents = kwargs.get('continents') or ids or _id
        floors = kwargs.get('floors')
        regions = kwargs.get('regions')
        maps = kwargs.get('maps')
        sectors = kwargs.get('sectors')

        def id_string(value_or_values):
            if value_or_values == 'all':
                return ''
            if isinstance(value_or_values, str):
                if ',' in value_or_values:
                    return '?ids=' + value_or_values
                return '/' + value_or_values
            try:
                return '?ids=' + ','.join(map(str, value_or_values))
            except TypeError:  # single values are not iterable
                return '/' + str(value_or_values)

        # Since we validate before, we just have to build the url in order
        # not nested
        if continents:
            request_url += id_string(continents)
        if floors:
            request_url += '/floors' + id_string(floors)
        if regions:
            request_url += '/regions' + id_string(regions)
        if maps:
            request_url += '/maps' + id_string(maps)
        if sectors:
            request_url += '/sectors' + id_string(sectors)

        return super().get(url=request_url)


class CreateSubToken(BaseAPIv2Object):
    """
        This allows for the creation of Subtokens; essentially API keys with a more limited set of permissions,
        which can be used as a substitute for them.
        Authenticated Endpoint.
    """
    def get(self, expire, permissions,  **kwargs):
        """
             This appends the match_id and guild_id to the endpoint and then passes it to the parent get() function.
             Returns None if it fails to append expire datem, permissions, or urls.

             Args:
                 expire: datetime, the date and time when the subtoken expires
                 permissions: list, collection of permissions for subtoken to inherit
                 **kwargs:
                    urls: list, Endpoints that will be accessible using this Subtoken.
         """
        endpoint_url = self._build_endpoint_base_url() + '?'

        try:
            endpoint_url += f'expire={expire.isoformat()}&'
        except AttributeError:
            print('expire param must be of type datetime.')
            return None

        try:
            endpoint_url += 'permissions=' + ','.join([str(_) for _ in permissions]) + '&'
        except TypeError:
            print("Could not add permissions because the given permissions argument is not an iterable.")
            return None

        urls = kwargs.get('urls')
        if urls:
            try:
                endpoint_url += 'urls=' + ','.join([str(_) for _ in urls]) + '&'
            except TypeError:
                print("Could not add urls because the given urls argument is not an iterable.")
                return None

        return super().get(url=endpoint_url, **kwargs)
    pass


class Currencies(BaseAPIv2Object):
    """
        This returns a list of the currencies contained in the account wallet.
    """
    pass


class DailyCrafting(BaseAPIv2Object):
    """
        This returns information about time-gated recipes that can be crafted in-game.
    """
    pass


class Dungeons(BaseAPIv2Object):
    """
        This returns details about each dungeon and it's associated paths.
    """
    pass


class EmblemBackgrounds(BaseAPIv2Object):
    """
        This returns image resources that are needed to render the background of guild emblems.
    """
    pass


class EmblemForegrounds(BaseAPIv2Object):
    """
        This returns image resources that are needed to render the foreground of guild emblems.
    """
    pass


class Emotes(BaseAPIv2Object):
    """
        This returns information about unlockable emotes.
    """
    pass


class Files(BaseAPIv2Object):
    """
        This returns commonly requested in-game assets that may be used to enhance API-derived applications.
    """
    pass


class Finishers(BaseAPIv2Object):
    """
        This returns information about finishers that are available in-game.
    """
    pass


class Gliders(BaseAPIv2Object):
    """
        This returns information about gliders that are available in-game.
    """
    pass


class GuildId(BaseAPIv2Object):
    """
        This returns core details about a given guild.
        The end point will include more or less fields dependent on whether or not an API Key of a
        Leader or Member of the Guild with the guilds scope is included in the Request.
        Authenticated Endpoint.
    """
    def get(self, guild_id, **kwargs):
        """
            This appends the 'id' to the endpoint and then passes it to the parent get() function.

            Args:
                guild_id: string, the id of the guild to add to the endpoint.
        """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', guild_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildIdLog(BaseAPIv2Object):
    """
        This returns information about certain events in a guild's log.
        The endpoint requires the scope guilds, and will only work if the API key is from the guild leader's account.
        Authenticated Endpoint.
    """
    def get(self, guild_id, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.

             Args:
                 guild_id: string, the id of the guild to add to the endpoint.
                 **kwargs:
                    since: int, the id to use as a ceiling for return values.
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url = endpoint_url.replace(':id', guild_id)

            since = kwargs.get('since')
            if since:
                endpoint_url += f'?since=={since}'

        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildIdMembers(BaseAPIv2Object):
    """
        This returns information about the members of a specified guild.
        The endpoint requires the scope guilds, and will only work if the API key is from the guild leader's account.
        Authenticated Endpoint.
    """
    def get(self, guild_id, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.

             Args:
                 guild_id: string, the id of the guild to add to the endpoint.
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url = endpoint_url.replace(':id', guild_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildIdRanks(BaseAPIv2Object):
    """
        This returns information about the ranks of a specified guild.
        The endpoint requires the scope guilds, and will only work if the API key is from the guild leader's account.
        Authenticated Endpoint.
    """
    def get(self, guild_id, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.

             Args:
                 guild_id: string, the id of the guild to add to the endpoint.
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url = endpoint_url.replace(':id', guild_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildIdStash(BaseAPIv2Object):
    """
        This returns information about the items in a guild's vault.
        The endpoint requires the scope guilds, and will only work if the API key is from the guild leader's account.
        Authenticated Endpoint.
    """
    def get(self, guild_id, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.

             Args:
                 guild_id: string, the id of the guild to add to the endpoint.
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url = endpoint_url.replace(':id', guild_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildIdStorage(BaseAPIv2Object):
    """
        This returns information about the items in a guild's storage.
        The endpoint requires the scope guilds, and will only work if the API key is from the guild leader's account.
        Authenticated Endpoint.
    """
    def get(self, guild_id, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.

             Args:
                 guild_id: string, the id of the guild to add to the endpoint.
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url = endpoint_url.replace(':id', guild_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildIdTeams(BaseAPIv2Object):
    """
        This returns information about the teams in a guild.
        The endpoint requires the scope guilds, and will only work if the API key is from the guild leader's account.
        Authenticated Endpoint.
    """
    def get(self, guild_id, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.

             Args:
                 guild_id: string, the id of the guild to add to the endpoint.
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url = endpoint_url.replace(':id', guild_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildIdTreasury(BaseAPIv2Object):
    """
        This returns information about the items in a guild's treasury.
        The endpoint requires the scope guilds, and will only work if the API key is from the guild leader's account.
        Authenticated Endpoint.
    """
    def get(self, guild_id, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.

             Args:
                 guild_id: string, the id of the guild to add to the endpoint.w.
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url = endpoint_url.replace(':id', guild_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildIdUpgrades(BaseAPIv2Object):
    """
        This returns information about the guild's upgrades.
        The endpoint requires the scope guilds, and will only work if the API key is from the guild leader's account.
        Authenticated Endpoint.
    """
    def get(self, guild_id, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.

             Args:
                 guild_id: string, the id of the guild to add to the endpoint.
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url = endpoint_url.replace(':id', guild_id)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildPermissions(BaseAPIv2Object):
    """
        This resource returns information about all guild permissions.
    """
    pass


class GuildSearch(BaseAPIv2Object):
    """
        The endpoint an array, each value being a string of the guild id for the given name.
    """
    def get(self, name, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.

             name: string, the name of the guild to add to the endpoint.
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url += '?name={name}'.format(name=name)
        except TypeError:
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class GuildUpgrades(BaseAPIv2Object):
    """
        This returns information about all available Guild Hall upgrades, including scribe decorations.
    """
    pass


class HomeCats(BaseAPIv2Object):
    """
        This returns an array of ids for cats available for the home instance.
    """
    pass


class HomeNodes(BaseAPIv2Object):
    """
        This returns an array of ids for all currently available home instance nodes.
    """
    pass


class Items(BaseAPIv2Object):
    """
        This returns information about items that were discovered by players in the game.
    """
    pass


class ItemStats(BaseAPIv2Object):
    """
        This returns information about itemstats for items that are in the game.
    """
    pass


class Legends(BaseAPIv2Object):
    """
        This returns information about the Revenant Legends that are in the game.
    """
    pass


class MailCarriers(BaseAPIv2Object):
    """
        This returns information about mail carriers that are available in-game.
    """
    pass


class MapChests(BaseAPIv2Object):
    """
        This returns information about Hero's Choice Chests that can be be acquired once a day in-game.
    """
    pass


class Maps(BaseAPIv2Object):
    """
        This resource returns details about maps in the game, including details about
        floor and translation data on how to translate between world coordinates and map coordinates.
    """
    pass


class Masteries(BaseAPIv2Object):
    """
        This returns information about masteries that are available in-game.
    """
    pass


class Materials(BaseAPIv2Object):
    """
        This returns information about the categories in material storage.
    """
    pass


class Minis(BaseAPIv2Object):
    """
        This returns all minis in the game.
    """
    pass


class MountsSkins(BaseAPIv2Object):
    """
        This returns information about mount skins that are available in-game.
    """
    pass


class MountsTypes(BaseAPIv2Object):
    """
        This returns information about mount types that are available in-game.
    """
    pass


class Novelties(BaseAPIv2Object):
    """
        This returns information about novelties that are available in-game.
    """
    pass


class Outfits(BaseAPIv2Object):
    """
        This returns information about the outfits that are in the game.
    """
    pass


class Pets(BaseAPIv2Object):
    """
        This returns information about the Ranger pets that are in the game.
    """
    pass


class Professions(BaseAPIv2Object):
    """
        This returns information about professions that are in the game.
    """
    pass


class PvPAmulets(BaseAPIv2Object):
    """
        This returns information about the PvP amulets that are in the game.
    """
    pass


class PvPGames(BaseAPIv2Object):
    """
        This returns information about past PvP matches the player has participated in.
        Authenticated Endpoint.
    """
    pass


class PvPHeroes(BaseAPIv2Object):
    """
        This returns information about pvp heroes that are available in-game.
    """
    pass


class PvPRanks(BaseAPIv2Object):
    """
        This information about the available ranks in the Player versus Player game mode.
    """
    pass


class PvPSeasons(BaseAPIv2Object):
    """
        This returns information about League seasons.
    """
    pass


class PvPSeasonsLeaderboards(BaseAPIv2Object):
    """
        This returns information about League season leaderboards for either NA or EU.
    """
    def get(self, season_id, **kwargs):
        """
             This appends the 'id' to the endpoint and then passes it to the parent get() function.
             Appends board and region if they are supplied

             Args:
                 season_id: string, the id of the guild to add to the endpoint.
                 **kwargs
                    board: string, type of leaderboard to get. I.E. 'legendary'
                    region: string, the region to get leaderboard of. I.E. 'eu/na
         """
        try:
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url = endpoint_url.replace(':id', season_id)
        except TypeError:
            return super().get(**kwargs)

        board = kwargs.get('board')
        if board:
            try:
                endpoint_url += f'/{board}'
            except TypeError:
                print("Failed to add board. Ensure it is of type string")
                return None

        region = kwargs.get('region')
        if region:
            try:
                endpoint_url += f'/{region}'
            except TypeError:
                print("Failed to add region. Ensure it is of type string")
                return None

        return super().get(url=endpoint_url, **kwargs)


class PvPStandings(BaseAPIv2Object):
    """
        This returns information about player pips.
        Authenticated Endpoint.
    """
    pass


class PvPStats(BaseAPIv2Object):
    """
        This returns information about wins and losses in the account's PvP matches.
        Authenticated Endpoint.
    """
    pass


class Quaggans(BaseAPIv2Object):
    """
          This returns quaggan images.
      """
    pass


class Quests(BaseAPIv2Object):
    """
          This resource returns information about Story Journal missions within the personal story and Living World.
      """
    pass


class Races(BaseAPIv2Object):
    """
          This returns information about the different playable races.
      """
    pass


class Raids(BaseAPIv2Object):
    """
          This returns details about each raid and it's associated wings.
      """
    pass


class Recipes(BaseAPIv2Object):
    """
          This returns information about recipes that were discovered by players in the game.
      """
    pass


class RecipesSearch(BaseAPIv2Object):
    """
          This allows searching for recipe.
          To get additional information about the returned recipes, use the recipes endpoint.
      """

    def get(self, **kwargs):
        """
            If either 'input' or 'output' is passed into **kwargs
            , then append item id and the given param into the endpoint.
        Args:
            **kwargs: dict, dictionary of key word arguments.

        Returns:
            List of recipe ids that match the query or None if input/output cant be converted to strings
        """
        if any(key in ['input', 'output'] for key in kwargs):
            param = 'input' if 'input' in kwargs else 'output'
            item_id = kwargs.get(param)
            endpoint_url = self._build_endpoint_base_url()
            endpoint_url += '?{param}={item_id}'.format(param=param, item_id=item_id)

            return super().get(url=endpoint_url)

        # Fallback to let the official API handle the error cases
        return super().get(**kwargs)


class Skills(BaseAPIv2Object):
    """
        This returns information about skills usable by players in the game.
    """
    pass


class Skins(BaseAPIv2Object):
    """
        This returns information about skins that were discovered by players in the game.
    """
    pass


class Specializations(BaseAPIv2Object):
    """
        This returns information on currently released specializations.
    """
    pass


class Stories(BaseAPIv2Object):
    """
        This returns information about the Story Journal stories; including the personal story and Living World.
    """
    pass


class StoriesSeasons(BaseAPIv2Object):
    """
        This returns information about the Story Journal story seasons; including the personal story and Living World.
    """
    pass


class Titles(BaseAPIv2Object):
    """
        This returns information about the titles that are in the game.
    """
    pass


class Tokeninfo(BaseAPIv2Object):
    """
        This resource returns information about the supplied API key.
        Authenticated Endpoint.
    """
    pass


class Traits(BaseAPIv2Object):
    """
        This returns information about specific traits which are contained within specializations.
    """
    pass


class WorldBosses(BaseAPIv2Object):
    """
        This returns information about scheduled World bosses in Core Tyria that reward boss chests
        that can be be opened once a day in-game.
    """
    pass


class Worlds(BaseAPIv2Object):
    """
        This returns information about the available worlds, or servers.
    """
    pass


class WvwAbilities(BaseAPIv2Object):
    """
        This returns information about the available abilities in the World versus World game mode.
    """
    pass


class WvwMatches(BaseAPIv2Object):
    """
        This returns either an array of matches or further details about a specified match.
    """
    pass


class WvwMatchesOverview(BaseAPIv2Object):
    """
        This returns either an array of matches or further details about a specified match.
    """
    pass


class WvwMatchesScores(BaseAPIv2Object):
    """
        This returns either an array of match overviews or further details about a specified match.
    """
    pass


class WvwMatchesStats(BaseAPIv2Object):
    """
        This returns either an array of match stats or further details about a specified match.
    """
    pass


class WvwMatchesStatsGuilds(BaseAPIv2Object):
    """
        This returns specific details pertaining to guilds and their WVW stats.
    """
    def get(self, match_id, guild_id, **kwargs):
        """
             This appends the match_id and guild_id to the endpoint and then passes it to the parent get() function.

             Args:
                 guild_id: string, the id of the guild to add to the endpoint.
                 match_id: int, the ID of the match.
         """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', match_id)
            endpoint_url = endpoint_url.replace(':guild_id', guild_id)
        except TypeError:
            print('Failed to set match id or guild id. Ensure they are both strings.')
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class WvwMatchesStatsTeamsKDR(BaseAPIv2Object):
    """
        This returns specific details pertaining to teams and their KDR.
    """

    def get(self, match_id, team_id, **kwargs):
        """
             This appends the match_id and team_id to the endpoint and then passes it to the parent get() function.
             Returns None if it fails to append the ids.

             Args:
                 match_id: int, the ID of the match.
                 team_id: string, the id of the guild to add to the endpoint.
         """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', match_id)
            endpoint_url = endpoint_url.replace(':team', team_id)
        except TypeError:
            print('Failed to set match id or team id. Ensure they are both strings.')
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class WvwMatchesStatsTeamsKills(BaseAPIv2Object):
    """
        This returns specific details pertaining to teams and their kills.
    """
    def get(self, match_id, team_id, **kwargs):
        """
             This appends the match_id and team_id to the endpoint and then passes it to the parent get() function.

             Args:
                 match_id: int, the ID of the match.
                 team_id: string, the id of the guild to add to the endpoint.
         """
        endpoint_url = self._build_endpoint_base_url()
        try:
            endpoint_url = endpoint_url.replace(':id', match_id)
            endpoint_url = endpoint_url.replace(':team', team_id)
        except TypeError:
            print('Failed to set match id or team id. Ensure they are both strings.')
            return super().get(**kwargs)

        return super().get(url=endpoint_url, **kwargs)


class WvwObjectives(BaseAPIv2Object):
    """
        This returns details about World vs. World objectives such as camps, towers, and keeps.
    """
    pass


class WvwRanks(BaseAPIv2Object):
    """
        This returns information about the available ranks in the World versus World game mode.
    """
    pass


class WvwUpgrades(BaseAPIv2Object):
    """
        This returns details about available World vs. World upgrades for objectives such as camps, towers, and keeps.
    """
    pass


API_OBJECTS = [Account('account'),
               AccountAchievements('account/achievements'),
               AccountBank('account/bank'),
               AccountBuildStorage('account/buildstorage'),
               AccountDailyCrafting('account/dailycrafting'),
               AccountDungeons('account/dungeons'),
               AccountDyes('account/dyes'),
               AccountEmote('account/emotes'),
               AccountFinishers('account/finishers'),
               AccountGliders('account/gliders'),
               AccountHomeCats('account/home/cats'),
               AccountHomeNodes('account/home/nodes'),
               AccountInventory('account/inventory'),
               AccountLuck('account/luck'),
               AccountMailCarriers('account/mailcarriers'),
               AccountMapChests('account/mapchests'),
               AccountMasteries('account/masteries'),
               AccountMasteryPoints('account/mastery/points'),
               AccountMaterials('account/materials'),
               AccountMinis('account/minis'),
               AccountMountsSkins('account/mounts/skins'),
               AccountMountsTypes('account/mounts/types'),
               AccountNovelties('account/novelties'),
               AccountOutfits('account/outfits'),
               AccountPvPHeroes('account/pvp/heroes'),
               AccountRaids('account/raids'),
               AccountRecipes('account/recipes'),
               AccountSkins('account/skins'),
               AccountTitles('account/titles'),
               AccountWallet('account/wallet'),
               AccountWorldBosses('account/worldbosses'),
               Achievements('achievements'),
               AchievementsCategories('achievements/categories'),
               AchievementsDaily('achievements/daily'),
               AchievementsDailyTomorrow('achievements/daily/tomorrow'),
               AchievementsGroups('achievements/groups'),
               BackstoryAnswers('backstory/answers'),
               BackstoryQuestions('backstory/questions'),
               Build('build'),
               Characters('characters'),
               CharactersBackstory('characters/:id/backstory'),
               CharactersBuildTabs('characters/:id/buildtabs'),
               CharactersBuildTabsActive('characters/:id/buildtabs/active'),
               CharactersCore('characters/:id/core'),
               CharactersCrafting('characters/:id/crafting'),
               CharactersEquipment('characters/:id/equipment'),
               CharactersEquipmentTabs('characters/:id/equipmenttabs'),
               CharactersEquipmentTabsActive('characters/:id/equipmenttabs/active'),
               CharactersHeroPoints('characters/:id/heropoints'),
               CharactersInventory('characters/:id/inventory'),
               CharactersQuests('characters/:id/quests'),
               CharactersRecipes('characters/:id/recipes'),
               CharactersSab('characters/:id/sab'),
               CharactersSkills('characters/:id/skills'),
               CharactersSpecialization('characters/:id/specializations'),
               CharactersTraining('characters/:id/training'),
               Colors('colors'),
               CommerceDelivery('commerce/delivery'),
               CommerceExchangeCoins('commerce/exchange/coins'),
               CommerceExchangeGems('commerce/exchange/gems'),
               CommerceListings('commerce/listings'),
               CommercePrices('commerce/prices'),
               CommerceTransactions('commerce/transactions'),
               Continents('continents'),
               CreateSubToken('createsubtoken'),
               Currencies('currencies'),
               DailyCrafting('dailycrafting'),
               Dungeons('dungeons'),
               EmblemBackgrounds('emblem/backgrounds'),
               EmblemForegrounds('emblem/foregrounds'),
               Emotes('emotes'),
               Files('files'),
               Finishers('finishers'),
               Gliders('gliders'),
               GuildId('guild/:id'),
               GuildIdLog('guild/:id/log'),
               GuildIdMembers('guild/:id/members'),
               GuildIdRanks('guild/:id/ranks'),
               GuildIdStash('guild/:id/stash'),
               GuildIdStorage('guild/:id/storage'),
               GuildIdTeams('guild/:id/teams'),
               GuildIdTreasury('guild/:id/treasury'),
               GuildIdUpgrades('guild/:id/upgrades'),
               GuildPermissions('guild/permissions'),
               GuildSearch('guild/search'),
               GuildUpgrades('guild/upgrades'),
               HomeCats('home/cats'),
               HomeNodes('home/nodes'),
               Items('items'),
               ItemStats('itemstats'),
               Legends('legends'),
               MailCarriers('mailcarriers'),
               MapChests('mapchests'),
               Maps('maps'),
               Masteries('masteries'),
               Materials('materials'),
               Minis('minis'),
               MountsSkins('mounts/skins'),
               MountsTypes('mounts/types'),
               Novelties('novelties'),
               Outfits('outfits'),
               Pets('pets'),
               Professions('professions'),
               PvPAmulets('pvp/amulets'),
               PvPGames('pvp/games'),
               PvPHeroes('pvp/heroes'),
               PvPRanks('pvp/ranks'),
               PvPSeasons('pvp/seasons'),
               PvPSeasonsLeaderboards('pvp/seasons/:id/leaderboards'),
               PvPStandings('pvp/standings'),
               PvPStats('pvp/stats'),
               Quaggans('quaggans'),
               Quests('quests'),
               Races('races'),
               Raids('raids'),
               Recipes('recipes'),
               RecipesSearch('recipes/search'),
               Skills('skills'),
               Skins('skins'),
               Specializations('specializations'),
               Stories('stories'),
               StoriesSeasons('stories/seasons'),
               Titles('titles'),
               Tokeninfo('tokeninfo'),
               Traits('traits'),
               WorldBosses('worldbosses'),
               Worlds('worlds'),
               WvwAbilities('wvw/abilities'),
               WvwMatches('wvw/matches'),
               WvwMatchesOverview('wvw/matches/overview'),
               WvwMatchesScores('wvw/matches/scores'),
               WvwMatchesStats('wvw/matches/stats'),
               WvwMatchesStatsGuilds('wvw/matches/stats/:id/guilds/:guild_id'),
               WvwMatchesStatsTeamsKDR('wvw/matches/stats/:id/teams/:team/top/kdr'),
               WvwMatchesStatsTeamsKills('wvw/matches/stats/:id/teams/:team/top/kills'),
               WvwObjectives('wvw/objectives'),
               WvwRanks('wvw/ranks'),
               WvwUpgrades('wvw/upgrades')]
