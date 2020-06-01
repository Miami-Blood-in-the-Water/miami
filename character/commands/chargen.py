from evennia import Command, EvMenu

from character.models import Character


class CmdRace(Command):
    key = 'race'

    races = {
        'character': Character
    }

    def func(self):
        args = self.args.strip()
        try:
            race = self.races[args]
            character = race(character=self.caller)
            character.save()
            self.msg(f'You are now a {args}.')
        except KeyError:
            self.msg(f"No such race, {args}.")


class CmdChargen(Command):
    key = "chargen"

    def func(self):
        EvMenu(self.caller, "character.chargen")
