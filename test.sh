#!/usr/bin/env bash

evennia migrate
coverage run --source=. --omit=*/migrations/*,server/*,*/apps.py,*/tests/*.py,*/tests.py $(which evennia) test --settings=settings .
coveralls