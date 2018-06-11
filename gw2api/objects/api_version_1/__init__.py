from gw2api.objects.base_object import BaseAPIObject


class Build(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json().get('build_id')


class Colors(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json().get('colors')


class Continents(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json().get('continents')


class EventDetails(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json().get('events')


class EventNames(BaseAPIObject):
    """Undocumented Deprecation - Endpoint now disabled"""
    def get(self, world_id=None, map_id=None, event_id=None):
        raise DeprecationWarning("Endpoint is disabled")


class Events(BaseAPIObject):
    """Deprecated Endpoint, see - https://wiki.guildwars2.com/wiki/API:1/events"""
    def get(self, world_id=None, map_id=None, event_id=None):
        raise DeprecationWarning("Endpoint is disabled")


class Files(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json()


class GuildDetails(BaseAPIObject):

    def get(self, guild_id=None, guild_name=None):
        """
        Only one of the parameters is required here.
        If both parameters are passed, the `guild_id` takes precedence.

        Additionally, `guild_id` must follow the following format (UUID):

        XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

        e.g. 75FD83CF-0C45-4834-BC4C-097F93A487AF
        """
        endpoint_url = self._build_endpoint_base_url() + '?'

        if not (guild_id or guild_name):
            raise ValueError('No Guild ID or Guild name has been passed')

        if guild_id:
            endpoint_url += 'guild_id=%s&' % guild_id

        if guild_name:
            endpoint_url += 'guild_name=%s' % guild_name

        endpoint_url.rstrip('&')

        response = self.session.get(endpoint_url)
        return response.json()


class Items(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json().get('items')


class ItemDetails(BaseAPIObject):

    def get(self, item_id):
        endpoint_url = self._build_endpoint_base_url() + '?item_id=%s' % item_id
        response = self.session.get(endpoint_url)
        return response.json()


class Maps(BaseAPIObject):

    def get(self, map_id=None):
        endpoint_url = self._build_endpoint_base_url()

        if map_id:
            endpoint_url += '?%s' % map_id

        response = self.session.get(endpoint_url)
        return response.json().get('maps')


class MapNames(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json()


class MapFloor(BaseAPIObject):

    def get(self, continent_id, floor):
        endpoint_url = self._build_endpoint_base_url() + '?continent_id=%s&floor=%s' % (continent_id, floor)
        response = self.session.get(endpoint_url)
        return response.json()


class Recipes(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json().get('recipes')


class RecipeDetails(BaseAPIObject):

    def get(self, recipe_id):
        endpoint_url = self._build_endpoint_base_url() + '?recipe_id=%s' % recipe_id
        response = self.session.get(endpoint_url)
        return response.json()


class Skins(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json().get('skins')


class SkinDetails(BaseAPIObject):

    def get(self, skin_id):
        endpoint_url = self._build_endpoint_base_url() + '?skin_id=%s' % skin_id
        response = self.session.get(endpoint_url)
        return response.json()


class WorldNames(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json()


class WvWMatches(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json().get('wvw_matches')


class WvWMatchDetails(BaseAPIObject):

    def get(self, match_id):
        endpoint_url = self._build_endpoint_base_url() + '?match_id=%s' % match_id
        response = self.session.get(endpoint_url)
        return response.json()


class WvWObjectiveNames(BaseAPIObject):

    def get(self):
        response = super().get()
        return response.json()


API_OBJECTS = [Build('build'),
               Colors('colors'),
               Continents('continents'),
               EventDetails('event_details'),
               Files('files'),
               GuildDetails('guild_details'),
               ItemDetails('item_details'),
               Items('items'),
               MapFloor('map_floor'),
               MapNames('map_names'),
               Maps('maps'),
               RecipeDetails('recipe_details'),
               Recipes('recipes'),
               SkinDetails('skin_details'),
               Skins('skins'),
               WorldNames('world_names'),
               WvWMatchDetails('wvw/match_details'),
               WvWMatches('wvw/matches'),
               WvWObjectiveNames('wvw/objective_names')]
