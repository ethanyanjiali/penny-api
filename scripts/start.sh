#!/usr/bin/env bash
gunicorn -w 2 main:app --name penny --daemon