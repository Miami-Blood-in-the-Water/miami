from evennia import Command, EvMenu


class CmdChargen(Command):
    key = "chargen"

    def func(self):
        EvMenu(self.caller, "character.chargen")