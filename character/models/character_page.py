from django.db.models import OneToOneField, PROTECT, SET_NULL
from wagtail.core.models import Page

from character.models import Character


class CharacterPage(Page):
    character = OneToOneField(Character, on_delete=SET_NULL, null=True, blank=True, unique=True)