from client.objects.base_object import BaseAPIObject


class BaseAPIv2Object(BaseAPIObject):
    """Extends the base API handler to automatically handle pagination"""

    def get(self, **kwargs):
        return super().get(id=kwargs.get('id'),
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
               Colors('colors')]
