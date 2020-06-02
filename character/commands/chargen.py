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
            character = race(character=self.caller, account=self.caller.account)
            character.save()
            self.msg(f'You are now a {args}.')
        except KeyError:
            self.msg("Valid races are:")
            for race in self.races.keys():
                self.msg(race)


class CmdChargen(Command):
    key = "chargen"

    def func(self):
        EvMenu(self.caller, "character.chargen")
