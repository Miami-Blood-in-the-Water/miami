from django.db.models import Model, CASCADE, OneToOneField, CharField, IntegerField, ForeignKey
from evennia.accounts.models import AccountDB
from evennia.objects.models import ObjectDB
from model_utils.managers import InheritanceManager


class Character(Model):
    objects = InheritanceManager()

    character = OneToOneField(ObjectDB, on_delete=CASCADE, primary_key=True)
    account = ForeignKey(AccountDB, on_delete=CASCADE, null=True)

    type = CharField(max_length=16, null=True, blank=True, editable=False)

    @property
    def name(self):
        return self.character.name

    def save(self, *args, **kwargs):
        self.type = self.__class__.__name__.lower()
        super(Character, self).save(*args, **kwargs)

    strength = IntegerField(default=1)
    dexterity = IntegerField(default=1)
    stamina = IntegerField(default=1)
    intelligence = IntegerField(default=1)
    wits = IntegerField(default=1)
    resolve = IntegerField(default=1)
    presence = IntegerField(default=1)
    manipulation = IntegerField(default=1)
    composure = IntegerField(default=1)

    academics = IntegerField(default=0)
    computer = IntegerField(default=0)
    crafts = IntegerField(default=0)
    investigation = IntegerField(default=0)
    medicine = IntegerField(default=0)
    occult = IntegerField(default=0)
    politics = IntegerField(default=0)
    science = IntegerField(default=0)
    athletics = IntegerField(default=0)
    brawl = IntegerField(default=0)
    drive = IntegerField(default=0)
    firearms = IntegerField(default=0)
    larceny = IntegerField(default=0)
    stealth = IntegerField(default=0)
    survival = IntegerField(default=0)
    weaponry = IntegerField(default=0)
    animal_ken = IntegerField(default=0)
    empathy = IntegerField(default=0)
    expression = IntegerField(default=0)
    intimidation = IntegerField(default=0)
    persuasion = IntegerField(default=0)
    socialize = IntegerField(default=0)
    streetwise = IntegerField(default=0)
    subterfuge = IntegerField(default=0)

    size = IntegerField(default=5)

    temporary_willpower = IntegerField(default=0)
    permanent_willpower = IntegerField(default=0)

    @property
    def maximum_willpower(self):
        return self.get('wits') + self.get('resolve') - self.permanent_willpower

    @property
    def current_willpower(self):
        return self.maximum_willpower - self.temporary_willpower

    bashing = IntegerField(default=0)
    lethal = IntegerField(default=0)
    aggravated = IntegerField(default=0)

    @property
    def maximum_health(self):
        return self.get('size') + self.get('stamina') + self.get_bonuses('health')

    @property
    def undamaged(self):
        return max(self.maximum_health - self.bashing - self.lethal - self.aggravated, 0)

    @property
    def speed(self):
        return 5 + self.get('strength') + self.get('dexterity')

    @property
    def initiative(self):
        return self.get('dexterity') + self.get('composure')

    @property
    def defense(self):
        return min(self.get('dexterity'), self.get('wits')) + self.get('athletics')

    def get(self, stat):
        current = getattr(self, stat)
        if isinstance(current, int):
            return current + self.get_bonuses(stat)
        else:
            return current

    def get_bonuses(self, stat):
        return 0

    def display_stat(self, name, width=20):
        display_name = name.replace('_', ' ')
        display_name = display_name.title()
        display_name = display_name.ljust(width - 2)
        value = self.get(name)
        return f'{display_name} {value}'

    @property
    def display_attributes(self):
        return f"""
        {self.display_stat('intelligence')} {self.display_stat('strength')} {self.display_stat('presence')}
        {self.display_stat('wits')} {self.display_stat('dexterity')} {self.display_stat('manipulation')}
        {self.display_stat('resolve')} {self.display_stat('stamina')} {self.display_stat('composure')}
        """.strip()

    @property
    def display_skills(self):
        return f"""
        {self.display_stat('academics')} {self.display_stat('athletics')} {self.display_stat('animal_ken')}
        {self.display_stat('computer')} {self.display_stat('brawl')} {self.display_stat('empathy')}
        {self.display_stat('crafts')} {self.display_stat('drive')} {self.display_stat('expression')}
        {self.display_stat('investigation')} {self.display_stat('firearms')} {self.display_stat('intimidation')}
        {self.display_stat('medicine')} {self.display_stat('larceny')} {self.display_stat('persuasion')}
        {self.display_stat('occult')} {self.display_stat('stealth')} {self.display_stat('socialize')}
        {self.display_stat('politics')} {self.display_stat('survival')} {self.display_stat('streetwise')}
        {self.display_stat('science')} {self.display_stat('weaponry')} {self.display_stat('subterfuge')}
        """.strip()

    @property
    def mental_attributes(self):
        return sum([
            self.intelligence,
            self.wits,
            self.resolve
        ])

    @property
    def physical_attributes(self):
        return sum([
            self.strength,
            self.dexterity,
            self.stamina
        ])

    @property
    def social_attributes(self):
        return sum([
            self.presence,
            self.manipulation,
            self.composure
        ])

    @property
    def mental_skills(self):
        return sum([
            self.academics,
            self.computer,
            self.crafts,
            self.investigation,
            self.medicine,
            self.occult,
            self.politics,
            self.science
        ])

    @property
    def physical_skills(self):
        return sum([
            self.athletics,
            self.brawl,
            self.drive,
            self.firearms,
            self.larceny,
            self.stealth,
            self.survival,
            self.weaponry
        ])

    @property
    def social_skills(self):
        return sum([
            self.animal_ken,
            self.empathy,
            self.expression,
            self.intimidation,
            self.persuasion,
            self.socialize,
            self.streetwise,
            self.subterfuge
        ])
