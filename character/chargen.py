def start(caller, raw_string, **kwargs):
    text = "Welcome to Miami Character Creation."

    options = [
        {
            "desc": "Select Attributes",
            "goto": "attributes"
        },
        {
            "desc": "Select Skills",
            "goto": "skills"
        },
        {
            "desc": "Select Merits",
            "goto": "merits"
        },
        {
            "desc": "Validate Character",
            "goto": _validate
        }
    ]

    return text, options


_attributes = ["strength", "dexterity", "stamina",
               "intelligence", "wits", "resolve",
               "presence", "manipulation", "composure"]


def attributes(caller, raw_string, attribute=None, **kwargs):
    character = caller.character
    if not attribute:
        text = f"""
        Which attribute do you want to set? Type 'back' to go back to the main menu.

        {"Mental":18} {character.mental_attributes - 3} {"Physical":18} {character.physical_attributes - 3} {"Social":18} {character.social_attributes - 3}

        {character.display_attributes}
        """

        options = [
            {
                "key": "_default",
                "goto": (_in_list, {"list": _attributes})
            }
        ]
    else:
        text = f"What do you want to set {attribute} to?"

        options = [
            {
                "key": "_default",
                "goto": (_set, {"attribute": attribute})
            }
        ]

    return text, options


def _in_list(caller, raw_string, list, **kwargs):
    raw_string = raw_string.strip()

    if raw_string in list:
        return None, {"attribute": raw_string}
    elif raw_string == "back":
        return "start"
    else:
        caller.msg(f"{raw_string} is not a valid attribute, try again.")
        return None


def _set(caller, raw_string, attribute, **kwargs):
    raw_string = raw_string.strip()
    character = caller.character
    original = getattr(character, attribute)
    if raw_string.isdigit():
        raw_string = int(raw_string)
    setattr(character, attribute, raw_string)
    try:
        character.save()
    except ValueError:
        setattr(character, attribute, original)
        caller.msg(f"{raw_string} is not a valid value for {attribute}.")
        return None

    caller.msg(f"You have set {attribute} to {raw_string}.")

    return None, {"attribute": None}


_skills = ["academics", "computer", "crafts", "investigation", "medicine", "occult", "politics", "science"
                                                                                                 "athletics", "brawl",
           "drive", "firearms", "larceny", "stealth", "survival", "weaponry"
                                                                  "animal ken", "empathy", "expression", "intimidation",
           "persuasion", "socialize", "streetwise", "subterfuge"]


def skills(caller, raw_string, attribute=None, **kwargs):
    character = caller.character
    if not attribute:
        text = f"""
        Which skill do you want to set? Type 'back' to go back to the main menu."

        {"Mental":18} {character.mental_skills} {"Physical":18} {character.physical_skills} {"Social":18} {character.social_skills}

        {character.display_skills}
        """

        options = [
            {
                "key": "_default",
                "goto": (_in_list, {"list": _skills})
            }
        ]
    else:
        text = f"What do you want to set {attribute} to?"

        options = [
            {
                "key": "_default",
                "goto": (_set, {"attribute": attribute})
            }
        ]

    return text, options


def _validate_attributes(caller):
    character = caller.character
    physical = character.physical_attributes
    mental = character.mental_attributes
    social = character.social_attributes

    attribs = sorted([physical, mental, social])

    if attribs == [6, 7, 8]:
        return True
    else:
        caller.msg(f"""
Attributes must be 5/4/3, currently:
Mental: {mental - 3}
Physical: {physical - 3}
Social: {social - 3}
        """)
        return False


def _validate_skills(caller):
    character = caller.character
    physical = character.physical_skills
    mental = character.mental_skills
    social = character.social_skills

    attribs = sorted([physical, mental, social])

    if attribs == [4, 7, 11]:
        return True
    else:
        caller.msg(f"""
Skills must be 11/7/4, currently:
Mental: {mental}
Physical: {physical}
Social: {social}
        """)
        return False


_validations = [
    _validate_attributes,
    _validate_skills,
]


def _validate(caller, raw_string, **kwargs):
    valid = all([_v(caller) for _v in _validations])

    if valid:
        caller.msg("Character is valid!")

    return None
