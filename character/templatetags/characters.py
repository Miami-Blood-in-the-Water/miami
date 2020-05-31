from django import template
from faker import Faker
from character.models import Character, CharacterPage
from random import randint

register = template.Library()


@register.filter
def by_type(arg):
    fake = Faker()
    return [fake.first_name() for _ in range(randint(0, 5))]


@register.filter
def my_characters(user):
    return Character.objects.filter(account=user)


@register.filter
def character_page(character):
    try:
        return CharacterPage.objects.get(character=character)
    except CharacterPage.DoesNotExist:
        return None
