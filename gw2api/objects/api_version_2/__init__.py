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
    pass


class AccountAchievements(BaseAPIv2Object):
    pass


class AccountBank(BaseAPIv2Object):
    pass


class AccountDungeons(BaseAPIv2Object):
    pass


class AccountDyes(BaseAPIv2Object):
    pass


class AccountFinishers(BaseAPIv2Object):
    pass


class AccountGliders(BaseAPIv2Object):
    pass


class AccountHomeCats(BaseAPIv2Object):
    pass


class AccountHomeNodes(BaseAPIv2Object):
    pass


class AccountInventory(BaseAPIv2Object):
    pass


class AccountMailCarriers(BaseAPIv2Object):
    pass


class AccountMasteries(BaseAPIv2Object):
    pass


class AccountMasteryPoints(BaseAPIv2Object):
    pass


class AccountMaterials(BaseAPIv2Object):
    pass


class AccountMinis(BaseAPIv2Object):
    pass


class AccountOutfits(BaseAPIv2Object):
    pass


class AccountPvPHeroes(BaseAPIv2Object):
    pass


class AccountRaids(BaseAPIv2Object):
    pass


class AccountRecipes(BaseAPIv2Object):
    pass


class AccountSkins(BaseAPIv2Object):
    pass


class AccountTitles(BaseAPIv2Object):
    pass


class AccountWallet(BaseAPIv2Object):
    pass


class Achievements(BaseAPIv2Object):
    pass


class AchievementsCategories(BaseAPIv2Object):
    pass


class AchievementsDaily(BaseAPIv2Object):
    pass


class AchievementsDailyTomorrow(BaseAPIv2Object):
    pass


class AchievementsGroups(BaseAPIv2Object):
    pass


class BackstoryAnswers(BaseAPIv2Object):
    pass


class BackstoryQuestions(BaseAPIv2Object):
    pass


class Build(BaseAPIv2Object):
    pass


class Cats(BaseAPIv2Object):
    pass


class Characters(BaseAPIv2Object):
    pass


class Colors(BaseAPIv2Object):
    pass


class CommerceDelivery(BaseAPIv2Object):
    pass


class CommerceExchange(BaseAPIv2Object):
    pass


class CommerceExchangeCoins(BaseAPIv2Object):
    pass


class CommerceExchangeGems(BaseAPIv2Object):
    pass


class CommerceListings(BaseAPIv2Object):
    pass


class CommercePrices(BaseAPIv2Object):
    pass


class CommerceTransactions(BaseAPIv2Object):
    pass


class Continents(BaseAPIv2Object):

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


class Currencies(BaseAPIv2Object):
    pass


class Dungeons(BaseAPIv2Object):
    pass


class Emblem(BaseAPIv2Object):
    pass


class Files(BaseAPIv2Object):
    pass


class Finishers(BaseAPIv2Object):
    pass


class Gliders(BaseAPIv2Object):
    pass


class GuildId(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdLog(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdMembers(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdRanks(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdStash(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdTeams(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdTreasury(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildIdUpgrades(BaseAPIv2Object):

    def get(self, id, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url = endpoint_url.replace(':id', id)

        return super().get(url=endpoint_url)


class GuildPermissions(BaseAPIv2Object):
    pass


class GuildSearch(BaseAPIv2Object):

    def get(self, name, **kwargs):
        endpoint_url = self._build_endpoint_base_url()
        endpoint_url += '?name={name}'.format(name=name)

        return super().get(url=endpoint_url)


class GuildUpgrades(BaseAPIv2Object):
    pass


class Items(BaseAPIv2Object):
    pass


class ItemStats(BaseAPIv2Object):
    pass


class Legends(BaseAPIv2Object):
    pass


class MailCarriers(BaseAPIv2Object):
    pass


class Maps(BaseAPIv2Object):
    pass


class Masteries(BaseAPIv2Object):
    pass


class Materials(BaseAPIv2Object):
    pass


class Minis(BaseAPIv2Object):
    pass


class Nodes(BaseAPIv2Object):
    pass


class Outfits(BaseAPIv2Object):
    pass


class Pets(BaseAPIv2Object):
    pass


class Professions(BaseAPIv2Object):
    pass


class PvP(BaseAPIv2Object):
    pass


class PvPAmulets(BaseAPIv2Object):
    pass


class PvPGames(BaseAPIv2Object):
    pass


class PvPHeroes(BaseAPIv2Object):
    pass


class PvPRanks(BaseAPIv2Object):
    pass


class PvPSeasons(BaseAPIv2Object):
    pass


class PvPSeasonsLeaderboards(BaseAPIv2Object):
    pass


class PvPStandings(BaseAPIv2Object):
    pass


class PvPStats(BaseAPIv2Object):
    pass


class Quaggans(BaseAPIv2Object):
    pass


class Races(BaseAPIv2Object):
    pass


class Raids(BaseAPIv2Object):
    pass


class Recipes(BaseAPIv2Object):
    pass


class RecipesSearch(BaseAPIv2Object):

    def get(self, **kwargs):
        if any(key in ['input', 'output'] for key in kwargs):
            param = 'input' if 'input' in kwargs else 'output'
            item_id = kwargs.get(param)

            endpoint_url = self._build_endpoint_base_url()
            endpoint_url += '?{param}={item_id}'.format(param=param, item_id=item_id)

            return super().get(url=endpoint_url)

        # Fallback to let the official API handle the error cases
        return super().get(**kwargs)


class Skills(BaseAPIv2Object):
    pass


class Skins(BaseAPIv2Object):
    pass


class Specializations(BaseAPIv2Object):
    pass


class Stories(BaseAPIv2Object):
    pass


class StoriesSeasons(BaseAPIv2Object):
    pass


class Titles(BaseAPIv2Object):
    pass


class Tokeninfo(BaseAPIv2Object):
    pass


class Traits(BaseAPIv2Object):
    pass


class Worlds(BaseAPIv2Object):
    pass


class Wvw(BaseAPIv2Object):
    pass


class WvwAbilities(BaseAPIv2Object):
    pass


class WvwMatches(BaseAPIv2Object):
    pass


class WvwMatchesStatsTeams(BaseAPIv2Object):
    pass


class WvwObjectives(BaseAPIv2Object):
    pass


class WvwRanks(BaseAPIv2Object):
    pass


class WvwUpgrades(BaseAPIv2Object):
    pass


API_OBJECTS = [Account('account'),
               AccountAchievements('account/achievements'),
               AccountBank('account/bank'),
               AccountDungeons('account/dungeons'),
               AccountDyes('account/dyes'),
               AccountFinishers('account/finishers'),
               AccountGliders('account/gliders'),
               AccountHomeCats('account/home/cats'),
               AccountHomeNodes('account/home/nodes'),
               AccountInventory('account/inventory'),
               AccountMailCarriers('account/mailcarriers'),
               AccountMasteries('account/masteries'),
               AccountMasteryPoints('account/mastery/points'),
               AccountMaterials('account/materials'),
               AccountMinis('account/minis'),
               AccountOutfits('account/outfits'),
               AccountPvPHeroes('account/pvp/heroes'),
               AccountRaids('account/raids'),
               AccountRecipes('account/recipes'),
               AccountSkins('account/skins'),
               AccountTitles('account/titles'),
               AccountWallet('account/wallet'),
               Achievements('achievements'),
               AchievementsCategories('achievements/categories'),
               AchievementsDaily('achievements/daily'),
               AchievementsDailyTomorrow('achievements/daily/tomorrow'),
               AchievementsGroups('achievements/groups'),
               BackstoryAnswers('backstory/answers'),
               BackstoryQuestions('backstory/questions'),
               Build('build'),
               Cats('cats'),
               Characters('characters'),
               Colors('colors'),
               CommerceDelivery('commerce/delivery'),
               CommerceExchange('commerce/exchange'),
               CommerceExchangeCoins('commerce/exchange/coins'),
               CommerceExchangeGems('commerce/exchange/gems'),
               CommerceListings('commerce/listings'),
               CommercePrices('commerce/prices'),
               CommerceTransactions('commerce/transactions'),
               Continents('continents'),
               Currencies('currencies'),
               Dungeons('dungeons'),
               Emblem('emblem'),
               Files('files'),
               Finishers('finishers'),
               Gliders('gliders'),
               GuildId('guild/:id'),
               GuildIdLog('guild/:id/log'),
               GuildIdMembers('guild/:id/members'),
               GuildIdRanks('guild/:id/ranks'),
               GuildIdStash('guild/:id/stash'),
               GuildIdTeams('guild/:id/teams'),
               GuildIdTreasury('guild/:id/treasury'),
               GuildIdUpgrades('guild/:id/upgrades'),
               GuildPermissions('guild/permissions'),
               GuildSearch('guild/search'),
               GuildUpgrades('guild/upgrades'),
               Items('items'),
               ItemStats('itemstats'),
               Legends('legends'),
               MailCarriers('mailcarriers'),
               Maps('maps'),
               Masteries('masteries'),
               Materials('materials'),
               Minis('minis'),
               Nodes('nodes'),
               Outfits('outfits'),
               Pets('pets'),
               Professions('professions'),
               PvP('pvp'),
               PvPAmulets('pvp/amulets'),
               PvPGames('pvp/games'),
               PvPHeroes('pvp/heroes'),
               PvPRanks('pvp/ranks'),
               PvPSeasons('pvp/seasons'),
               PvPSeasonsLeaderboards('pvp/seasons/leaderboards'),
               PvPStandings('pvp/standings'),
               PvPStats('pvp/stats'),
               Quaggans('quaggans'),
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
               Worlds('worlds'),
               Wvw('wvw'),
               WvwAbilities('wvw/abilities'),
               WvwMatches('wvw/matches'),
               WvwMatchesStatsTeams('wvw/matches/stats/teams'),
               WvwObjectives('wvw/objectives'),
               WvwRanks('wvw/ranks'),
               WvwUpgrades('wvw/upgrades')]
