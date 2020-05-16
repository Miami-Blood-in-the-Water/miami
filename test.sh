#!/usr/bin/env bash

evennia makemigrations
evennia migrate
evennia test --settings=settings .