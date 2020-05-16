from django.test import TestCase
from character.models import Character


class CharacterTestSuite(TestCase):
    def test_can_create_character(self):
        character = Character(1)
        character.save()
        self.assertIsNotNone(character)