#!/usr/bin/env bash

evennia makemigrations
evennia migrate
evennia createsuperuser --no-input --username One --email admin@miamimush.com
evennia start -l