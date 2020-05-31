from django.db.models import Model, CASCADE, OneToOneField, CharField
from evennia.accounts.models import AccountDB
from evennia.objects.models import ObjectDB
from model_utils.managers import InheritanceManager


class Character(Model):
    objects = InheritanceManager()

    character = OneToOneField(ObjectDB, on_delete=CASCADE, primary_key=True)
    account = OneToOneField(AccountDB, on_delete=CASCADE)

    type = CharField(max_length=16, blank=True, editable=False)

    @property
    def name(self):
        return self.character.name

    def save(self, *args, **kwargs):
        self.type = self.__class__.__name__.lower()
        super(Character, self).save(*args, **kwargs)
