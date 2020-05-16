from django.db.models import Model, CASCADE, OneToOneField
from evennia.objects.models import ObjectDB
from model_utils.managers import InheritanceManager


class Character(Model):
    objects = InheritanceManager()

    character = OneToOneField(ObjectDB, on_delete=CASCADE, primary_key=True)
