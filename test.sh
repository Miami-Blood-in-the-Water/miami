#!/usr/bin/env bash
evennia migrate
evennia test --settings=settings .
